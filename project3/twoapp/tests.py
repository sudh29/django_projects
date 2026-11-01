from django.test import TestCase, Client
from django import forms
from twoapp.templatetags.form_filters import addclass


class SampleForm(forms.Form):
    title = forms.CharField()


class TwoAppTests(TestCase):
    def test_addclass_filter(self):
        form = SampleForm()
        rendered_field = addclass(form["title"], "form-control custom-input")
        self.assertIn('class="form-control custom-input"', str(rendered_field))
