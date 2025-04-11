from pydoc import render_doc
from zoneinfo import reset_tzpath
from config import Config

from flask import Flask ,jsonify,request,render_template,redirect,url_for
from config import Config
from models import db

app=Flask(__name__)
app.config.from_object(Config)
db.ini_app(app)

with app.app_context():
    db.create_all()
# table is created

@app.route("/home",methods=["GET"])
def home():
    return {"msg":"this is my home page"}

@app.route("/pathparm/<int:id>",methods=["GET"])
def path_parm(id):
    return jsonify(msg=f"the path parm is:{id}")


@app.route("/qureyparam",methods=["GET"])
def qure_parm_funct():
    # name=request.args.get("name")
    # age=request.args.get("age")
    # return jsonify(msg=f"qurey parmas are {name},{age}")
    # name=request.args.getlist("name")
    # return jsonify(msg=f"qurey parmas are {name}")
# when we dont know the args or query parametors we use to_dict()
#     data=request.args.to_dict()
#     print(data,type(data))
#     return data
# when we have a mutiple names at that time we use flat=False
        data=request.args.to_dict(flat=False)
        print(data,type(data))
        return data

@app.route("/insertdata",methods=["POST"])
def insert_func():
    data=request.get_json(silent=True)
    # data=request.data
    print(data,type(data))
    # return "from post"
    return data

@app.route("/put_demo/<id>",methods=["PUT"])
def put_func():
    data=request.get_json(silent=True)
    return jsonify(msg=f"{data},{id}")

@app.route("/rawhtml",methods=["GET"])
def raw_func():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>RAW HTML</title>
</head>
<body>
    <hl>from raw html</hl>
</body>
</html>
"""

@app.route("/templet_html",methods=["GET"])
def temp_html_func():
    return render_template("demo.html")

@app.route("/redirect",methods=["GET"])
def redirect_func():
    return redirect(url_for("home"))


@app.route("/formdata",methods=["POST"])
def form_data_func():
    # name=request.form.get("name")
    # age=request.form.get("age")
    # return jsonify(msg=f'qurey parms are {name},{age}')
    # name=request.form.getlist("name")
    # return jsonify(mge=f" from form data {name}")
    data=request.form.to_dict(flat=False)
    print(data,type(data))
    return data
if __name__=="__main__":
    app.run(debug=True,port=5000)