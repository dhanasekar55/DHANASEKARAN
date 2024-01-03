from flask import Flask,render_template,url_for,redirect,request,flash
from flask_mysqldb import MySQL

app=Flask(__name__)
#MYSQL CONNECTION
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="root"
app.config["MYSQL_DB"]="voter"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(app)


#Loading Home Page
@app.route("/")
def home():
    con=mysql.connection.cursor()
    sql="SELECT * FROM dhana"
    con.execute(sql)
    res=con.fetchall()
    return render_template("home.html",datas=res)
    
#New User
@app.route("/addvoter",methods=['GET','POST'])
def addvoter():
    if request.method=='POST':
        ID=request.form['ID']
        name=request.form['name']
        voter=request.form['fav_language']
        con=mysql.connection.cursor()
        sql="insert into dhana(ID,name,voter) value (%s,%s,%s)"
        con.execute(sql,[ID,name,voter])
        mysql.connection.commit()
        con.close()
        flash('User Details Added')        
        return redirect(url_for("home"))
    return render_template("addvoter.html")

# Details
@app.route("/details",methods=['GET','POST'])
def details():
    if request.method=='POST':
        ID=request.form['ID']
        name=request.form['name']
        voter=request.form['fav_language']
        con=mysql.connection.cursor()
        sql="insert into dhana(ID,name,voter) value (%s,%s,%s)"
        con.execute(sql,[ID,name,voter])
        mysql.connection.commit()
        con.close()
        flash('User Details view')        
        return redirect(url_for("home"))
    return render_template("details.html")


if(__name__=='__main__'):
    app.secret_key="abc123"
    app.run(debug=True)

