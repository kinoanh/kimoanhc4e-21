from flask import Flask , render_template
app=flask(__name__)
@app.route("/register")
def register():
    return render_template("frist.html")
if __name__ == "__main__":
    app.run(debug=True)
