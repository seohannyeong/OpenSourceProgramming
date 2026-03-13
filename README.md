# 오늘의 퇴근/퇴사 계산기

사용자가 입력한 목표 시간까지 남은 시간을 계산하고 실시간으로 카운트다운을 보여주는 웹 애플리케이션입니다.

남은 시간을 기반으로 커피, 치킨, 돈 등 재미있는 지표로 변환하여 사용자에게 제공합니다.

## 주요 기능

1. 목표 날짜 및 시간 설정
2. 실시간 카운트다운
3. 남은 시간을 재미있는 값으로 변환

## 실행 방법

Flask 설치

```bash
pip install flask
```

프로그램 실행

```bash
python app.py
```

브라우저에서 접속

```
http://127.0.0.1:5000
```

## 프로젝트 구조

```
project
│
├─ app.py
├─ Requirements.md
├─ README.md
│
├─ templates
│  ├─ index.html
│  ├─ countdown.html
│  └─ convert.html
│
└─ static
   └─ style.css
```
