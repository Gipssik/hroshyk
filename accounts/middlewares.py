from django_twitch_auth.middlewares import TwitchAuthenticationMiddleware


class AuthenticationMiddleware(TwitchAuthenticationMiddleware):
    def __call__(self, request):
        if request.user.is_authenticated:
            return self.get_response(request)
        return super().__call__(request)
