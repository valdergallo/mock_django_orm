from django.test import TestCase
from app.forms import FormAppOne


class TestForm(TestCase):

    def test_invalid_name_form(self):
        form = FormAppOne({'name': '1234', 'description': 'validate name'})
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors, {'name': [u'Name must be only text']})

    def test_invalid_description_form(self):
        form = FormAppOne({'name': 'asd'})
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors, {'description':
                          [u'This field is required.']})

    def test_required_fields(self):
        form = FormAppOne({})
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors, {'name': [u'This field is required.'],
                          'description': [u'This field is required.']})

    def test_valid_form(self):
        form = FormAppOne({'name': 'valder', 'description': 'validate name'})
        self.assertTrue(form.is_valid())

    def test_save_valid_form(self):
        form = FormAppOne({'name': 'valder', 'description': 'validate name'})
        self.assertTrue(form.save())
