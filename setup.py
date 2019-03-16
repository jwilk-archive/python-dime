# encoding=UTF-8

# Copyright © 2007-2018 Jakub Wilk <jwilk@jwilk.net>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

'''
*python-dime* provides a way to parse and generate DIME messages.

`Direct Internet Message Encapsulation`_ (DIME) is a binary message format that
can be used to encapsulate multiple payloads into a single message.

.. _Direct Internet Message Encapsulation:
   http://xml.coverpages.org/draft-nielsen-dime-02.txt
'''

import io
import os

import distutils.core
from distutils.command.sdist import sdist as distutils_sdist

try:
    import distutils644
except ImportError:
    pass
else:
    distutils644.install()

exec b''  # Python 2.6 or 2.7 is required

class cmd_sdist(distutils_sdist):

    def maybe_move_file(self, base_dir, src, dst):
        src = os.path.join(base_dir, src)
        dst = os.path.join(base_dir, dst)
        if os.path.exists(src):
            self.move_file(src, dst)

    def make_release_tree(self, base_dir, files):
        distutils_sdist.make_release_tree(self, base_dir, files)
        self.maybe_move_file(base_dir, 'LICENSE', 'doc/LICENSE')

def get_version():
    with io.open('doc/changelog', encoding='UTF-8') as file:
        line = file.readline()
    return line.split()[1].strip('()')

classifiers = '''
Development Status :: 3 - Alpha
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 2
Topic :: Internet
'''.strip().splitlines()

distutils.core.setup(
    name='python-dime',
    version=get_version(),
    license='MIT',
    description='DIME message processing',
    long_description=__doc__.strip(),
    classifiers=classifiers,
    url='http://jwilk.net/software/python-dime',
    author='Jakub Wilk',
    author_email='jwilk@jwilk.net',
    py_modules=['dime'],
    cmdclass=dict(
        sdist=cmd_sdist,
    ),
)

# vim:ts=4 sts=4 sw=4 et
