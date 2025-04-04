import json
import random
from typing import Optional

from django.contrib.auth import get_user_model
from django.contrib.gis.db import models as gis_models
from django.db import models
from django.template.defaultfilters import slugify  # new
from django.utils.translation import gettext_lazy as _
from exif import Image
from sorl.thumbnail import ImageField
from taggit.managers import TaggableManager


class Album(models.Model):
    """Album"""

    label = models.CharField(
        max_length=100, verbose_name=("Label"), unique=True
    )
    description = models.TextField(verbose_name=("Description"), default="")
    timestamp_create = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default="", null=False, unique=True)

    def __str__(self):
        return f"{self.label}"

    def save(self, *args, **kwargs):
        if not self.slug or self.slug == "":
            self.slug = slugify(self.label)
            print(self.slug)
        return super().save(*args, **kwargs)


class Tags(models.Model):
    """Image tags"""

    label = models.CharField(max_length=100, verbose_name=("Label"))
    timestamp_create = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.label}"


class Photo(models.Model):
    """
    A class thaat determines how photos will be saved into the database
    """

    name = models.CharField(max_length=244, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"))
    city = models.CharField(max_length=244, verbose_name=_("City"), blank=True)
    country = models.CharField(
        max_length=244, verbose_name=_("Country"), blank=True
    )
    geom = gis_models.PointField(
        srid=4326, verbose_name=_("Geometry"), blank=True, null=True
    )
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, verbose_name=_("Album")
    )
    # tags = models.ManyToManyField(Tags)
    tags = TaggableManager()
    photographer = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name=_("Photographer"),
        blank=True,
        null=True,
    )
    exif_data = models.JSONField(
        verbose_name=_("Exif data"), blank=True, null=True
    )
    timestamp_create = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)
    image = ImageField(upload_to="photo")
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        """
        String representation
        """
        return f"{self.name}"

    @property
    def exif_dict(self) -> Optional[dict]:
        """Exif data as dict"""
        return json.loads(self.exif_data) if self.exif_data else None

    @property
    def exif_full(self):
        """Get full exif data from image"""
        exif = Image(self.image)
        print(exif.get_all())
        if exif.has_exif:
            data = {exif.get_all()[key] for key in exif.get_all()}
            return data
        return {}

    @classmethod
    def show_all_photos(cls):
        """
        A method to return all photos posted in order of the most
        recent to oldest
        """
        return cls.objects.order_by("timestamp_create")[::-1]

    @classmethod
    def show_random_photo(cls):
        """
        A method which returns a random photo
        """
        all_photos = cls.show_all_photos()
        random_id = random.randint(1, len(all_photos))

        return cls.objects.get(id=random_id)

    @classmethod
    def delete_photo(cls, pk):
        """
        A method to delete an object
        """

        return cls.objects.filter(pk=pk).delete()

    @classmethod
    def get_photo_by_id(cls, pk):
        """
        A method to get a photo based on its id
        """
        return cls.objects.filter(pk=pk)[0]

    @classmethod
    def search_photo_by_category(cls, search):
        """
        A method to return all photos that fall under a certain catergory
        """
        return cls.objects.filter(categories__name__icontains=search)

    @classmethod
    def filter_by_location(cls, pk):
        """
        A method to filter all photos based on the location in which they were
        taken
        """
        return cls.objects.filter(location__id=pk)

    def save(self, *args, **kwargs):
        exif = Image(self.image)
        print(exif.get_all())
        if exif.has_exif:
            data = {
                key: exif.get_all()[key]
                for key in [
                    "lens_model",
                    "lens_make",
                    "artist",
                    "model",
                    "make",
                    "aperture_value",
                    "exposure_bias_value",
                    "focal_length",
                    "focal_length_in_35mm_film",
                    "datetime_original",
                    "photographic_sensitivity",
                    "exposure_time",
                ]
                if key in exif.get_all()
            }
            self.exif_data = json.dumps(data)
        return super().save(*args, **kwargs)
