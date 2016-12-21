import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

import wordsegment

class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        import tox
        errno = tox.cmdline(self.test_args)
        sys.exit(errno)

with open('README.rst') as fptr:
    readme = fptr.read()

with open('LICENSE') as fptr:
    license = fptr.read()

setup(
    name='wordsegment',
    version=wordsegment.__version__,
    description='English word segmentation.',
    long_description=readme,
    author='Grant Jenks',
    author_email='contact@grantjenks.com',
    url='http://www.grantjenks.com/docs/wordsegment/',
    license=license,
    py_modules=['wordsegment'],
    packages=['wordsegment_data'],
    package_data={'wordsegment_data': ['*.txt']},
    tests_require=['tox'],
    cmdclass={'test': Tox},
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
