from django import forms
from django.core.mail import send_mail

from django.conf import settings
from .models import SingUp


class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()

    subject = 'Contact form'
    from_email = settings.EMAIL_HOST_USER
    to_email = [from_email, ]
    contact_message = "foo  "#str(full_name) + str(email) + str(message)

    send_mail(subject, contact_message, from_email, to_email,
              fail_silently=True)


class SingUpForm(forms.ModelForm):
    # list_display = ['__str__', 'timestamp', 'updated']
    class Meta:
        model = SingUp
        fields = [ 'full_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # email_base, provider = email.split('@')
        # domain, extension = provider.split('.')
        # if not extension == '.edu':
        #     raise forms.ValidationError('Use a valid University email.')
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        return full_name
