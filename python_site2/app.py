from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)
data = [{
   'name': 'Bobby'
}]


@app.route("/congrats")
def congrats():
   return "Congrats!"

@app.route("/")
def start():
   return render_template("app.html")

@app.route("/question", methods = ["POST"])
def question():
   if request.form.get("guess") and request.form.get.lower("guess") == "warzone": #not sure if i can place lower() there
      return redirect("/congrats")
   else:
      return redirect("/")

@app.route("/jsondata")
def jsondata():
   return jsonify(data)
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE
