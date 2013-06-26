from django.utils.unittest import TestCase
from django.template import Template, Context
from django.conf import settings

from django_jsconstants import jsconstants

CONSTANT_1 = '1'
CONSTANT_2 = '2'
CONSTANT_3 = '3'
not_a_constant = '4'    

class JsConstantsTemplateTagTests(TestCase):
    
    def tearDown(self):
        jsconstants._reset_all()

    def test_import_module(self):
        jsconstants.register_all(__name__)

        t = Template("{% load jsconstants %}" + 
                    "JSConstants: {% jsconstants \""+__name__+"\"%}")

        output = t.render(Context())
        self.assertIn("CONSTANT_1", output)
        self.assertIn("CONSTANT_2", output)
        self.assertIn("CONSTANT_3", output)
        self.assertIn(__name__, output)

