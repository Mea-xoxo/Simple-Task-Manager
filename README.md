# Simple Task Manager

A task management web application built with Django that displays tasks.

## Features
- User registration and login
- Create, edit and delete tasks
- Mark tasks as complete
- Add due dates to tasks
- Priority levels (Low, Medium, High)
- Overdue task indicator
- Custom CSS styling

## Technologies Used
- Python
- Django
- SQLite
- HTML/CSS

## How to Run Locally

1. Clone the repo:
git clone https://github.com/Mea-xoxo/Simple-Task-Manager.git

2. Navigate into the folder:
cd Simple-Task-Manager

3. Create and activate virtual environment:
python -m venv venv
venv\Scripts\activate

4. Install dependencies:
pip install -r requirements.txt

5. Run migrations:
python manage.py migrate

6. Start the server:
python manage.py runserver

7. Visit http://127.0.0.1:8000/
