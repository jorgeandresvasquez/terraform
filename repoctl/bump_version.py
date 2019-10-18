import os
import subprocess
import yaml

PROJECT_ROOT_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../')
GLOBALS_PATH = os.path.join(PROJECT_ROOT_PATH, 'global.yml')

# Simple script to bump the patch number of the version (i.e., from 2.1.11 to 2.1.12)

def read_from_globals(global_property):
    external_vars = {}
    if not os.path.isfile(GLOBALS_PATH):
        raise RuntimeError(
            "Could not find file specified in variable {}".format(GLOBALS_PATH))

    with open(GLOBALS_PATH, 'r') as fd:
        external_vars = yaml.load(fd.read(), Loader=yaml.FullLoader)
        return external_vars[global_property]

def set_global_value(global_property_name, global_property_value):
    with open(GLOBALS_PATH) as f:
        doc = yaml.load(f, Loader=yaml.FullLoader)

    doc[global_property_name] = global_property_value

    with open(GLOBALS_PATH, 'w') as f:
        yaml.dump(doc, f)

current_version = read_from_globals('versionNumber')
if current_version:
    print(current_version)
    version_arr = [int(x) for x in current_version.split('.')]
    if len(version_arr) == 3:
        version_arr[2] += 1
    new_version = '.'.join([str(x) for x in version_arr])
    set_global_value('versionNumber', new_version)
    print(GLOBALS_PATH)
    subprocess.check_output(['git', 'commit', GLOBALS_PATH, '-m', 'bumped version to {}'.format(new_version)])
    subprocess.check_output(['git', 'tag', new_version])
    subprocess.check_output(['git', 'push', '--follow-tags'])
