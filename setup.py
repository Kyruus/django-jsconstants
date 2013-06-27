from distutils.core import setup

setup(
    name='django-jsconstants',
    version='1.0',
    packages=['django_jsconstants',],
    include_package_data=True,
    license='Apache 2.0 license',
    description='An interface to communicate constants between Python and Javascript.',
    long_description=README,
    author='Kyruus',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License', 
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
