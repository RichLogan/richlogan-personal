import os
from flask import Flask, render_template
from datetime import datetime
from pytz import timezone
import pytz
app = Flask(__name__)

@app.route('/')
def index():
	#london = timezone('Europe/London')
	#londonTime = datetime.now(london)
	#sanJose = timezone('America/Los_Angeles')
	#sanJoseTime = datetime.now(sanJose)
	return render_template('index.html')
	#, londonTime = londonTime.strftime('%d/%m %H:%M'), sanJoseTime = sanJoseTime.strftime('%d/%m %H:%M'))

if __name__ == "__main__":
	app.run(debug=True)