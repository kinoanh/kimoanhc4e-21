#1.create a flask app
from flask import Flask, render_template

app = Flask(__name__)

#2. create routr
@app.route("/")
def homepage():
    return render_template("homepage.html", posts= ps, title="web introduction")
@app.route("/hello/<name>")
def hello(name):
    return "hello " + name
@app.route("/add/<int:a>/<int:b>")
def add(a,b):
    sum=a+b
    print(sum)
    return str(sum)
@app.route("/h1tag")
def h1tag():
    return"<h1>heading 1 - biggg</h1>"
@app.route("/posts/<int:i>")
def posts(i):
    if i<0 or i >=len(ps):
        return "not found"

    p=ps[i-1]
    return render_template("homepage.html", post=p)


#3. run app
print("")
if __name__ == "__main__":
    app.run(debug=True) #listening
