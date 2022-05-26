# #!/usr/bin/python3
# """Alta3 APIs and HTML"""

# from flask import Flask
# from flask import redirect
# from flask import request
# from flask import render_template

# app = Flask(__name__)

# @app.route("/success")
# def success(anwser):
#     return f"Very nice!"


# @app.route("/")
# def start():
#     return render_template("app.html")

# @app.route("/riddle", methods = ["POST"])
# def riddle():
#     if request.form.get("nm") and request.form.get("nm") == "eggs":
#         return redirect("success", anwser)
#     else:
#         redirect("/")
        



# if __name__ == "__main__":
#    app.run(host="0.0.0.0", port=2224) 
#!/usr/bin/python3

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template

app = Flask(__name__)

html= """<style>
body {
  background-color: black;
  text-align: center;
  color: white;
  font-family: Arial, Helvetica, sans-serif;
}
</style>
</head>
<body>

<h1>TRIVIA TIME</h1>
<p>What is the meaning of life, the universe, and everything?</p>
<img src="https://stevetobak.com/wp-content/uploads/2021/02/dont-panic.png" alt="Avatar" style="width:200px">

    <form action = "/login" method = "POST">
        <p><input type = "text" name = "nm"></p>
        <p><input type = "submit" value = "submit"></p>
    </form>

</body>
</html>"""

@app.route("/correct")
def success():
    return f"That is correct!"

@app.route("/")
def start():
    return render_template("app.html")

@app.route("/login", methods = ["POST"])
def login():
        if request.form.get("nm") and request.form.get("nm") == "42":
                return redirect("/correct")
        else:
            return redirect("/")


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application