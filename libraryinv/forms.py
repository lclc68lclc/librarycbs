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
            'publisher_match': _('Publisher'),
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
            'Location': _('Location'),
        }


class LineForm(forms.ModelForm):
    class Meta:
        model = Line

        help_texts = {
            'title': _('Title of the Publication'),
            'price': _('Price'),
            'version': _('Publication Version'),
            'quantity': _('Quantity'),
            }


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice

        help_texts = {
            'invoice_number': _('Invoice Number'),
            'publication_match': _('Publication'),
            'price': _('Price'),
            'tax': _('Tax'),
            'shipping': _('Shipping'),
            'total': _('Total'),
            'date_purchased': _('Date Purchased'),
            'order_type': _('Type of Order (Standing, New, Canceled)'),
            'date_sent_acctg': _('Date Sent to Accounting'),
            }
