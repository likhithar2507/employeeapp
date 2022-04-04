from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def welcome():
    return "employee data"

@app.route('/add')
def add():
    return render_template("add.html")


@app.route('/search')
def search():
    return render_template("search.html")


@app.route('/update')
def Update():
    return render_template("update.html")


@app.route('/delete')
def delete():
    return render_template ("delete.html")


if __name__ == "__main__":
    app.run()
