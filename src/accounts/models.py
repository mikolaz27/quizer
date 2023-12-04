from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from accounts.managers import CustomerManager


class Customer(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_("Name"), max_length=150, blank=True)
    last_name = models.CharField(_("Surname"), max_length=150, blank=True)

    email = models.EmailField(_("Email address"), unique=True)
    phone_number = PhoneNumberField(_("Phone number"), null=True, blank=True)

    is_staff = models.BooleanField(
        _("Staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("Active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. " "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("Date joined"), default=timezone.now)
    birth_date = models.DateTimeField(_("Birth_date"), null=True, blank=True)
    avatar = models.ImageField(_("Avatar"), upload_to="media/img/avatars", null=True, blank=True)

    objects = CustomerManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("customer")
        verbose_name_plural = _("customers")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def get_period_of_registration(self):
        return f"Time on site: {timezone.now() - self.date_joined}"
