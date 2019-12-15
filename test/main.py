#!/usr/bin/env python3

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../..')

from helm_python.Helm import Helm

test = Helm()
print('ok')