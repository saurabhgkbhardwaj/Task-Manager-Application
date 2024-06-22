# Task Manager Application

## Overview

The Task Manager Application is a web-based platform designed to help users manage their tasks efficiently. It provides functionalities to create, update, and delete tasks, each with a title, description, and due date. The application is built using Django and Django REST Framework for the backend and utilizes HTML, CSS, and JavaScript for the frontend.

## Features

- **Create Task**: Add new tasks with a title, description, and due date.
- **Update Task**: Edit the details of existing tasks.
- **Delete Task**: Remove tasks from the list.
- **List Tasks**: View all tasks with their details.
- **Interactive UI**: Uses Bootstrap for a responsive and modern interface.

## Installation

### Prerequisites

- Python 3.8 or higher
- Django 3.2 or higher

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/task_manager.git
    cd task_manager
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip3 install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

5. Run the development server:

    ```bash
    python3 manage.py runserver
    ```

6. Open your browser and navigate to `http://127.0.0.1:8000`.

## Project Structure


*.*

*├── db.sqlite3*

*├── manage.py*

*├── readme.md*

*├── requirements.txt*

*├── task_manager*

*│ ├── asgi.py*

*│ ├── \_\_init\_\_.py*

*│ ├── \_\_pycache\_\_*

*│ │ ├── \_\_init\_\_.cpython-311.pyc*

*│ │ ├── settings.cpython-311.pyc*

*│ │ ├── urls.cpython-311.pyc*

*│ │ └── wsgi.cpython-311.pyc*

*│ ├── settings.py*

*│ ├── urls.py*

*│ └── wsgi.py*

*└── tasks*

* ├── admin.py*

* ├── apps.py*

* ├── forms.py*

* ├── \_\_init\_\_.py*

* ├── migrations*

* │ ├── 0001_initial.py*

* │ ├── \_\_init\_\_.py*

* │ └── \_\_pycache\_\_*

* │ ├── 0001_initial.cpython-311.pyc*

* │ └── \_\_init\_\_.cpython-311.pyc*

* ├── models.py*

* ├── \_\_pycache\_\_*

* │ ├── admin.cpython-311.pyc*

* │ ├── apps.cpython-311.pyc*

* │ ├── forms.cpython-311.pyc*

* │ ├── \_\_init\_\_.cpython-311.pyc*

* │ ├── models.cpython-311.pyc*

* │ ├── serializers.cpython-311.pyc*

* │ ├── urls.cpython-311.pyc*

* │ └── views.cpython-311.pyc*

* ├── serializers.py*

* ├── templates*

* │ ├── base.html*

* │ ├── create_task.html*

* │ ├── index.html*

* │ └── update_task.html*

* ├── tests.py*

* ├── urls.py*

* └── views.py*

*8 directories, 38 files*


### Key Files and Directories

- **manage.py**: A command-line utility that lets you interact with this Django project.

- **task_manager**: The main project directory.
  - **settings.py**: Contains settings/configuration for the project.
  - **urls.py**: The URL declarations for this Django project.
  - **wsgi.py**: An entry-point for WSGI-compatible web servers to serve your project.

- **tasks**: The application directory.
  - **models.py**: Defines the data models.
  - **views.py**: Contains the logic for handling requests and responses.
  - **forms.py**: Contains form classes for the application.
  - **serializers.py**: Contains the serializers for the REST API.
  - **urls.py**: URL declarations specific to the tasks application.
  - **templates**: Contains HTML templates for rendering pages.
    - **base.html**: The base template used by other templates.
    - **create_task.html**: Template for creating a new task.
    - **index.html**: Template for listing tasks.
    - **update_task.html**: Template for updating a task.

## API Endpoints

- **GET /api/tasks/**: Retrieve a list of tasks.
- **POST /api/tasks/**: Create a new task.
- **PUT /api/tasks/{id}/**: Update an existing task.
- **DELETE /api/tasks/{id}/**: Delete a task.

## Usage

- **Home Page**: Displays the list of tasks. You can edit or delete tasks from this page.
- **Add Task**: Navigate to the "Add Task" page to create a new task.
- **Edit Task**: Click on the "Edit" button next to a task to update its details.
- **Delete Task**: Click on the "Delete" button next to a task to remove it.



## Acknowledgements

This project was developed as a part of a task for PedalStart.
