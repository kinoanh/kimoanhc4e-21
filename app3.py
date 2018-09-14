from flask import Flask

app4 = Flask(__name__)

@app4.route("/user/<username>")
def Name(username):
    Users = {'huy':{'name':'Nguyen Quang Huy','age':29},'tuananh':{'name':'Huynh Tuan Anh','age':22}}

    if username == 'huy':
        return(str(Users['huy']))
    elif username == 'tuananh':
        return(str(Users['tuananh']))
    else:
        return('Not found')
   


print('Running app')
if __name__ == "__main__":
    app4.run(debug=True)