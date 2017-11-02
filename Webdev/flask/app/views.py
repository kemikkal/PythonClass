from flask import Flask
app = Flask(__name__)
#sets the url path of the app
@app.route('/home')

def home():
    return('hompage')
@app.route('/home2')
def home2():
    return('second homepage')
if __name__=="__main__":
    app.run()
