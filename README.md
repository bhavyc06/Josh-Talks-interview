# Josh-Talks-interview
Table of Contents
Overview

Features

Tech Stack

Requirements

Project Structure

Setup Instructions

API Endpoints

Example Usage via Postman

Testing & Validation

Contributing

License

Overview
This Task Management API provides a simple way to:

Create tasks with basic details (name, description).

Assign tasks to one or multiple users.

Fetch tasks assigned to a specific user.

It’s built using Django and Django REST Framework, following best practices for maintainability and clarity.

Features
Create a New Task

Capture name, description, and optional fields like task type and status.

Assign a Task to Users

Use a single API call to assign an existing task to multiple users simultaneously.

List Tasks for a Given User

Return all tasks that a specific user is assigned to.

Custom User Model

Includes fields like name, email, mobile, plus built-in username/password.

Admin Panel

Manage users and tasks in a friendly web interface.

Tech Stack
Language: Python 3.8+

Framework: Django (5.1+) & Django REST Framework

Database: SQLite (by default)

Others:

Virtual environment recommended (venv)

Git for version control

Requirements
Python 3.8+

Pip (Python package manager)

Django 5.1+

Django REST Framework

(Optional) Git for version control

