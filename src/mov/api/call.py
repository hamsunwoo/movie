import requests
import os
import pandas as pd

def echo(yaho):
    return yaho

def req(load_dt="20120101", url_param={}):
    url = gen_url(load_dt, url_param)
    r = requests.get(url)
    data = r.json()
    code = r.status_code
    print(data)
    return code, data

def gen_url(dt="20120101", url_param={}):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = get_key()
    url = f"{base_url}?key={key}&targetDt={dt}"
    for key, value in url_param.items():
        url = url + f"&{key}={value}"

    return url

def get_key():
    """영화진흥위원회 가입 및 API 키 생성 후 환경변수 선언 필요"""
    key = os.getenv('MOVIE_API_KEY')
    return key

def req2list(load_dt='20120101', url_param={}):
    _, data = req(load_dt, url_param)
    l = data['boxOfficeResult']['dailyBoxOfficeList']

    return l

def list2df(load_dt='20120101', url_param={}):
    l = req2list(load_dt, url_param)
    df = pd.DataFrame(l)

    return df

def save2df(load_dt='20120101', url_param={}):
    df = list2df(load_dt, url_param)
    df['load_dt'] = load_dt
    #아래 파일 저장시 load_df 기준으로 파티셔닝
    #df.to_parquet('~/tmp/test_parquet/load_dt', partition_cols=['load_dt'])
    
    return df

def apply_type2df(load_dt="20120101", path="~/tmp/test_parquet/load_dt"):
    df = pd.read_parquet(f'{path}/load_dt={load_dt}')
    
    num_cols = ['rnum', 'rank', 'rankInten', 'salesAmt', 'audiCnt',
                'audiAcc', 'scrnCnt', 'showCnt', 'salesShare', 'salesInten',
                'salesChange', 'audiInten', 'audiChange']
    
    #for col_name in num_cols:
    #   df[col_name] = pd.to_numeric(df[col_name])

    df[num_cols] = df[num_cols].apply(pd.to_numeric)

    return df
