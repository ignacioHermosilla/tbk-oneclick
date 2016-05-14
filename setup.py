# encoding=UTF-8
#!/usr/bin/env python
import os
from setuptools import setup, find_packages

setup(
    name='tbk-oneclick',
    version='0.1',
    description='',
    long_description='',
    author='Ignacio Hermosilla',
    author_email='hi@ignacio.im',
    maintainer='Ignacio  Hermosilla',
    maintainer_email='hi@ignacio.im',
    licence='MIT',
    url='https://github.com/ignacioHermosilla/tbk-oneclick',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='transbank oneclick one_click webpay tbk chile payments pago',
    install_requires=[
        'pyopenssl',
        'arrow',
        'rsa',
        'requests',
        'urllib3',
        'pyasn1',
        'ndg-httpsclient'],
    tests_require=[
        'mock>=1.0.1',
        'nose>=1.3.3',
    ],
    packages=find_packages(),
    test_suite='nose.collector',
    zip_safe=True,
)