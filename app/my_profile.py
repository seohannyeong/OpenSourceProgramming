from flask import Flask, request, render_template, jsonify
from datetime import datetime
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

# --- Constants ---
SECONDS_PER_HOUR = 3600
CHICKEN_PRICE = 20000
COFFEE_PRICE = 4500
DEFAULT_WAGE = 9860

def get_diff_seconds(target_dt, now):
    """
    Calculates the difference between the target time and current time in seconds.
    
    :param target_dt: Target date and time (datetime object)
    :param now: Current date and time (datetime object)
    :return: Remaining time (in seconds, 0 if in the past)
    """
    diff_seconds = (target_dt - now).total_seconds()
    return max(0, diff_seconds)

def get_conversion_stats(diff_seconds, wage):
    """
    Calculates the expected earnings, and the number of chickens and coffees that can be purchased based on the remaining time.

    :param diff_seconds: Remaining time (seconds)
    :param wage: Hourly wage to apply (KRW)
    :return: Expected earnings, number of chickens, number of coffees (tuple)
    """
    earned = int((diff_seconds / SECONDS_PER_HOUR) * wage)
    chickens = earned // CHICKEN_PRICE
    coffees = earned // COFFEE_PRICE
    return earned, chickens, coffees

class TargetDateTime:
    """A class that manages and converts target date and time into a datetime object."""
    def __init__(self, date, time):
        self.datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")

def get_request_params():
    """Extracts target date, time, and wage from the request's query parameters."""
    target_date = request.args.get('date')
    target_time = request.args.get('time')
    wage = request.args.get('wage', DEFAULT_WAGE)
    return target_date, target_time, wage

def calculate_stats(target_dt, wage):
    """Calculates the remaining time until the target time and returns the converted stats."""
    now = datetime.now()
    diff_seconds = get_diff_seconds(target_dt, now)
    return get_conversion_stats(diff_seconds, wage)

@app.route("/")
def index():
    """
    Main page (Target setting)
    
    ---
    
    responses:
      200:
        description: Renders a form where users can input the target date and time.
    """
    # 1. Target setting page
    return render_template('index.html')

@app.route("/countdown")
def countdown():
    """
    Real-time countdown page
    
    ---
    
    parameters:
      - name: date
        in: query
        type: string
        required: true
      - name: time
        in: query
        type: string
        required: true
      - name: wage
        in: query
        type: integer
        required: false
        default: 9860
    responses:
      200:
        description: Renders the real-time countdown page.
    """
    # 2. Real-time countdown page
    target_date, target_time, wage = get_request_params()
    target_iso = f"{target_date}T{target_time}"
    
    return render_template('countdown.html', 
                           target_date=target_date, 
                           target_time=target_time, 
                           wage=wage, 
                           target_iso=target_iso)

@app.route("/stats")
def stats():
    """
    Witty conversion stats page
    
    ---
    
    parameters:
      - name: date
        in: query
        type: string
        required: true
      - name: time
        in: query
        type: string
        required: true
      - name: wage
        in: query
        type: integer
        required: false
    responses:
      200:
        description: Renders a page showing expected earnings, and the number of chickens and coffees.
    """
    # 3. Witty conversion stats page
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

@app.route("/api/health")
def api_health():
    """
    Health check API
    
    ---
    
    responses:
      200:
        description: Returns the health status of the API server.
    """
    # 4. 서버 상태 확인용 API
    return jsonify({"status": "ok", "message": "Server is running smoothly."})

@app.route("/api/calculate")
def api_calculate():
    """
    Calculate remaining time and stats API
    
    ---
    
    parameters:
      - name: date
        in: query
        type: string
        required: true
      - name: time
        in: query
        type: string
        required: true
      - name: wage
        in: query
        type: integer
        required: false
        default: 9860
    responses:
      200:
        description: Returns calculated stats in JSON format.
    """
    # 5. 계산 결과 JSON 반환 API
    target_date, target_time, wage = get_request_params()
    wage = int(wage)
    target_dt_obj = TargetDateTime(target_date, target_time)
    earned, chickens, coffees = calculate_stats(target_dt_obj.datetime, wage)
    
    return jsonify({"earned_krw": earned, "chickens": chickens, "coffees": coffees})

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
