# Library Management System API

This project is a **Library Management System API** developed using **Django** and **Django REST Framework (DRF)**. It serves as the backend for managing library resources, allowing users to interact with the system by borrowing, returning, and viewing books.

---

## Features

### 1. **Books Management (CRUD)**
- Create, read, update, and delete books.
- Attributes include:
  - Title
  - Author
  - ISBN (unique)
  - Published Date
  - Number of Copies Available
- Validation ensures unique ISBN numbers.

### 2. **Users Management (CRUD)**
- Create, read, update, and delete library users.
- User attributes include:
  - Username (unique)
  - Email
  - Date of Membership
  - Active Status

### 3. **Book Check-Out and Return**
- Users can check out books if copies are available.
- Only one copy of a book can be checked out per user at a time.
- Automatically reduces available copies upon check-out.
- Allows users to return books, increasing available copies.
- Logs the date of check-out and return.

### 4. **View Available Books**
- Lists all books with an option to filter by availability.
- Search functionality for books by:
  - Title
  - Author
  - ISBN


### Prerequisites
- Python 3.9+
- Django 4.x
- Django REST Framework (DRF)

API Endpoints
Books Endpoints
GET /books/ - List all books.
POST /books/ - Add a new book.
GET /books/<id>/ - Retrieve a specific book.
PUT /books/<id>/ - Update a specific book.
DELETE /books/<id>/ - Delete a specific book.
Users Endpoints
GET /users/ - List all users.
POST /users/ - Add a new user.
GET /users/<id>/ - Retrieve a specific user.
PUT /users/<id>/ - Update a specific user.
DELETE /users/<id>/ - Delete a specific user.
Transactions Endpoints
POST /transactions/checkout/ - Check out a book.
POST /transactions/return/ - Return a book.