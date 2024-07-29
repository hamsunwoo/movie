# mov

### install
```bash
# main
$ pip install git+https://github.com/hamsunwoo/movie.git

# branch
$ pip install git+https://github.com/hamsunwoo/movie.git@<BRANCH_NAME>
pip install git+https://github.com/hamsunwoo/movie.git@0.2/api
```

### start dev
```bash
$ git clone <URL>
$ cd <DIR> 
$ source .venv/bin/activate
$ pdm install
$ pytest

#option
$ pdm venv create
```

### setting env
```bash
#MY_ENV
export MOVIE_API_KEY="<KEY>"
```

### 트러블슈팅 
- [] 영화진흥위원회 API 키 생성
```
{'message': '유효하지않은 키값입니다.', 'errorCode: '320010'}
```
