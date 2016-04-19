
import os
import codecs
from setuptools import setup


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


setup(
    name="ascntr",
    version="0.0.1b",
    url='https://github.com/ashwoods/ascntr',
    license='BSD',
    description="Small simple cron file task reader",
    long_description=read('README.rst'),
    author='Ashley Camba Garrido',
    author_email='ashwoods@gmail.com',
    entry_points={
        'console_scripts': [
            'ascntr = ascntr.cli:cli',
        ],
    },
    packages=['ascntr'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Utilities',
    ],
    install_requires=[
        'click',
    ],
    zip_safe=False,
)
