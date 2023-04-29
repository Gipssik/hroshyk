from django.forms import Field, CharField, IntegerField


def donation_add_validation(form, obj):
    for field_name in ("nickname", "amount", "message"):
        field: Field = form.fields[field_name]
        field.widget.attrs["placeholder"] = getattr(obj, f"{field_name}_placeholder")
        if isinstance(field, CharField):
            field.widget.attrs["maxlength"] = getattr(obj, f"{field_name}_max_length")
            field.widget.attrs["minlength"] = getattr(obj, f"{field_name}_min_length")
        elif isinstance(field, IntegerField):
            field.widget.attrs["max"] = getattr(obj, f"{field_name}_max")
            field.widget.attrs["min"] = getattr(obj, f"{field_name}_min")
