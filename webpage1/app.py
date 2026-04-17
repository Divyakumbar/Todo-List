from flask import Flask,render_template,request
import sqlite3
app=Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/create",methods=["GET","POST"])
def create():
    if request.method=="POST":
        name=request.form['name']
        task=request.form['task']
        conn=sqlite3.connect("todo.db")
        cursor=conn.cursor()
        cursor.execute("INSERT INTO task(name,list) VALUES(?,?)",(name,task))
        conn.commit()
        conn.close()
        
    return render_template("create.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/task",methods=["GET","POST"])
def task():
    conn=sqlite3.connect("todo.db")
    cursor=conn.cursor()

    if request.method=="POST":
     task_id=request.form.get("ID")
     cursor.execute("DELETE  FROM task WHERE id=?",(task_id,))
     conn.commit()
     
    cursor.execute("SELECT * FROM task")
    all_data=cursor.fetchall()
    conn.close()
    return render_template("task.html",tasks=all_data)

@app.route("/completed")
def completed():
    conn=sqlite3.connect("todo.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM task")
    all_data=cursor.fetchall()
    conn.close()
    return render_template("completed.html",tasks=all_data)

@app.route("/",methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form['username']
        password=request.form['password']
        conn=sqlite3.connect("todo.db")
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM user WHERE username=? AND password=?",(username,password))
        data=cursor.fetchone()
        if data:
            return render_template("home.html")
        else:
            return "Invalid Username and Password"
        
    return render_template("login.html")

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
        username=request.form['username']
        email=request.form['email']
        number=request.form['number']
        password=request.form['password']
        conn=sqlite3.connect("todo.db")
        cursor=conn.cursor()
        cursor.execute("INSERT INTO user (username,email,number,password) VALUES(?,?,?,?) ",
        (username,email,number,password))
        conn.commit()
        conn.close()
    return render_template("register.html")

if __name__=="__main__":
    app.run(debug=True)


    
