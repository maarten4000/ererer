from flask import Flask,render_template,request




app = Flask(__name__)




@app.route("/",methods=["POST","GET"])
def home():
    if request.method == "POST":
        username = request.form["name"]
        pw = request.form["pw"]
        print(pw,username)





    return render_template("home.html")






if __name__ == "__main__":
    app.run(debug=True)
