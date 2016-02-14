
import fnmatch
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


def recursive_include(directory, patterns):
    result = []
    for root, dirs, files in os.walk(directory):
        child_root = root.replace(directory, '').lstrip('/')
        for pattern in patterns:
            result.extend([os.path.join(child_root, name)
                           for name in fnmatch.filter(files, pattern)])
    return result

# be careful with the syntax of this line since it is parsed from
# the docs/conf.py file
VERSION = '0.1.0'

setup(
    name='mariandb',
    version=VERSION,
    url='https://github.com/enriquepablo/mariandb',
    license='BSD',
    description=('Marian DB'),
    #long_description=(read('README.rst') + '\n\n' + read('CHANGES.rst')),
    author='enriquepablo',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    packages=find_packages('.'),
    package_dir={'mariandb': 'mariandb'},
    package_data={
        'mariandb': recursive_include('mariandb',
                            ['*.html', '*.css', '*.js', '*.txt',
                             '*.png', '*.ico', '*.wsgi', '*.xsd'])
    },
    zip_safe=False,
    install_requires=[
        'Django==1.9.2',
        'django-bootstrap3==6.2.2',
        'django-admin-bootstrapped>=2.5.7',
    ],
    extras_require = {
        'PG': ['psycopg2 == 2.5.4',],
    },
    dependency_links=[
    ]
)
