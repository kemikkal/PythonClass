from flask import Flask, render_template , request
app = Flask(__name__)
#create a url
@app.route('/' , methods = ['post', 'get'])

def index():
    name=""
    age=""
    '''title = request.args.get('title ', 'no title')
    name = request.args.get('name', 'Nobody')'''
    greeting = "Hello"
    day = "saturday"
    if request.method =='post':
        print("in the post req")
        name2 = request.form['name']
        age = request.form['pw']
        title = age
        print(title)

        return render_template('index.html' , title=title , day = day, greeting = greeting)

    else:
        return render_template('index.html' , title=title , day = day, greeting = greeting)



if __name__ == "__main__":
    app.run(debug=True)
