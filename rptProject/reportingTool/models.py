from django.db import models
from django.core.exceptions import ValidationError
import re



# Create your models here.

class Post_depistage(models.Model):
    
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title



class Patient(models.Model):

    def code_patient_validate(value):
        reg = re.compile('^[0-9]{4}\/[a-zA-Z0-9]{2}\/[0-3][0-9]\/[0-9]{5}(e|E){0,1}1{0,1}[0-9]{0,1}$')
        if not reg.match(value):
            raise ValidationError(u'%s n\'est pas un code patient valide' % value)
    
    code_patient = models.CharField(max_length=25, validators=[code_patient_validate])

    
    GENDER_CHOICES = (
        ('Masculin', 'Masculin'),
        ('Feminin', 'Feminin'),
    )
    genre = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)


    def age_validate(value):
        if value > 120:
            raise ValidationError(u'%s n\'est pas un âge valide' % value)
    age = models.PositiveSmallIntegerField(validators=[age_validate], null=True)

    # INFORMATION SUR LE TEST DE DÉPISTAGE

    CONSEILLER_CHOICES = (
            ('OUI', 'OUI'),
            ('NON', 'NON'),
        )
    conseiller = models.CharField(max_length=1, choices=CONSEILLER_CHOICES, blank=True)


    depister = models.BooleanField(null=True)

    RESULTAT_TEST_CHOICES = (
        ('P', 'Positif'),
        ('N', 'Négatif'),
        ('I', 'Indéterminer'),
        ('C', 'Statut connu')
    )
    resultat = models.CharField(max_length=1, choices=RESULTAT_TEST_CHOICES, blank=True)

    resultat_recu = models.BooleanField(null=True) # On veut les conseillés et dépistés ayants reçu leur resultats
                                          # On veut les positifs ayants reçu leur résultat
    
    beneficiant_CD4 = models.BooleanField(null=True) # Positif bénéficiant d'un CD4 (Seuls les positifs en bénéficient)

    def __str__(self):
        return self.code_patient

