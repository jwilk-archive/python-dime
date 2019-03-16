import io
import os

extensions = [
    'sphinx.ext.doctest',
]

source_suffix = '.txt'
master_doc = 'index'

project = 'python-dime'

def get_version():
    path = os.path.join(
        os.path.dirname(__file__),
        'changelog',
    )
    with io.open(path, encoding='UTF-8') as file:
        line = file.readline()
    return line.split()[1].strip('()')

release = version = get_version()

html_theme = 'haiku'
html_show_copyright = False
pygments_style = 'sphinx'

# vim:ts=4 sts=4 sw=4 et
