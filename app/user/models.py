# core/user/models.py
from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils.translation import gettext_lazy as _
from sorl.thumbnail import ImageField

SOCIAL_CHOICES = {
    "instagram": _("Instagram"),
    "pixelfed": _("Pixelfed"),
    "facebook": _("Facebook"),
    "x": _("X"),
    "mastodpn": _("Mastodon"),
    "website": _("WebSite"),
    "flickr": _("FlickR"),
    "500px": _("500px"),
}


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None, **kwargs):
        """Create and return a `User` with an
        email, phone number, username and password."""
        if username is None:
            raise TypeError("Users must have a username.")
        if email is None:
            raise TypeError("Users must have an email.")

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError("Superusers must have a password.")
        if email is None:
            raise TypeError("Superusers must have an email.")
        if username is None:
            raise TypeError("Superusers must have an username.")

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class Socials(models.Model):
    """Social networks"""

    network = models.CharField(choices=SOCIAL_CHOICES)
    url = models.URLField(max_length=200)

    def __str__(self):
        return f"{self.network} - {self.url}"


class User(AbstractUser, PermissionsMixin):
    """Custom user model"""

    username = models.CharField(db_index=True, max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(
        db_index=True, unique=True, null=True, blank=True
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_photographer = models.BooleanField(default=True)
    avatar = ImageField(blank=True, default="", upload_to="user")
    socials = models.ManyToManyField(Socials)
    description = models.TextField(blank=True, default="")
    introduction = models.TextField(blank=True, default="")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"
