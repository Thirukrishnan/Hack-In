from flask import *
import hashlib

app = Flask(__name__,static_folder='static')

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/s3cr3t',methods=['POST','GET'])
def get_secret():
   cookie_gen=hashlib.md5("Web Challenge Explaining what cookies and how to get them".encode()).hexdigest()
   if request.method=='POST':
      cookie_value=request.cookies.get("my_cookie")
      if cookie_value == '':
         response=make_response('Setting a cookie')
         response.set_cookie('my_cookie',cookie_gen)
      else:
         return 'Everyone gets only one Cookie!!!'
   else:
      cookie_value=request.cookies.get("my_cookie")
      if cookie_value == cookie_gen:
         response="thiran{C00kie_4_d4y_k33p5_th3_l0g1n_p4g3_away}"
      else:
         response="Look for the secret snack"

   return response



if __name__ == '__main__':
   app.run('127.1',9090,debug=True)