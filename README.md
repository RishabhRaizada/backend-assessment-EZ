Overview
This project is a secure file-sharing system that enables two types of users: Ops Users and Client Users. The Ops Users can login, upload files, while Client Users can sign up, log in, and download files. The API is built using Django and provides a RESTful interface for interaction.

User Roles
Ops User:

Username: rishabhadmin

Email: user@example.com

Role: ops

Password: opspass 

Note: Ops Users cannot sign up through the API.

Features
User authentication (sign up and login).
File upload by Ops Users.
File download and listing by Client Users.
Secure encrypted URLs for file access.
API Endpoints
1. Signup API
Endpoint: POST /api/signup/
Name: signup
Description: Allows a new Client User to register an account.
Request Body:

json
Copy code
{
  "username": "your_username",
  "email": "your_email@example.com",
  "password": "your_password"
}
Response:

Success (201 Created):
json
Copy code
{
  "message": "User created successfully."
}
Error (400 Bad Request):
json
Copy code
{
  "error": "Validation error description."
}
2. Login API
Endpoint: POST /api/login/
Name: login
Description: Authenticates a user and provides access tokens.
Request Body:

json
Copy code
{
  "username": "your_username",
  "password": "your_password"
}
Response:

Success (200 OK):
json
Copy code
{
  "access_token": "your_access_token",
  "refresh_token": "your_refresh_token"
}
Error (401 Unauthorized):
json
Copy code
{
  "error": "Authentication error description."
}
3. Upload File API
Endpoint: POST /api/upload-file/
Name: upload-file
Description: Allows an authenticated Ops User to upload a file.
Request Body:

file (file): The file to be uploaded (supported formats: .pptx, .docx, .xlsx).
Headers:

Authorization: Bearer token obtained from the login endpoint.
Response:

Success (201 Created):
json
Copy code
{
  "file_id": "unique_file_id",
  "message": "File uploaded successfully."
}
Error (403 Forbidden):
json
Copy code
{
  "error": "Access denied."
}
4. Download File API
Endpoint: GET /api/download-file/<str:file_id>/
Name: download-file
Description: Allows a Client User to download a file using its unique identifier.
Path Parameters:

file_id (string): Unique identifier for the file to be downloaded.
Headers:

Authorization: Bearer token obtained from the login endpoint.
Response:

Success (200 OK): Returns the file content for download.
Error (404 Not Found):
json
Copy code
{
  "error": "File not found."
}
Error (403 Forbidden):
json
Copy code
{
  "error": "Access denied."
}
5. List Files API
Endpoint: GET /api/list-files/
Name: list-files
Description: Allows an authenticated Client User to list all uploaded files.
Headers:

Authorization: Bearer token obtained from the login endpoint.
Response:

Success (200 OK):
json
Copy code
{
  "files": [
    {
      "file_id": "unique_file_id",
      "filename": "example_file.docx",
      "uploaded_at": "2024-09-30T12:34:56Z"
    }
  ]
}
Error (403 Forbidden):
json
Copy code
{
  "error": "Access denied."
}
Installation and Setup
Clone the repository.
Install the required dependencies using:
bash
Copy code
pip install -r requirements.txt
Configure your database settings in settings.py.
Run database migrations:
bash
Copy code
python manage.py migrate
Create a superuser for the Ops role:
bash
Copy code
python manage.py createsuperuser
Usage
Start the Django server:
bash
Copy code
python manage.py runserver
Access the API endpoints as documented above.
