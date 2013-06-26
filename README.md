django-jsconstants
==================
Django-jsconstants is an interface for communicating constants between Python code and frontend Javascript. 
This allows you to avoid hardcoding constants into your Javascript, as that is prone to breaking silently and 
unpredictably when the underlying codebase changes. Jsconstants is robust and fail-fast: changing a constant's value won't 
affect behavior, while changing a constant's name (or removing it) will throw a detectable Javascript error.
  
Registering a module's constants
--------------------------------
Before you can import constants into a template, they must first be registered into the `jsconstants` module.

Example: `myapp/models.py`

.. code-block: python

    from django_jsconstants import jsconstants
    
    COLOR_RED = "FF250D"
    COLOR_MAGENTA = "FF00A9"
    SOME_CONSTANT = "not_needed"
    
    jsconstants.register(__name__, "COLOR_RED", "COLOR_MAGENTA")
    
    class MyAppModel...
    
The first argument to the `register...` methods is the path to the module being registered. There are several variations of 
the `register` method:

* `register_all(module)` - finds and registers all variables in ALL_CAPS. Careful! These constants will be publicly visible in 
    the template, so take care to not register sensitive constants like private keys.
* `register_all_except(module, *exceptions)` - finds and registers all variables in ALL_CAPS, except those specified.
* `register(module, *constants)` - only register the constants specified.




Sharing constants through a template tag
----------------------------------------

In your template, simply use the `jsconstants` template tag and pass it a list of modules that you'd like to import.

Example file:`yourproject/templates/yourproject/base.html`

.. code-block: html

    {% load jsconstants %}

    <html>
        <head>
            {% jsconstants "myapp.models" "utilsapp.tools" %}
        </head>
        <body>

        </body>
    </html>

Using the constants in your Javascript
--------------------------------------

From inside of any Javascript function or file on the page, you can access the global ``jsconstants`` object to retrieve 
registered constants.

.. code-block:: javascript

    var COLOR_CHOICE_RED = jsconstants.get('myapp.models', 'COLOR_RED');
