import requests
from django.db import models

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin
from djangocms_baseplugins.baseplugin.utils import check_migration_modules_needed

check_migration_modules_needed("audioembed")


class AudioEmbedModelMixin(object):
    """
    needs "audioembed_url" and "oembed_info" fields on model
    """

    def save(self):
        needs = False
        if self.id:
            obj = self.__class__.objects.filter(id=self.id).first()
            if obj and not obj.audioembed_url == self.audioembed_url:
                needs = True
        elif self.audioembed_url:
            needs = True
        if needs:
            self.populate_oembed_infos()
        super().save()

    def populate_oembed_infos(self):
        url = None
        if "soundcloud.com/" in self.audioembed_url:
            url = "https://soundcloud.com/oembed"
            params = {
                # "format": "json",
                "url": self.audioembed_url,
                # "maxheight": "166",
            }
        elif "mixcloud.com/" in self.audioembed_url:
            url = "https://app.mixcloud.com/oembed"
            params = {
                "url": self.audioembed_url,
            }
        elif "spotify.com/" in self.audioembed_url:
            url = "https://open.spotify.com/oembed"
            params = {
                "url": self.audioembed_url,
            }
        if url:
            response = requests.get(url, params)
            if response.status_code == 200:
                self.oembed_info = response.json()
        return {}


class AudioEmbed(AudioEmbedModelMixin, AbstractBasePlugin):
    audioembed_url = models.URLField()
    color = models.CharField(
        max_length=32,
        default="",
        blank=True,
    )
    oembed_info = models.JSONField(
        default=dict,
        blank=True,
    )
    autoplay = models.BooleanField(
        default=False,
    )
    show_comments = models.BooleanField(
        default=False,
    )

    def to_string(self):
        return "Audio Embed ({})".format(self.audioembed_url)
