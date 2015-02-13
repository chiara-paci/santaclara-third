import os
from distutils.core import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='santaclara_third',
    version='0.10.4',
    packages=['santaclara_third'],
    package_data={'santaclara_third': [
            'static/css/*.css',
            'static/css/images/*',
            'static/fonts/*',
            'static/js/ace/snippets/*.js',
            'static/js/ace/*.js',
            'static/js/*.js',
            ]},
    include_package_data=True,
    license='GNU General Public License v3 or later (GPLv3+)',  # example license
    description='A Django app for third part software',
    long_description=README,
    url='http://www.gianoziaorientale.org/software/',
    author='Gianozia Orientale',
    author_email='chiara@gianziaorientale.org',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
