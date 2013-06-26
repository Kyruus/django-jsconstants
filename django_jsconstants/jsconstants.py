from django.utils import simplejson
from collections import defaultdict
import sys

_constants = defaultdict(lambda: defaultdict())

def register_all(path):
    """
    Register all the constants in the class given by <path>
    """
    module = sys.modules[path]
    for name in dir(module):
        attr = getattr(module, name)
        
        if not callable(attr) and _is_constant(name):
            _add_constant(path, name, attr)

def register_all_except(path, *exceptions):
    """
    Register all the constants in the class given by <path>,
        except those named in <constants>
    """
    module = sys.modules[path]
    for name in dir(module):
        attr = getattr(module, name)
    
        if not callable(attr) and name not in exceptions and _is_constant(name):
            _add_constant(path, name, attr)

def register(path, *constants):
    """
    Register only the constants specified by the arguments, in the class
        specified by <path>
    """
    module = sys.modules[path]
    for name in constants:
        try:
            attr = getattr(module, name)
        except AttributeError:
            raise ValueError("{0} is not a valid constant name.".format(name))

        if not callable(attr):
            _add_constant(path, name, attr)
        else:
            raise ValueError("\'{0}\' is a callable object, expected variable.".format(name))

def get_constants_json(*modules):
    """
    Get the JSON object for the constants in the specified modules
    """
    filtered_constants = {module: _constants[module] for module in modules}
    return simplejson.dumps(filtered_constants)

def _is_constant(name):
    """
    Determine whether a given name is a constant variable name
    """
    return name == name.upper()

def _add_constant(path, name, val):
    _constants[path][name] = val

def _reset_all():
    """
    Provided for testing purposes
    """
    _constants.clear()
