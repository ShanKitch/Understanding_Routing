from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"



@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say(name):
    if type(name) == str:
        return "Hi  " +  name + "!"
    else:
        return "Strings Only"


@app.route('/repeat/<x>/<word>')
def repeat(x, word):
    if x.isdigit() and type(word) ==str:
        return word   *  int(x)

@app.route('/', defaults={'path':""})
@app.route('/<path:path>')
def catch_all(path):
    return 'Sorry! No response. Try Again!'


if __name__ =="__main__":
    app.run(debug=True)

 