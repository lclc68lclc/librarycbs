__author__ = 'Linac'

from django import forms
from django.utils.translation import ugettext_lazy as _
from libraryinv.models import *


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication

        help_texts = {
            'publication_number': _('Publication Number'),
            'publication_title': _('Title of the Publication'),
            'publication_type': _('Type of Publication'),
            'location': _('Location'),
            'price': _('Price'),
            }

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher

        help_texts = {
            'publisher': _('Publisher Name'),
            'account_number': _('Account Number'),
            'publication_number': _('Publication Number (ex. ISBN or reference number'),
            'publication_title': _('Name of Publication'),
            'version': _('Version'),
            'publication_type': _('Type of Publication'),
            'Location': _('Location'),
        }