from django import forms
from .models import ContactMessage, Skill, Certification, Milestone


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name']


class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = '__all__'

class MilestoneForm(forms.ModelForm):
    class Meta:
        model = Milestone
        fields = ['title', 'subtitle', 'year']