def req(dt="20120101"):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = "2876d824a15bd70f1bc9323cd14b2276"
    url = f"{base_url}?key={key}&targetDt={dt}"
    print(url)

