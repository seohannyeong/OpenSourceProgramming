from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

# --- Constants ---
SECONDS_PER_HOUR = 3600
CHICKEN_PRICE = 20000
COFFEE_PRICE = 4500
DEFAULT_WAGE = 9860

def get_diff_seconds(target_dt, now):
    diff_seconds = (target_dt - now).total_seconds()
    return max(0, diff_seconds)

def get_conversion_stats(diff_seconds, wage):
    earned = int((diff_seconds / SECONDS_PER_HOUR) * wage)
    chickens = earned // CHICKEN_PRICE
    coffees = earned // COFFEE_PRICE
    return earned, chickens, coffees

class TargetDateTime:
    def __init__(self, date, time):
        self.datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")

def get_request_params():
    target_date = request.args.get('date')
    target_time = request.args.get('time')
    wage = request.args.get('wage', DEFAULT_WAGE)
    return target_date, target_time, wage

def calculate_stats(target_dt, wage):
    now = datetime.now()
    diff_seconds = get_diff_seconds(target_dt, now)
    return get_conversion_stats(diff_seconds, wage)

@app.route("/")
def index():
    # 1. 목표 설정 페이지
    return render_template('index.html')

@app.route("/countdown")
def countdown():
    # 2. 실시간 카운트다운 페이지
    target_date, target_time, wage = get_request_params()
    target_iso = f"{target_date}T{target_time}"
    
    return render_template('countdown.html', 
                           target_date=target_date, 
                           target_time=target_time, 
                           wage=wage, 
                           target_iso=target_iso)

@app.route("/stats")
def stats():
    # 3. 위트 있는 변환 수치 페이지
    target_date, target_time, wage = get_request_params()
    wage = int(wage)
    
    target_dt_obj = TargetDateTime(target_date, target_time)
    earned, chickens, coffees = calculate_stats(target_dt_obj.datetime, wage)
    
    return render_template('stats.html',
                           target_date=target_date,
                           target_time=target_time,
                           wage=wage,
                           earned="{:,}".format(earned),
                           chickens=chickens,
                           coffees=coffees)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
