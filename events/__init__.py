from os.path import basename, dirname, join
from glob import glob

PYGLOB = '*.py'

pwd = dirname(__file__)

for module in glob(join(pwd, PYGLOB)):
    if not module.startswith('__'):
        __import__(basename(module)[:-3], globals(), locals())
