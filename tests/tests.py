import yaml
import pprint



def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"



def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]



def test_some_primes():
    assert 37 in {
        num
        for num in range(1, 50)
        if num != 1 and not any([num % div == 0 for div in range(2, num)])
    }



def test_ap_prof():
    with open('../implementation/roles/ap/vars/main.yml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        for k, v in data.items():
            pprint.pprint(list(v))
            for i in v:
                assert (i.get('tenant') == 'common' and i.get('description') == 'default')
                assert "ap_" in str(i)



#import re

#if any(re.findall(r'a|b|c', str, re.IGNORECASE)):
#    print 'possible matches thanks to regex'
#else:
#    print 'no matches'

