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
    
    # Cette partie du code ne fonctionne pas. Et je ne sais pas pourquoi
    def __init__(self, *args, **kwargs):
        super(RptForms, self).__init__(*args, **kwargs)
        self.fields['genre'].empty_label = "Choisissez"
        self.fields['genre'].required = True
        self.fields['conseiller'].required = True
        self.fields['depister'].required = True
        self.fields['resultat'].required = True
        self.fields['resultat_recu'].required = True
        self.fields['beneficiant_CD4'].required = True
    #-------------------------------------------------------------------------------------