from flask import Flask, render_template
app = Flask(__name__, static_folder='')
@app.route("/")
def handle(): return render_template("index.html")
if __name__ == "__main__": app.run(port="8765", debug=False)