import re
import shutil
from subprocess import run, call, PIPE


class Helm:

  def __init__(self):
    # test if helm is in PATH
    if shutil.which('helm') is None:
      print('Helm is not installed')
      return

    # test Helm version
    p = run(["helm", "version"], check=True, stdout=PIPE).stdout
    m = re.search('"v(\d+?).(\d+?).(\d+?)-?[^"]*"', str(p))
    if m:
      major = m.group(1)
      minor = m.group(2)
      patch = m.group(3)
    else:
      print('No regex version available')
      return

    if int(major) < 3:
      print('This package only work with Helm 3.x.y')

    print("Using Helm Major: " + major + ". Minor: " + minor + ". Patch: " + patch)
    
  def upgrade(self, name, path, namespace='default', value_file_path='', sets=[]):

    # MANDATORY : all helm upgrade command must start with
    command = [
      "helm",
      "upgrade",
      "--install",
      "--namespace", namespace
    ]

    if len(value_file_path) > 0:
      command.append("--values")
      command.append(value_file_path)
    else:
      print('No file value')

    if len(sets) > 0:
      set_string = ''
      for i, set in sets:
        if i == 0:
          set_string = set['name'] + "=" + set['value']
        else:
          set_string = set_string + "," + set['name'] + "=" + set['value']
      command.append("--set")
      command.append(set_string)
        
    else:
      print('No value add')


    # MANDATORY : these two arguments must be the last
    command.append(name)
    command.append(path)

    # call the command locally
    call(command)
