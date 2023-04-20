from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/robots.txt")
def robots():
	response= 'Part 3: _Sc4v3nger_hunt_w4s_fun}'# Now visit this <a href="final">endpoint</a></div>'''
	return response

@app.route("/final")
def final():
	if request.headers.get('X-Forwarded-For') == '127.0.0.1' and request.headers.get('User-Agent') == 'ThiranBrowser':
		return "Part 5:_fun}"
	elif request.headers.get('X-Forwarded-For') == '127.0.0.1':
		return render_template_string('<p>Part 4:_hunt_w4s<br>Only people who use the official ThiranBrowser are allowed on this site!</p><center><img src=static/whoareyou.gif alt="Loser Image" width="600" height="600">')	

		
	elif request.headers.get('X-Forwarded-For') != '127.0.0.1':
		return render_template_string('<p>This site allows traffic FORWARDED only from localhost</p><center><img src=static/whoareyou.gif alt="Loser Image" width="600" height="600">')

	
	else:
		return render_template_string('<p>Only people who use the official ThiranBrowser are allowed on this site!</p><center><img src=static/whoareyou.gif alt="Loser Image" width="600" height="600">')	

if __name__ == '__main__':
   app.run('127.1',6060,debug=True)