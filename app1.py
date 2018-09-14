from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def homepage():
    return "<h1><a href = '/about-me'> Exercise </a></h1>"

@app.route('/about-me')
def about_me():
    return "<h1>họ tên : vũ thị kim oanh</h1>,<h1>là học sinh c4e21</h1>"

@app.route('/school')
def school_redirect():
    return redirect('http://techkids.vn', code = 302)

if __name__ == "__main__":
    app.run(debug = True)