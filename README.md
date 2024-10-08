# File Sharing System API

## Overview

This project is a secure file-sharing system that enables two types of users: **Ops Users** and **Client Users**. The Ops Users can login, upload files, while Client Users can sign up, log in, and download files. The API is built using Django and provides a RESTful interface for interaction.

### User Roles

- **Ops User:** 
  - Username: `rishabhadmin`
  - Password: `opspass` 
  - Role: `ops`  
  

  Note: Ops Users cannot sign up through the API.

## Testing

Test cases are included in the `test.py` file. You can run the tests using the following command:
```python
python3 manage.py test
```

## How do you plan on deploying this to the production environment?

## 1. Prerequisites
- Python 3.10+
- Django
- Gunicorn (for serving the app)
- Nginx (reverse proxy)
- PostgreSQL/MongoDB (database)
- Git (version control)
- SSL/TLS Certificate (for HTTPS)
- Cloud provider (AWS, DigitalOcean, Heroku, etc.)

---

## 2. Deployment Steps

1. **Cloud Infrastructure**: Set up a virtual machine (AWS EC2, DigitalOcean Droplet, etc.) and install required packages (Python, pip, PostgreSQL/MongoDB, Nginx).

2. **Clone and Configure**: Clone the repository, set up a virtual environment, and install dependencies. Configure environment variables, database settings, and static file paths.

3. **Database Migration**: Run Django migrations to create the necessary database schema and ensure your database is properly configured.

4. **Gunicorn Setup**: Install and configure Gunicorn as the WSGI server for running the Django application in production.

5. **Nginx Configuration**: Set up Nginx as a reverse proxy to serve the Django app via Gunicorn. Ensure SSL is configured for secure HTTPS access.

6. **System Monitoring**: Enable systemd services for Gunicorn and monitor the application. Set up server firewalls and logging for production.


### Features

- User authentication (sign up and login).
- File upload by Ops Users.
- File download and listing by Client Users.
- Secure encrypted URLs for file access.

## API Endpoints

### 1. Signup API

- **Endpoint:** `POST /api/signup/`
- **Name:** `signup`
- **Description:** Allows a new Client User to register an account.

**Request Body:**
- `username`: The desired username of the user.
- `email`: The user's email address.
- `password`: The user's password.

**Response:**
- **Success:** Confirmation message indicating successful registration.
- **Error:** Description of the validation error.

### 2. Login API

- **Endpoint:** `POST /api/login/`
- **Name:** `login`
- **Description:** Authenticates a user and provides access tokens.

**Request Body:**
- `username`: The user's username.
- `password`: The user's password.

**Response:**
- **Success:** JWT access token and refresh token for authenticated requests.
- **Error:** Description of the authentication error.

### 3. Upload File API

- **Endpoint:** `POST /api/upload-file/`
- **Name:** `upload-file`
- **Description:** Allows an authenticated Ops User to upload a file.

**Request Body:**
- `file`: The file to be uploaded (supported formats: .pptx, .docx, .xlsx).

**Headers:**
- `Authorization`: Bearer token obtained from the login endpoint.

**Response:**
- **Success:** Unique identifier for the uploaded file and confirmation message.
- **Error:** Description of the access error.

### 4. Download File API

- **Endpoint:** `GET /api/download-file/<str:file_id>/`
- **Name:** `download-file`
- **Description:** Allows a Client User to download a file using its unique identifier.

**Path Parameters:**
- `file_id`: Unique identifier for the file to be downloaded.

**Headers:**
- `Authorization`: Bearer token obtained from the login endpoint.

**Response:**
- **Success:** Returns the file content for download.
- **Error:** Description indicating the file was not found or access error.

### 5. List Files API

- **Endpoint:** `GET /api/list-files/`
- **Name:** `list-files`
- **Description:** Allows an authenticated Client User to list all uploaded files.

**Headers:**
- `Authorization`: Bearer token obtained from the login endpoint.

**Response:**
- **Success:** Array of file objects with details.
- **Error:** Description of the access error.

## Installation and Setup

1. Clone the repository.
2. Install the required dependencies.
3. Configure your database settings.
4. Run database migrations.
5. Create a superuser for the Ops role.

## Usage

- Start the Django server.
- Access the API endpoints as documented above.





