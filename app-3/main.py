from flask import *



app = Flask(__name__)
app.secret_key = 'qrack{Use_AES_to_decrypt_the_author}'

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/hello")
def hello_ssti():
    blacklist=['config','self','"']
    template=''
    if request.args.get('name'):
        name = request.args.get('name')
        for x in blacklist:
            if x in name:
                return 'Hacking attempt!!!'
        template = f'''<div>
        <h1>Hello {name}</h1><center><img src="static/loser.jpg" alt="Loser Image" width="600" height="600"></center>
        </div>
        '''
    return render_template_string(template)

if __name__ == '__main__':
   app.run('127.1',7070,debug=True)
