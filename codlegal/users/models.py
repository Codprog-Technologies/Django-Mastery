from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):

    class RoleChoices(models.TextChoices):
        ADVOCATE = "AD", "Advocate"
        CLIENT = "CL", "Client"

    class TimeZoneChoices(models.TextChoices):
        ASIA_KOLKATA = "Asia/Kolkata", "Asia/Kolkata"
        AMERICA_SAO_PAULO = "America/Sao_Paulo", "America/Sao_Paulo"
        ASIA_JAKARATA = "Asia/Jakarta", "Asia/Jakarta"

    username = None
    email = models.EmailField(_("email address"), blank=False, unique=True)
    dob = models.DateField(null=True, verbose_name=_("Date of Birth"))
    role = models.CharField(max_length=2, choices=RoleChoices, blank=True, verbose_name=_("role"))
    timezone = models.CharField(max_length=25, choices=TimeZoneChoices, default=TimeZoneChoices.ASIA_KOLKATA)

    REQUIRED_FIELDS = ["dob"]
    USERNAME_FIELD = "email"

    objects = CustomUserManager()


class PhoneNumber(models.Model):
    number = models.CharField(_("Phone Number"), max_length=20, validators=[validators.MinLengthValidator(9)])
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="phone_number_set", related_query_name="phone_number")


class AdvocateProfile(models.Model):

    website_url = models.URLField(verbose_name=_("Website Url"))
    practicing_from = models.DateField(verbose_name=_("Practicing From"))
    educational_qualifications = models.CharField(max_length=30, verbose_name=_("Educational Qualifications"))
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="advocate_profile", related_query_name="advocate_profile")
    # user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    practice_areas = models.ManyToManyField("appointments.PracticeArea", related_name="advocate_profile_set", related_query_name="advocate_profile")
    image = models.ImageField(upload_to="profiles/", blank=True, verbose_name=_("Image"))