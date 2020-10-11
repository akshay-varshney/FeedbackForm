from flask import url_for, render_template,request,Flask,redirect,session
from flask_mysqldb import MySQL
import MySQLdb

app=Flask(__name__)
app.config['DEBUG']=True
app.secret_key='5791628bb0b13ce0c676dfde280ba245'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'feedback'

mysql = MySQL(app)

@app.route('/home/',methods=['GET','POST'])
def home():
    msg=''
    if request.method=="POST":
        customername=request.form['customername']
        language=request.form['language']
        rating=request.form['rating']
        comment=request.form['comment']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        result="INSERT INTO feedform VALUES(%s,%s,%s,%s)"
        values=(customername,language,rating,comment)
        cursor.execute(result,values)
        mysql.connection.commit()
        messages=customername
        session['messages'] = messages
        return redirect(url_for('thankyou',messages=messages))
    return render_template('home.html',msg=msg)

@app.route('/thankyou/')
def thankyou():
    msg=''
    messages = request.args['messages']  # counterpart for url_for()
    messages = session['messages']  
    return render_template('index.html',msg=messages)

    
if __name__=="__main__":
    app.run()

