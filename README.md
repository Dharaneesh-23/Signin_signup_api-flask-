# Signin_signup_api-flask-

This Flask application provides API endpoints for user signup and sign-in functionalities with MySQL database integration. The project ensures secure communication for API endpoints and includes measures to hash user passwords before storing them.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [MySQL Database Setup](#mysql-database-setup)
- [Postman Test and Documentation](#postman-test-and-documentation)
- [Security Measures](#security-measures)
- [License](#license)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Dharaneesh-23/signin_signup_apis.git

2. **Navigate to the project directory:**

    ```bash
    cd signin_signup_apis

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt

## Usage

1. **Run the Flask application:**
   
   ```bash
   python app.py

3. **Access the API endpoints:**

   Open your web browser and go to http://localhost:5000.

## MySQL Database Setup

1. **Create a MySQL database:**
   Read the 'queries.txt' file complete setup of the database and the table.
   ![Table structure](https://github.com/Dharaneesh-23/Signin_signup_api-flask-/blob/main/images/database.png)
   
## Postman Test and Documentation

1. **Watch the video:**
   View the demonstration video in 'dharaneesh_invictusInterrn.mp4' to see the functionality of the APIs.

2. **API Documentation:**
   Detailed instructions on API usage can be found below:
   - Signup API Endpoint:
     * Endpoint: /signup
     * Method: POST
     * Input: JSON object with username, email, and password.
     * Example:
         {
          "username": "example_user",
          "email": "user@example.com",
          "password": "securepassword"
         }
   - Sign In API Endpoint:
     * Endpoint: /signin
     * Method: POST
     * Input: JSON object with username_email and password.
     * Example:
         {
          "username_email": "example_user",
          "password": "securepassword"
         }


## Security Measures

* User passwords are hashed using the SHA-256 algorithm before storing them in the database.

* API endpoints use secure communication over HTTPS.

## License
This project is licensed under the MIT License. Copyright © 2023 Dharaneesh-23.
