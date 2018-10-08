import enco_deco
import db_url
from flask import render_template,request,Flask,redirect


#initializing the app
app = Flask(__name__,template_folder='templates')

#home page
@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

#url shortening
#
@app.route('/short',methods=['GET','POST'])
def long_to_shot():
    big_url=request.form['url']
    mini_url = enco_deco.short(big_url)
    db_url.post(big_url,mini_url)
    return render_template('short.html',url=mini_url[0])

#redirecting to the actual url using the short url
@app.route("/<name>")
def short_to_long(name):
    long_url=db_url.get(name)
    return redirect(long_url,code=302)



if __name__=="__main__":
    app.run()