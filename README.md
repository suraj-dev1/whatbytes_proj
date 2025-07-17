🏥 WhatBytes Healthcare Backend API
This project is a Django-based REST API backend built for managing healthcare-related data, created as part of the Backend Developer Internship assignment for WhatBytes.

It includes JWT-based user authentication, doctor-patient mappings, and RESTful endpoints to manage the data with full CRUD operations.

🔧 Tech Stack
Backend Framework: Django 4.x

API Layer: Django REST Framework (DRF)

Authentication: JWT ( Web Tokens)

Database: SQLite (for testing, can be switched to PostgreSQL)

Language: Python 3.x

  Setup Instructions
Clone the Repository




git clone https://github.com/suraj-dev1/whatbytes_proj.git
cd whatbytes_proj
Create & Activate Virtual Environment




python -m venv env
source env/bin/activate    # On Windows: env\Scripts\activate
Install Dependencies




pip install -r requirements.txt
Apply Migrations




python manage.py makemigrations
python manage.py migrate
Create Superuser (Optional for Admin Panel)




python manage.py createsuperuser
Run the Development Server




python manage.py runserver
Access the API at: http://127.0.0.1:8000/api/

 Authentication – JWT
Use the following endpoints to obtain and refresh tokens:

POST /api/token/ – Get access and refresh token

POST /api/token/refresh/ – Refresh the access token

Sample Payload:




{
  "username": "yourusername",
  "password": "yourpassword"
}
 API Endpoints Overview
 Registration & Login
POST /api/register/ – Register a new user (doctor or patient)

POST /api/token/ – Login and receive JWT tokens

 Mappings (Doctor ↔ Patient)
GET /api/mappings/ – List all mappings

POST /api/mappings/ – Create new mapping

GET /api/mappings/<id>/ – Retrieve specific mapping

PUT /api/mappings/<id>/ – Fully update a mapping

PATCH /api/mappings/<id>/ – Partially update a mapping

DELETE /api/mappings/<id>/ – Delete a mapping

 Filtered Mappings
GET /api/mappings/patient/ – View all patient-specific mappings (custom endpoint)

 Notes
Only authenticated users can access the endpoints.

Users are classified by a role field (doctor or patient).

Admin panel is available at /admin/ if superuser is created.

 Developer Info
Developed by: Suraj S
GitHub: https://github.com/suraj-dev1
Project Repo: https://github.com/suraj-dev1/whatbytes_proj

 Status
 User Registration & Login

 JWT Authentication

 Doctor-Patient Mapping CRUD

 Custom Filter API

 Fully Tested via Postman

 Summary
This project demonstrates the ability to:

Build secure, token-authenticated APIs

Work with Django REST Framework efficiently

Apply clean REST principles in a healthcare setting

Write modular, testable, and maintainable backend logic

Made with 💻 and ☕ by Suraj for WhatBytes Internship Assignment – 2025