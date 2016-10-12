# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetmanage', '0006_auto_20161011_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetmanage',
            name='remote_ip',
            field=models.CharField(default=b'-', max_length=20),
        ),
        migrations.AlterField(
            model_name='assetmanage',
            name='server_ip',
            field=models.CharField(default=b'-', max_length=20),
        ),
    ]
