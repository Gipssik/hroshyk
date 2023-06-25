import requests
from django.contrib.auth import get_user_model
from django_twitch_auth.authbackends import TwitchBackend as BaseTwitchBackend
from django_twitch_auth.settings import TWITCH_USERS_URL, TWITCH_CLIENT_ID, TWITCH_USERNAME_FIELD, TWITCH_EMAIL_FIELD

User = get_user_model()


class TwitchBackend(BaseTwitchBackend):
    def authenticate(self, request, token=None):
        response = requests.get(
            TWITCH_USERS_URL,
            headers={
                "Accept": "application/vnd.twitchtv.v5+json",
                "Client-ID": TWITCH_CLIENT_ID,
                "Authorization": f"Bearer {token}",
            },
        )
        if response.ok:
            user_information = response.json()["data"][0]
            user_data = {
                TWITCH_USERNAME_FIELD: user_information["login"],
                TWITCH_EMAIL_FIELD: user_information.get("email"),
                "auth_id": user_information["id"],
                "profile_image_url": user_information.get("profile_image_url"),
            }
            try:
                user = User.objects.get(auth_id=user_data["auth_id"])
                modified = False
                for field_name in (TWITCH_USERNAME_FIELD, TWITCH_EMAIL_FIELD):
                    if getattr(user, field_name) != user_data[field_name]:
                        setattr(user, field_name, user_data[field_name])
                        modified = True
                if modified:
                    user.donation_page.page_link = user_data[TWITCH_USERNAME_FIELD]
                    user.donation_page.save()
                    user.save()
            except User.DoesNotExist:
                user = User.objects.create_user(**user_data)
            return user
        return None
