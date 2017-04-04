# coding: utf-8
from __future__ import unicode_literals

from cms.models import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.utils.html import strip_tags
from django.utils.text import Truncator

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin


@python_2_unicode_compatible
class TeaserSectionBase(AbstractBasePlugin):

    class Meta:
        abstract = True

    def __str__(self):
        return str(_("Teaser Section"))


class TeaserSection(TeaserSectionBase):
    pass
