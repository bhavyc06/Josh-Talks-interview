# Josh-Talks-interview Task Management API
A Django + Django REST Framework application to manage tasks and assign them to multiple users.

Overview:
  This API provides endpoints to:

  1.Create tasks with a name, description, type, status, timestamps, etc.

  2.Assign tasks to one or more users.

  3.Retrieve tasks assigned to a specific user.

A custom User model is included with fields like mobile, and the admin interface allows easy management of users and tasks.

Features:
  1.Simple Data Model: A Task model with all required fields (name, description, created_at, etc.) and a User model with additional fields like email and mobile.

  2.Many-to-Many Relationship: A single task can be assigned to multiple users; each user can have multiple tasks.

  3.Django Admin Integration: Easily manage tasks and users from the admin dashboard.

  4.RESTful Endpoints: Clear, well-documented API calls for creating, assigning, and retrieving tasks.

Tech Stack:

  1.Language: Python 3.8+

  2.Framework: Django (5.1+) and Django REST Framework

  3.Database: SQLite (default) or any other supported database

  4.Version Control: Git


