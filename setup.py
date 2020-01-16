# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from aldryn_categories import __version__

# git tag '[version]'
# git push --tags origin master
# python setup.py sdist upload
# python setup.py bdist_wheel upload

setup(
    name='js-categories',
    version=__version__,
    url='https://github.com/compoundpartners/js-categories',
    license='BSD License',
    description='Hierarchical categories/taxonomies for your Django project',
    author='Divio AG',
    author_email='info@divio.ch',
    package_data={},
    packages=find_packages(),
    platforms=['OS Independent'],
    classifiers=[
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
    ],
    install_requires=[
        'django>=1.8,<3.0',
        'django-parler>=1.2.1',
        'django-treebeard>=2.0',
        'aldryn-translation-tools>=0.2.1',
    ],
    include_package_data=True,
    zip_safe=False
)
