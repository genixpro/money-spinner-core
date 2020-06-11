import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open('requirements.txt', 'rt') as f:
    requires = f.readlines()

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest >= 3.7.4',
    'pytest-cov',
]

setup(
    name='moneyspinner',
    version='0.0',
    description='',
    long_description="",
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='',
    author_email='',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    package_data={
        'moneyspinner': [`
            "tiles/*.json"
        ]
    },
    install_requires=requires,
    entry_points={
        'console_scripts': [
            "moneyspinner = moneyspinner.bin.moneyspinner"
        ]
    },
)

