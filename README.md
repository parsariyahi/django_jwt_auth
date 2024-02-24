# Django JWT Authentication

## Description
This repository contains a Django application that demonstrates how to implement JSON Web Token (JWT) authentication in a Django project. JWT authentication provides a secure and stateless way to authenticate users in web applications.

## Features
- User registration and authentication using JWT tokens.
- Token-based authentication for protected routes.
- Customizable token expiration time.
- Integration with Django's built-in user model.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/parsariyahi/django_jwt_auth.git
   ```

2. Navigate to the project directory:
   ```
   cd django_jwt_auth
   ```

3. Install dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage

1. Obtain a JWT token:
   ```
   POST /api/auth/token/
   ```
   Provide the username and password in the request body to obtain a JWT token.

3. Access protected routes:
   ```
   GET /api/auth/
   ```
   Include the JWT token in the Authorization header with the format: `Bearer <token>`.

4. Refresh JWT token:
   ```
   POST /api/auth/token/refresh/
   ```
   Provide the refresh token in the request body to obtain a new JWT token.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
