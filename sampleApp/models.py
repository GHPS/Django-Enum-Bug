from django.db import models

from django.utils.translation import gettext_lazy as _

class sampleModel(models.Model):

    class eAssets(models.IntegerChoices):
        dvd       =1, _('DVD')
        bluray    =3, _('Blu-ray')
        none      =0, _('-')

    id=models.BigAutoField(primary_key=True)
    stTitle=models.CharField(max_length=80)
    eAsset=models.PositiveSmallIntegerField(choices=eAssets.choices, default=eAssets.none)
