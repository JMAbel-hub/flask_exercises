# Worked with Joe Onghena 
from flask import render_template, Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def get_date_time():
    temp_date = datetime.now()
    return render_template('index.html', date = temp_date.strftime("%A, %B %d %Y %H:%M:%S") )

if __name__ == '__main__':
    app.run()