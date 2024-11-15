from django.utils.translation import gettext as _, ngettext

django_standard_messages_to_override = [
    _("Your password can’t be too similar to your other personal information."),
    ngettext(
        "Your password must contain at least %(min_length)d character.",
        "Your password must contain at least %(min_length)d characters.",
        8,
    ) % {"min_length": 8},
    _("Your password can’t be a commonly used password."),
    _("Your password can’t be entirely numeric."),
    _("Enter the same password as before, for verification.")
]
