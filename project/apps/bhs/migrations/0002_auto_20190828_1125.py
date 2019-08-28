# Generated by Django 2.2.4 on 2019-08-28 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bhs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='email',
            field=models.EmailField(blank=True, editable=False, help_text='\n            The contact email of the resource.', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, editable=False, help_text='\n            The contact email of the resource.', max_length=254, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='group',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='group',
            constraint=models.UniqueConstraint(fields=('bhs_id', 'kind'), name='unique_group_kind'),
        ),
    ]
