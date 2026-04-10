import pytest
from datetime import datetime
from app.my_profile import app, get_diff_seconds, get_conversion_stats

@pytest.fixture
def client():
    """A Pytest fixture that provides a Flask test client."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# 1. Test for time calculation function
def test_get_diff_seconds():
    target_dt = datetime(2024, 1, 2, 12, 0)
    now_dt = datetime(2024, 1, 2, 10, 0)
    
    # Normal future time (2 hours = 7200 seconds difference)
    assert get_diff_seconds(target_dt, now_dt) == 7200
    
    # Should return 0 if the target time is in the past
    past_target_dt = datetime(2024, 1, 2, 8, 0)
    assert get_diff_seconds(past_target_dt, now_dt) == 0

# 2. Test for conversion function
def test_get_conversion_stats():
    # Case: 1 hour (3600s) / hourly wage of 10,000 KRW
    earned, chickens, coffees = get_conversion_stats(3600, 10000)
    assert earned == 10000
    assert chickens == 0
    assert coffees == 2
    
    # Case: 10 hours (36000s) / minimum wage of 9,860 KRW
    earned, chickens, coffees = get_conversion_stats(36000, 9860)
    assert earned == 98600
    assert chickens == 4  # 98600 // 20000
    assert coffees == 21  # 98600 // 4500

# 3. Test for Flask routes
def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200

def test_countdown_route(client):
    response = client.get('/countdown?date=2024-12-31&time=23:59&wage=9860')
    assert response.status_code == 200

def test_stats_route(client):
    # Check for a successful response with query parameters
    response = client.get('/stats?date=2024-12-31&time=23:59&wage=9860')
    assert response.status_code == 200