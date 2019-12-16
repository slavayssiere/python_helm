#!/usr/bin/env python3

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../..')

from helm_python.Helm import Helm

hlm = Helm(debug=True)

tst_set = [
    {
        'name': 'image.tag',
        'value': '2.0.0'
    },
    {
        'name': 'image.name',
        'value': 'eu.gcr.io/slavayssiere/web-test'
    },
    {
        'name': r'grafana."grafana\.ini"."auth\.google"',
        'value': 'SECRET'
    },
    {
        'name': 'alertmanager.config.receivers[0].slack_configs[0].api_url',
        'value': 'ANOTHER_SECRET'
    }
]

hlm.upgrade('my-nginx', 'stable/nginx', namespace='web', value_file_path='../nginx/values.yaml', sets=tst_set)

print('ok')