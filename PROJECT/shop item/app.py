from flask import Flask,render_template,url_for,redirect,request,flash
from flask_mysqldb import MySQL

app=Flask(__name__)
#MYSQL CONNECTION
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="root"
app.config["MYSQL_DB"]="kalai"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(app)


#Loading Home Page
@app.route("/")
def home():
    con=mysql.connection.cursor()
    sql="SELECT * FROM kk"
    con.execute(sql)
    res=con.fetchall()
    return render_template("home.html",datas=res)
    
#New User
@app.route("/addproducts",methods=['GET','POST'])
def addproducts():
    if request.method=='POST':
        name=request.form['name']
        prand=request.form['prand']
        price=request.form['price']
        con=mysql.connection.cursor()
        sql="insert into kk(products,prand,price) value (%s,%s,%s)"
        con.execute(sql,[name,prand,price])
        mysql.connection.commit()
        con.close()
        flash('product Added')        
        return redirect(url_for("home"))
    return render_template("addproducts.html")
#update User
@app.route("/editUser/<string:id>",methods=['GET','POST'])

def editUser(id):
    con=mysql.connection.cursor()
    if request.method=='POST':
        products=request.form['products']
        prand=request.form['prand']
        price=request.form['price']
        sql="update kk set products=%s,prand=%s,price=%s where ID=%s"
        con.execute(sql,[products,prand,price,id])
        mysql.connection.commit()
        con.close()
        flash('User Detail Updated')
        return redirect(url_for("home"))
    con=mysql.connection.cursor()
        
    sql="select * from kk where ID=%s"
    con.execute(sql,[id])
    res=con.fetchone()
    return render_template("editUser.html",datas=res)
#Delete User
@app.route("/deleteUser/<string:id>",methods=['GET','POST'])
def deleteUser(id):
    con=mysql.connection.cursor()
    sql="delete from kk where ID=%s"
    con.execute(sql,id)
    mysql.connection.commit()
    con.close()
    flash('User Details Deleted')
    return redirect(url_for("home"))

if(__name__=='__main__'):
    app.secret_key="abc123"
    app.run(debug=True)
