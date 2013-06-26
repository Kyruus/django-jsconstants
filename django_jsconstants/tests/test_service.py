from django.utils.unittest import TestCase
from django.utils import simplejson

from django_jsconstants import jsconstants

CONSTANT_1 = '1'
CONSTANT_2 = '2'
CONSTANT_3 = '3'
not_a_constant = '4'    

class JsConstantsServiceTests(TestCase):

    def tearDown(self):
        jsconstants._reset_all()
        obj = self.jsconstants_get_obj()
        self.assertEqual(len(obj[__name__]), 0)

    def jsconstants_get_obj(self):
        json = jsconstants.get_constants_json(__name__)
        return simplejson.loads(json)

    def test_register_all(self):
        jsconstants.register_all(__name__)

        obj = self.jsconstants_get_obj()

        self.assertEqual(len(obj), 1)

        self.assertTrue("CONSTANT_1" in obj[__name__])
        self.assertEqual(obj[__name__]["CONSTANT_1"], CONSTANT_1)
        self.assertTrue("CONSTANT_2" in obj[__name__])
        self.assertEqual(obj[__name__]["CONSTANT_2"], CONSTANT_2)
        self.assertFalse("not_a_constant" in obj[__name__])

    def test_register_single(self):
        jsconstants.register(__name__, "CONSTANT_1")

        obj = self.jsconstants_get_obj()

        self.assertTrue("CONSTANT_1" in obj[__name__])
        self.assertEqual(obj[__name__]["CONSTANT_1"], CONSTANT_1)

        self.assertEqual(len(obj), 1)
        self.assertEqual(len(obj[__name__]), 1)

    def test_register_multiple(self):
        jsconstants.register(__name__, "CONSTANT_1", "CONSTANT_3")

        obj = self.jsconstants_get_obj()
        
        self.assertTrue("CONSTANT_1" in obj[__name__])
        self.assertEqual(obj[__name__]["CONSTANT_1"], CONSTANT_1)
        self.assertTrue("CONSTANT_3" in obj[__name__])
        self.assertEqual(obj[__name__]["CONSTANT_3"], CONSTANT_3)

        self.assertEqual(len(obj[__name__]), 2)

    def test_register_except(self):
        jsconstants.register_all_except(__name__, "CONSTANT_2", "CONSTANT_3")

        obj = self.jsconstants_get_obj()

        self.assertEqual(len(obj), 1)

        self.assertTrue("CONSTANT_1" in obj[__name__])
        self.assertEqual(obj[__name__]["CONSTANT_1"], CONSTANT_1)

        self.assertEqual(len(obj[__name__]), 1)

    def test_register_method(self):
        self.assertRaises(ValueError, jsconstants.register, __name__, "test_register_method")

    def test_register_nonexistent(self):
        self.assertRaises(ValueError, jsconstants.register, __name__, "random_var")
