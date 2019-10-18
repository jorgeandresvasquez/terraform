import os
import subprocess

# Simple script to bump the patch number of the version (i.e., from 2.1.11 to 2.1.12)

with open(os.path.join('../global.yml'), 'r') as f:
    __version__ = None
    exec(f.read())

if __version__:
    version = [int(x) for x in __version__.split('.')]
    if len(version) == 3:
        version[2] += 1
    __version__ = '.'.join([str(x) for x in version])
    with open(os.path.join('../global.yml'), 'w') as f:
        f.write('__version__ = \'{}\''.format(__version__))

subprocess.check_output(['git', 'commit', '../global.yml', '-m', 'bump version to {}'.format(__version__)])
subprocess.check_output(['git', 'tag', __version__])
