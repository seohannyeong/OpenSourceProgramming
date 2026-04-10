# 오늘의 퇴근/퇴사 계산기 (Today's Countdown Calculator)

!Python Version
!Flask Version
!Tests
!Docs

> 사용자가 설정한 목표 시간까지 남은 시간을 계산하고, 이를 돈, 치킨, 커피 등 재미있고 직관적인 지표로 변환해 주는 위트 있는 카운트다운 웹 애플리케이션입니다.

## 📸 스크린샷 및 시연 (Demo)
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/e8ab54c5-1f23-4578-ae27-f0a8d2fa3d16" /> <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/bcb919cb-1885-493d-a23c-8306e42ef5a9" />
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/799c83f9-19f8-4dc8-9e75-bf57a9ac6b94" />



## 💡 기획 의도 및 배경 (Motivation)

길고 지루한 업무 시간이나 힘든 프로젝트 기간 동안 단순히 시계를 보는 것은 동기부여가 되지 않습니다. 이 프로젝트는 **"남은 시간을 더 재미있고 체감할 수 있게 만들 수 없을까?"**라는 단순한 아이디어에서 출발했습니다. 시간이 줄어드는 것을 보는 대신, 기다림으로써 "얻게 되는" 긍정적이고 유머러스한 보상(치킨, 커피 등)으로 남은 시간을 재구성하여 목표 시간까지의 지루함을 덜어줍니다.

## 🛠️ 기술 스택 및 선정 이유 (Tech Stack & Rationale)

- **Python**: 높은 가독성과 풍부한 생태계를 고려하여 핵심 언어로 선택했습니다.
- **Flask**: 가볍고 유연한 웹 프레임워크로, 소규모 웹 애플리케이션과 API를 빠르게 구축하는 데 적합하여 채택했습니다.
- **Flasgger (Swagger UI)**: 대화형 API 문서를 자동으로 생성하기 위해 사용했습니다. API를 누구나 쉽게 이해하고 테스트할 수 있도록 전문적인 개발 표준을 따랐습니다.
- **Sphinx**: 파이썬 Docstring을 기반으로 깔끔하고 전문적인 기술 문서 사이트를 구축하기 위해 도입했습니다.
- **Pytest**: 코드의 신뢰성과 유지보수성을 높이고, TDD(테스트 주도 개발) 원칙을 적용하기 위해 선택한 강력한 테스트 프레임워크입니다.

## 🌟 주요 기능 (Key Features)

- **실시간 카운트다운**: 미래의 특정 날짜와 시간을 설정하면 실시간으로 줄어드는 카운트다운을 제공합니다.
- **재치 있는 수치 변환**: 남은 시간을 예상 수익, 치킨 구매 가능 마리 수, 커피 구매 가능 잔 수 등으로 자동 변환합니다.
- **완벽히 문서화된 API**: 상태 확인 및 계산을 위한 5개의 RESTful API 엔드포인트를 제공하며, Swagger UI를 통해 문서화되었습니다.
- **포괄적인 기술 문서**: Sphinx를 통해 생성된 기술 문서 사이트로 코드베이스의 모든 함수와 클래스를 명확히 설명합니다.
- **단위 테스트 (Unit Test)**: 핵심 로직과 API 엔드포인트에 대한 단위 테스트를 작성하여 안정성을 확보했습니다.

## 🚀 시작하기 (Getting Started)

**1. 저장소 클론 및 폴더 이동**

```bash
git clone https://github.com/seohannyeong/opensourceprogramming.git
cd opensourceprogramming
```

**2. 필수 패키지 설치**

```bash
pip install flask flasgger sphinx pytest
```

**3. 프로그램 실행**

```bash
python -m app.my_profile
```

**4. 브라우저 접속**

- 메인 웹 서비스: `http://127.0.0.1:5000`
- API 문서 (Swagger): `http://127.0.0.1:5000/apidocs`

## 📚 공식 문서 (Documentation)

- **Sphinx 기술 문서**: https://seohannyeong.github.io/OpenSourceProgramming/

## 🧠 배운 점 및 트러블슈팅 (Lessons Learned)

프로젝트를 진행하며 가장 큰 과제 중 하나는 동일한 Docstring 내에 두 가지 다른 문서화 철학을 통합하는 것이었습니다. Flasgger는 API 명세에 YAML 형식을 사용하는 반면, Sphinx는 reStructuredText를 사용합니다. Sphinx 빌드 시 경고(Warning)가 발생하지 않도록 하면서 두 형식이 완벽하게 공존하게 하려면, 사람이 읽는 설명과 기계가 읽는 API 명세 사이에 빈 줄을 추가하는 등 세심한 포맷팅이 필요했습니다. 이 과정을 통해 다목적으로 활용되는 코드베이스를 유지보수하고 문서화하는 실질적인 방법을 배울 수 있었습니다.

## 📁 프로젝트 구조 (Project Structure)

```text
c:\opensourceprogramming\
├─ app/
│  ├─ __init__.py
│  ├─ my_profile.py
│  ├─ templates/
│  └─ static/
├─ docs/                 # Sphinx 문서 폴더
├─ test_my_profile.py    # Pytest 테스트 코드
└─ README.md
```
