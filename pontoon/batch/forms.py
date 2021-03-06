from django import forms

from pontoon.base import utils
from pontoon.batch.actions import ACTIONS_FN_MAP


class BatchActionsForm(forms.Form):
    """Handles the arguments passed to the batch actions view.
    """

    locale = forms.CharField()
    action = forms.ChoiceField(choices=[(x, x) for x in ACTIONS_FN_MAP.keys()])
    entities = forms.CharField(required=False)
    find = forms.CharField(required=False)
    replace = forms.CharField(required=False)

    def clean_entities(self):
        return utils.split_ints(self.cleaned_data['entities'])
