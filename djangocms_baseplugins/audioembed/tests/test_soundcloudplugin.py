from __future__ import unicode_literals

from django.test import TestCase

from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase

from ..cms_plugins import AudioEmbedPlugin


class AudioEmbedPluginTests(BasePluginTestCase, TestCase):
    plugin_class = AudioEmbedPlugin
    plugin_path = "djangocms_baseplugins.audioembed"

    def get_plugin_default_data(self):
        return {
            "audioembed_url": "https://soundcloud.com/grappainc/sinatras-movenr137?",
        }
