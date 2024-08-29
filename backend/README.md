# Users Management API
## Register a New User
    Endpoint: POST /users/register/
    Description: Creates a new user with the provided username, email, and password.
    Request Body:
        {
          "username": "your_username",
          "email": "your_email@example.com",
          "password": "your_password",
          "password2": "your_password"
        }
## Login
    Endpoint: POST /users/login/
    Description: Authenticates the user and provides JWT tokens.
    Request Body:
    {
      "username": "your_username",
      "password": "your_password"
    }
## Logout
    Endpoint: POST /users/logout/
    Description: Logs out the user by blacklisting the refresh token.
    Request Body:
    {
      "refresh": "your_refresh_token"
    }
## Authentication:
    For all secured API endpoints, include the access token in the Authorization header as a bearer token:
    Authorization: Bearer <your_access_token>
# Properties Management API
## List All Properties (Read - List View)
    Endpoint: GET /properties/
    Description: Retrieves a list of all properties.
## Retrieve a Single Property (Read - Detail View)
    Endpoint: GET /properties/{id}/
    Description: Retrieves a specific property by its id.
## Create a New Property (Create)
    Endpoint: POST /properties/
    Description: Creates a new property with the data provided in the request body.
    Request Body:
    {
        "name": "",
        "address": "",
        "property_type": "",
        "number_of_units": "",
        "rental_cost": ""
    }
## Update an Existing Property (Update - PUT)
    Endpoint: PUT /properties/{id}/
    Description: Updates an entire property record by its id. The request must include all fields.
    Request Body:
    {
        "name": "",
        "address": "",
        "property_type": "",
        "number_of_units": "",
        "rental_cost": ""
    }
## Partially Update a Property (Update - PATCH)
    Endpoint: PATCH /properties/{id}/
    Description: Partially updates a property by its id. Only the fields provided in the request will be updated.
    Request Body:
    {
        "rental_cost": ""
    }
## Delete a Property (Delete)
    Endpoint: DELETE /properties/{id}/
    Description: Deletes the property with the specified id.
# Tenants Management API
## List All Tenants (Read - List View)
    Endpoint: GET /tenants/
    Description: Retrieves a list of all tenants.
## Retrieve a Single Tenant (Read - Detail View)
    Endpoint: GET /tenants/{id}/
    Description: Retrieves a specific tenant by its id.
## Create a New Tenant (Create)
    Endpoint: POST /tenants/
    Description: Creates a new tenant with the data provided in the request body.
    Request Body:
    {
        "name": "",
        "contact_details": "",
        "property": "",
        "section_occupied": ""
    }
## Update an Existing Tenant (Update - PUT)
    Endpoint: PUT /tenants/{id}/
    Description: Updates an entire tenant record by its id. The request must include all fields.
    Request Body:
    {
        "name": "",
        "contact_details": "",
        "property": "",
        "section_occupied": ""
    }
## Partially Update a Tenant (Update - PATCH)
    Endpoint: PATCH /tenants/{id}/
    Description: Partially updates a tenant by its id. Only the fields provided in the request will be updated.
    Request Body:
    {
        "section_occupied": ""
    }
## Delete a Tenant (Delete)
    Endpoint: DELETE /tenants/{id}/
    Description: Deletes the tenant with the specified id.
# Payments Management API
## List All Payments (Read - List View)
    Endpoint: GET /payments/
    Description: Retrieves a list of all payments.
## Retrieve a Single Payment (Read - Detail View)
    Endpoint: GET /payments/{id}/
    Description: Retrieves a specific payment by its id.
## Create a New Payment (Create)
    Endpoint: POST /payments/
    Description: Creates a new payment with the data provided in the request body.
    Request Body:
    {
        "tenant": "",
        "amount": "",
        "date_paid": "",
        "settled": ""
    }
## Update an Existing Payment (Update - PUT)
    Endpoint: PUT /payments/{id}/
    Description: Updates an entire payment record by its id. The request must include all fields.
    Request Body:
    {
        "tenant": "",
        "amount": "",
        "date_paid": "",
        "settled": ""
    }
## Partially Update a Payment (Update - PATCH)
    Endpoint: PATCH /payments/{id}/
    Description: Partially updates a payment by its id. Only the fields provided in the request will be updated.
    Request Body:
    {
        "amount": ""
    }
## Delete a Payment (Delete)
    Endpoint: DELETE /payments/{id}/
    Description: Deletes the payment with the specified id.
# Notes
Ensure that the access token obtained during the login process is included in the Authorization header as a Bearer token for all protected endpoints.
