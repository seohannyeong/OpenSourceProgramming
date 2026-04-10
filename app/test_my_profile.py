import pytest
from datetime import datetime
from app.my_profile import app, get_diff_seconds, get_conversion_stats

@pytest.fixture
def client():
    """Flask 테스트 클라이언트를 제공하는 Pytest 픽스처"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# 1. 시간 계산 함수 테스트
def test_get_diff_seconds():
    target_dt = datetime(2024, 1, 2, 12, 0)
    now_dt = datetime(2024, 1, 2, 10, 0)
    
    # 정상적인 미래 시간 (2시간 = 7200초 차이)
    assert get_diff_seconds(target_dt, now_dt) == 7200
    
    # 목표 시간이 과거일 경우 0을 반환해야 함
    past_target_dt = datetime(2024, 1, 2, 8, 0)
    assert get_diff_seconds(past_target_dt, now_dt) == 0

# 2. 변환 함수 테스트
def test_get_conversion_stats():
    # 1시간(3600초) / 시급 10,000원인 경우
    earned, chickens, coffees = get_conversion_stats(3600, 10000)
    assert earned == 10000
    assert chickens == 0
    assert coffees == 2
    
    # 10시간(36000초) / 최저시급 9,860원인 경우
    earned, chickens, coffees = get_conversion_stats(36000, 9860)
    assert earned == 98600
    assert chickens == 4  # 98600 // 20000
    assert coffees == 21  # 98600 // 4500

# 3. Flask 라우트 테스트
def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200

def test_countdown_route(client):
    response = client.get('/countdown?date=2024-12-31&time=23:59&wage=9860')
    assert response.status_code == 200

def test_stats_route(client):
    # 쿼리 파라미터를 포함한 정상 응답 확인
    response = client.get('/stats?date=2024-12-31&time=23:59&wage=9860')
    assert response.status_code == 200