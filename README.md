# Flask To-Do List Application

## Overview
This is a simple To-Do List application built using Flask, SQLite, and SQLAlchemy. It allows users to add, edit, delete, and view tasks. The application follows a CRUD (Create, Read, Update, Delete) structure and utilizes an HTML frontend with CSS for styling.

## Features
- Add new tasks
- View all tasks
- Edit existing tasks
- Delete tasks
- Persistent storage using SQLite
- Simple and clean UI

## Project Structure
```
.flask-todo/
│-- .venv/                # Virtual environment (optional)
│-- instance/
│   ├── database.db       # SQLite database
│-- static/
│   ├── style.css         # CSS for styling
│-- templates/
│   ├── base.html         # Base template
│   ├── index.html        # Homepage
│   ├── edit.html         # Edit task page
│   ├── testing.html      # Testing page
│   ├── UnstyledAndOriginalhtml.html  # Original HTML file
│-- main.py               # Main Flask application
│-- requirement.txt       # Project dependencies
│-- Flask Database for your project.md   # Project documentation
│-- Flask Database for your project.pdf  # Project documentation (PDF)
```

## Installation & Setup
### 1. Clone the Repository
```sh
git clone https://github.com/your-username/flask-todo.git
cd flask-todo
```

### 2. Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3. Install Dependencies
```sh
pip install -r requirement.txt
```

### 4. Initialize the Database
```sh
python
>>> from main import db
>>> db.create_all()
>>> exit()
```

### 5. Run the Application
```sh
python main.py
```

### 6. Open in Browser
Visit `http://127.0.0.1:5000/` to use the application.

## Routes
| Route            | Method | Description |
|-----------------|--------|-------------|
| `/`             | GET, POST | Home page, displays tasks, allows adding tasks |
| `/edit/<id>`    | GET, POST | Edit a task |
| `/delete/<id>`  | GET | Delete a task |

## Technologies Used
- Python (Flask)
- SQLite (Database)
- SQLAlchemy (ORM)
- HTML, CSS (Frontend)

## License
This project is open-source and available under the MIT License.

## Author
[Aman Kumar](https://github.com/SKDPROGRAMMER-AMANKUMAR)

