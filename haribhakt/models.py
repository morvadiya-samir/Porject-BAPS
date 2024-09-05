from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _
from core.constants import HaribhaktConstants
from mandal.models import Mandal
from core.models import File
from core.managers import HaribhaktManager

class BaseModel(TimeStampedModel):
    ACTIVE = 0
    DELETED = 1

    STATUS = (
        (ACTIVE, _('Active')),
        (DELETED, _('Deleted')),
    )
    status = models.IntegerField(_("The life cycle status of this object"), choices=STATUS, blank=True, null=True,default=ACTIVE)

    class Meta:
        abstract = True

class Haribhakt(BaseModel):
    name = models.CharField(_("Name of Haribhakt"), max_length=1024, blank=True, null=True)
    is_gunbhavi = models.BooleanField(_("Is Haribakt gunbhavi or not ?"), default=False)
    gender = models.CharField(_("Gender"), choices=HaribhaktConstants.GENDER_CHOICES, max_length=16)
    is_head_of_family = models.BooleanField(_("Is Haribakt Head of Family ?"), default=False)
    relation_with_hof = models.CharField(_("Relation with Head of Family"), max_length=1024, blank=True, null=True)
    head_of_family = models.ForeignKey('self', on_delete=models.CASCADE,blank=True, null=True)
    contact_number_1 = models.CharField(_("Contact number 1"), max_length=10, blank=True, null=True)
    contact_number_2 = models.CharField(_("Contact number 2"), max_length=10, blank=True, null=True)
    contact_number_3 = models.CharField(_("Contact number 3"), max_length=10, blank=True, null=True)
    birth_date = models.DateField(_("Date of Birth"), blank=True, null=True)
    number_of_years_of_satsang = models.SmallIntegerField(_("Number of years of satsang"), blank=True, null=True)

    nitya_pooja = models.BooleanField(_("Nitya Pooja ?"), default=True)
    tilak_chaandlo = models.BooleanField(_("Tilak Chaandlo ?"), default=True)
    vyasan = models.BooleanField(_("Vyasan ?"), default=False)
    vyasan_type = models.CharField(_("Type of vyasan"), max_length=1024, blank=True, null=True)

    onion_garlic = models.BooleanField(_("Onion and Garlic ?"), default=False)
    weekly_sabha = models.BooleanField(_("Weekly Sabha ?"), default=True)
    poonam_sabha = models.BooleanField(_("Poonam Pooja ?"), default=False)
    ghar_sabha = models.BooleanField(_("Ghar Sabha ?"), default=True)
    vachnamrut_swami_ni_vaato_vanchan = models.BooleanField(_("Vachnamrut Swami ni vaato nu Vaanchan ?"), default=True)
    satsang_sikshan_pariksha = models.BooleanField(_("Satsang Sikshan Pariksha ?"), default=True)
    monthtly_donation = models.IntegerField(_("Monthly Donation ?"), blank=True, null=True)

    file = models.ForeignKey(File, on_delete=models.CASCADE,blank=True, null=True)
    mandal = models.ForeignKey(Mandal, on_delete=models.CASCADE,blank=True, null=True)
    objects = HaribhaktManager()

    def __unicode__(self):
        # Number: 9854815789, Call Text: lhvhslvhlvsv, SMS Text: jhdvjkdhvkdj, Outcomes Type: 1/2/3
        return "ID: " + str(self.id) + " Name : " + self.name