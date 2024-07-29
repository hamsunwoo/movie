import requests
import os
import pandas as pd
import datetime

def req(dt="20120101"):
    #url = gen_url('20240720')
    url = gen_url(dt)
    r = requests.get(url)
    data = r.json()
    code = r.status_code
    print(data)
    return code, data

def gen_url(dt="20120101"):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = get_key()
    url = f"{base_url}?key={key}&targetDt={dt}"

    return url

def get_key():
    """영화진흥위원회 가입 및 API 키 생성 후 환경변수 선언 필요"""
    key = os.getenv('MOVIE_API_KEY')
    return key

def req2list():
    _, data = req()
    l = data['boxOfficeResult']['dailyBoxOfficeList']

    return l

def list2df():
    l = req2list()
    df = pd.DataFrame(l)

    return df

def save2df():
    df = list2df()
    #df에 load_df 컬럼 추가 조회 일자 YYYYMMDD 형식
    current = datetime.datetime.now()
    dates = pd.to_datetime(current.strftime('%Y%m%d'))
    df['load_dt'] = dates
    #아래 파일 저장시 load_df 기준으로 파티셔닝
    df.to_parquet('~/data/parquet/load_dt', partition_cols=['load_dt'])
    
    return df
