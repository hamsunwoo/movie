from  mov.api.call import gen_url, req, get_key, req2dataframe

def test_비밀키숨기기():
    key = get_key()
    assert key

def test_gen_url():
    url = gen_url()
    assert "http" in url
    assert "kobis" in url

def test_req():
    code, data = req()
    assert code == 200

    code, data = req('20240710')
    assert code == 200

def test_req2dataframe():
    l = req2dataframe()
    assert len(l) >= 1
    v = l[0]
    assert 'rnum' in v.keys()
    assert v['rnum'] == '1'
