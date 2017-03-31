import io
import os

extensions = [
    'sphinx.ext.doctest',
]

source_suffix = '.txt'
master_doc = 'index'

project = 'python-dime'
copyright = '2013, Jakub Wilk'

def get_version():
    path = os.path.join(
        os.path.dirname(__file__),
        'changelog',
    )
    with io.open(path, encoding='UTF-8') as changelog:
        return changelog.readline().split()[1].strip('()')

release = version = get_version()

html_theme = 'haiku'
pygments_style = 'sphinx'

# vim:ts=4 sts=4 sw=4 et
