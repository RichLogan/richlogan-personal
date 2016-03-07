from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect("http://uk.linkedin.com/in/rich-logan-778b1556")

@app.route('/webhook')
def spark_webhook():
    return "Spark"

if __name__ == "__main__":
    app.run()
