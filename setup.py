import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-teachest',
    version='0.1',
    packages=['teachest'],
    include_package_data=True,
    license='GPLv2 License',  # example license
    description='Django app to monitor & graph tea production & consumption.',
    long_description=README,
    url='http://www.vam.ac.uk/',
    author='V&A Digital Media Team',
    author_email='webmaster@vam.ac.uk',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPLv2 License', 
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
