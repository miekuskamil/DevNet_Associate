import yaml
import pprint

def test_ap_prof():
    try:
        with open('implementation/roles/ap/vars/main.yml') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            for k, v in data.items():
                pprint.pprint(list(v))
                for i in v:
                    assert (i.get('tenant') == 'common' and i.get('description') == 'default') ### check if dict values equal to common/default
                    assert "ap_" in str(i.values())   ### check if ap_ prefix in dict 
                    assert "abc" not in str(i.values())   ### check if abc in dict 
                    assert ("name" in i.keys())   ### check if name in dict keys
    except IOError:
        print("File not accessible")
    finally:
        f.close()
