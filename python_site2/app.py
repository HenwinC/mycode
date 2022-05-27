from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
import json
app = Flask(__name__)

data = [{
   'name': 'Bobby',
   'class': 'pkm',
   'player_type': 'Run&Gun'
}]


@app.route("/congrats")
def congrats():
   return "Congrats!"

@app.route("/")
def start():
   return render_template("app.html")

@app.route("/question", methods = ["POST","GET"])
def question():
   if request.form.get("guess") and request.form.get("guess").lower() == "warzone": #not sure if i can place lower() there
      return redirect("/congrats")
   else:
      return redirect("/")

@app.route("/jsondata")
def jsondata():
   return json.dumps(data)
   
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2225) # runs the application
   # app.run(host="0.0.0.0", port=2225, debug=True) # DEBUG MODE
