from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    # 1. 목표 설정 페이지
    return render_template('index.html')

@app.route("/countdown")
def countdown():
    # 2. 실시간 카운트다운 페이지
    target_date = request.args.get('date')
    target_time = request.args.get('time')
    wage = request.args.get('wage')
    target_iso = f"{target_date}T{target_time}"
    
    return render_template('countdown.html', 
                           target_date=target_date, 
                           target_time=target_time, 
                           wage=wage, 
                           target_iso=target_iso)

@app.route("/stats")
def stats():
    # 3. 위트 있는 변환 수치 페이지
    target_date = request.args.get('date')
    target_time = request.args.get('time')
    wage = int(request.args.get('wage', 9860))
    
    target_dt = datetime.strptime(f"{target_date} {target_time}", "%Y-%m-%d %H:%M")
    now = datetime.now()
    
    diff_seconds = (target_dt - now).total_seconds()
    if diff_seconds < 0: diff_seconds = 0
    
    earned = int((diff_seconds / 3600) * wage)
    chickens = earned // 20000
    coffees = earned // 4500
    
    return render_template('stats.html',
                           target_date=target_date,
                           target_time=target_time,
                           wage=wage,
                           earned="{:,}".format(earned),
                           chickens=chickens,
                           coffees=coffees)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
