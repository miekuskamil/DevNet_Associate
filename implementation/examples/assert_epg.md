```bash
Paste CSV file content and finish with Ctrl+D
common  ap_1    epg_1   default bd_192.168.1.255/24     null
commons aps_2   epg_2   default b_192.168.2.0/24        null
        ap_3    epg_3   default bd_192.168.3.0/24       null
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'


PLAY [localhost] ****************************************************************************************************************************************************************************************************************************

TASK [parse csv to yaml] ********************************************************************************************************************************************************************************************************************
changed: [localhost]

TASK [call epg variables] *******************************************************************************************************************************************************************************************************************
ok: [localhost]

TASK [epg syntax checker - single block] ****************************************************************************************************************************************************************************************************
ok: [localhost] => (item={'tenant': 'common', 'app_prof': 'ap_1', 'name': 'epg_1', 'description': 'default', 'bd': 'bd_192.168.1.255/24'})
failed: [localhost] (item={'tenant': 'commons', 'app_prof': 'aps_2', 'name': 'epg_2', 'description': 'default', 'bd': 'b_192.168.2.0/24'}) => {"ansible_loop_var": "item", "assertion": "item.app_prof | regex_search('^ap\\_.*')", "changed": false, "evaluated_to": false, "item": {"app_prof": "aps_2", "bd": "b_192.168.2.0/24", "description": "default", "name": "epg_2", "tenant": "commons"}, "msg": "FAIL"}
failed: [localhost] (item={'tenant': '', 'app_prof': 'ap_3', 'name': 'epg_3', 'description': 'default', 'bd': 'bd_192.168.3.0/24'}) => {"ansible_loop_var": "item", "assertion": "item.tenant != \"\"", "changed": false, "evaluated_to": false, "item": {"app_prof": "ap_3", "bd": "bd_192.168.3.0/24", "description": "default", "name": "epg_3", "tenant": ""}, "msg": "FAIL"}
...ignoring

TASK [epg syntax checker - tenant existence] ************************************************************************************************************************************************************************************************
ok: [localhost] => (item={'tenant': 'common', 'app_prof': 'ap_1', 'name': 'epg_1', 'description': 'default', 'bd': 'bd_192.168.1.255/24'})
ok: [localhost] => (item={'tenant': 'commons', 'app_prof': 'aps_2', 'name': 'epg_2', 'description': 'default', 'bd': 'b_192.168.2.0/24'})
failed: [localhost] (item={'tenant': '', 'app_prof': 'ap_3', 'name': 'epg_3', 'description': 'default', 'bd': 'bd_192.168.3.0/24'}) => {"ansible_loop_var": "item", "assertion": "item.tenant != \"\"", "changed": false, "evaluated_to": false, "item": {"app_prof": "ap_3", "bd": "bd_192.168.3.0/24", "description": "default", "name": "epg_3", "tenant": ""}, "msg": "Tenant not defined"}
...ignoring

TASK [epg syntax checker - tenant common existence] *****************************************************************************************************************************************************************************************
ok: [localhost] => (item={'tenant': 'common', 'app_prof': 'ap_1', 'name': 'epg_1', 'description': 'default', 'bd': 'bd_192.168.1.255/24'})
ok: [localhost] => (item={'tenant': 'commons', 'app_prof': 'aps_2', 'name': 'epg_2', 'description': 'default', 'bd': 'b_192.168.2.0/24'})
failed: [localhost] (item={'tenant': '', 'app_prof': 'ap_3', 'name': 'epg_3', 'description': 'default', 'bd': 'bd_192.168.3.0/24'}) => {"ansible_loop_var": "item", "assertion": "item.tenant | regex_search('common')", "changed": false, "evaluated_to": false, "item": {"app_prof": "ap_3", "bd": "bd_192.168.3.0/24", "description": "default", "name": "epg_3", "tenant": ""}, "msg": "Tenant common not defined"}
...ignoring

TASK [epg syntax checker - bd subnet /24 existence] *****************************************************************************************************************************************************************************************
ok: [localhost] => (item={'tenant': 'common', 'app_prof': 'ap_1', 'name': 'epg_1', 'description': 'default', 'bd': 'bd_192.168.1.255/24'})
ok: [localhost] => (item={'tenant': 'commons', 'app_prof': 'aps_2', 'name': 'epg_2', 'description': 'default', 'bd': 'b_192.168.2.0/24'})
ok: [localhost] => (item={'tenant': '', 'app_prof': 'ap_3', 'name': 'epg_3', 'description': 'default', 'bd': 'bd_192.168.3.0/24'})

TASK [epg syntax checker - app profile name] ************************************************************************************************************************************************************************************************
ok: [localhost] => (item={'tenant': 'common', 'app_prof': 'ap_1', 'name': 'epg_1', 'description': 'default', 'bd': 'bd_192.168.1.255/24'})
failed: [localhost] (item={'tenant': 'commons', 'app_prof': 'aps_2', 'name': 'epg_2', 'description': 'default', 'bd': 'b_192.168.2.0/24'}) => {"ansible_loop_var": "item", "assertion": "item.app_prof | regex_search('^ap\\_.*')", "changed": false, "evaluated_to": false, "item": {"app_prof": "aps_2", "bd": "b_192.168.2.0/24", "description": "default", "name": "epg_2", "tenant": "commons"}, "msg": "App profile syntax not correct"}
ok: [localhost] => (item={'tenant': '', 'app_prof': 'ap_3', 'name': 'epg_3', 'description': 'default', 'bd': 'bd_192.168.3.0/24'})
...ignoring

TASK [epg syntax checker - epg profile name] ************************************************************************************************************************************************************************************************
ok: [localhost] => (item={'tenant': 'common', 'app_prof': 'ap_1', 'name': 'epg_1', 'description': 'default', 'bd': 'bd_192.168.1.255/24'})
ok: [localhost] => (item={'tenant': 'commons', 'app_prof': 'aps_2', 'name': 'epg_2', 'description': 'default', 'bd': 'b_192.168.2.0/24'})
ok: [localhost] => (item={'tenant': '', 'app_prof': 'ap_3', 'name': 'epg_3', 'description': 'default', 'bd': 'bd_192.168.3.0/24'})

TASK [epg syntax checker - bd name] *********************************************************************************************************************************************************************************************************
ok: [localhost] => (item={'tenant': 'common', 'app_prof': 'ap_1', 'name': 'epg_1', 'description': 'default', 'bd': 'bd_192.168.1.255/24'})
failed: [localhost] (item={'tenant': 'commons', 'app_prof': 'aps_2', 'name': 'epg_2', 'description': 'default', 'bd': 'b_192.168.2.0/24'}) => {"ansible_loop_var": "item", "assertion": "item.bd | regex_search('^bd\\_(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\/24')", "changed": false, "evaluated_to": false, "item": {"app_prof": "aps_2", "bd": "b_192.168.2.0/24", "description": "default", "name": "epg_2", "tenant": "commons"}, "msg": "BD profile syntax not correct"}
ok: [localhost] => (item={'tenant': '', 'app_prof': 'ap_3', 'name': 'epg_3', 'description': 'default', 'bd': 'bd_192.168.3.0/24'})
...ignoring

PLAY RECAP **********************************************************************************************************************************************************************************************************************************
localhost                  : ok=9    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=5


Do you wish to see variable file now? Yy/Nn: y
---
epg:
 - {tenant: "common", app_prof: "ap_1", name: "epg_1", description: "default", bd: "bd_192.168.1.255/24"}
 - {tenant: "commons", app_prof: "aps_2", name: "epg_2", description: "default", bd: "b_192.168.2.0/24"}
 - {tenant: "", app_prof: "ap_3", name: "epg_3", description: "default", bd: "bd_192.168.3.0/24"}
```
