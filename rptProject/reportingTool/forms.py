from django import forms
from .models import Patient

class RptForms(forms.ModelForm):

    class Meta:
        model = Patient

        fields = ('code_patient', 'genre', 'age', 'conseiller',
         'depister', 'resultat', 'resultat_recu', 'beneficiant_CD4')

        labels = {
            'code_patient':'Code du Patient',
            'genre':'Sexe',
            'age':'Âge',
            'conseiller':'Conseiller pour le test',
            'depister':'Éffectivement dépisté',
            'resultat':'Résultat du test de dépistage',
            'resultat_recu':'Positif ayant reçu son résultat',
            'beneficiant_CD4':'Positif bénéficiant d\'un CD4'
        }
        
    