'''
python-dime provides a way to parse and generate DIME messages.

Direct Internet Message Encapsulation (DIME) is a binary message format that can be used to encapsulate multiple payloads into a single message.\
'''

classifiers = '''\
Development Status :: 3 - Alpha
Intended Audience :: Developers
License :: OSI Approved :: GNU General Public License (GPL)
Operating System :: OS Independent
Programming Language :: Python
Topic :: Software Development :: Libraries :: Python Modules'''.split('\n')

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

setup(
	name = 'python-dime',
	version = '0.1',
	license = 'GNU GPL 2',
	platforms = ['any'],
	description = 'DIME message processing',
	long_description = __doc__.strip(),
	classifiers = classifiers,
	url = 'http://python-dime.googlecode.com/',
	author = 'Jakub Wilk',
	author_email = 'ubanus@users.sf.net',
	py_modules = ['dime']
)

# vim:ts=4 sw=4 noet
