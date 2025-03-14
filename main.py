# Import
from flask import Flask, render_template, redirect ,request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# My app
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

# Data Class ~ Row of data
class MyTask(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String(100),nullable=False)
    complete = db.Column(db.Integer,default=0)
    created = db.Column(db.DateTime,default=datetime.utcnow)
    
    def __repr__(self):
        return f"Task {self.id}"

# # Configure Flask to compile SCSS files from 'static' to 'static/css'
# Scss(app, static_dir="static", asset_dir="static")

# Routes to Webpage
# Home page
@app.route("/",methods=["POST","GET"])
def index():
    # Add a Task
    if request.method == "POST":
        current_task = request.form['content']
        new_task = MyTask(content=current_task)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print(f"Error: {e}")
            return f"Error: {e}"    
    
    # See all current tasks
    else:
        tasks = MyTask.query.order_by(MyTask.created).all() # This .all() converts the query object into a list.
        return render_template("index.html",tasks=tasks)
    
    
# Delete an Item
@app.route("/delete/<int:id>")
def delete(id:int):
    delete_task = MyTask.query.get_or_404(id)  # ✅ Call the method with id
    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        return f"Error:{e}"
    

# Edit an item
@app.route("/edit/<int:id>",methods=["GET","POST"])
def edit(id:int):
    task = MyTask.query.get_or_404(id)
    if request.method == "POST":
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f"Error:{e}"
    else:
        return render_template("edit.html",task=task)
    
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True) 