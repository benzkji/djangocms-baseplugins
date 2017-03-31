# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('textimage', '0002_textimage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textimage',
            name='image',
            field=filer.fields.image.FilerImageField(related_name='textimage_textimage_image', on_delete=django.db.models.deletion.SET_NULL, verbose_name='image', to='filer.Image', null=True),
        ),
    ]