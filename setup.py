import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-tornado-websockets',
    description="Simple way to use WebSockets for Django with Tornado",
    long_description=README,
    author='Hugo ALLIAUME',
    author_email='kocal@live.fr',
    install_requires=[
        'Django>=1.8',
        'tornado>=4.3',
        'six>=1.10',
    ],
    package_dir={'': 'tornado_websockets'},
    packages=find_packages('tornado_websockets'),
    setup_requires=['setuptools-git-version'],
    version_format='{tag}',
    include_package_data=True,
    license='GPLv3 License',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP'
    ]
)
