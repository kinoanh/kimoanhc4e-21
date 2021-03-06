
from flask import Flask, render_template, request
import mlab
from user import User
from string import punctuation

app = Flask(__name__)
mlab.connect()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('test.html')
    elif request.method == 'POST':
    
        form = request.form
        n = form['name']
        e = form['email']
        i= form['id']
        p= form['pass']
    
        if '@' not in e or '.' not in e:
            return 'Invalid Email adress'
        if len(p) < 6:
            return 'Password must be longer than 6 chars'

        new_user = User(name=n, email=e, id=c, pass=p)
        new_user.save()
        return 'OK'

if __name__ == '__main__':
    app.run(debug=True)