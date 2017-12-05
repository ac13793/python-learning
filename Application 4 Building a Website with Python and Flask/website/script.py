from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    # home.html has to be present in templates folder
    return render_template("home.html")

@app.route('/about')
def about():
    # return "About page content goes here!!"
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)