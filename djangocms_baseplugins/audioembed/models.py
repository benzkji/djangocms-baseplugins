from json import JSONDecodeError

import requests
from django.db import models

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin
from djangocms_baseplugins.baseplugin.utils import check_migration_modules_needed

check_migration_modules_needed("audioembed")


class AudioEmbed(AbstractBasePlugin):
    audioembed_url = models.URLField()
    color = models.CharField(
        max_length=32,
        default="",
        blank=True,
    )
    autoplay = models.BooleanField(
        default=False,
    )
    show_comments = models.BooleanField(
        default=False,
    )

    def to_string(self):
        return "AudioEmbed ({})".format(self.audioembed_url)

    def get_oembed(self):
        """
        docs: https://developers.audioembed.com/docs/oembed#introduction
        """
        url = "https://audioembed.com/oembed"
        params = {
            "format": "json",
            "url": self.audioembed_url,
            "maxheight": "166",
        }
        response = requests.get(url, params=params)
        try:
            return response.json()
        except JSONDecodeError:
            return {}
