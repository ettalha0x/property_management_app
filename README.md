# Property Management App

The goal of this project is to create a simple property management application that can handle properties of various sizes. The app enables property managers to add new properties, manage tenants, and monitor rent payments.

## Features

- Add Property: Manage property details including name, address, type, number of units, and rental costs.
- Tenant Management: Add, modify, and remove tenants with their names, contact details, and the section they occupy.
- Rental Payments Monitoring: Track rent payments, including payment dates and settlement status.

## Technologies Used

- Django
- Django REST Framework
- SQLite (or any other relational database)
- JWT Authentication

## Cloning the Project

To clone this project, run the following command:

```bash
git clone https://github.com/ettalha0x/property_management_app.git
cd property-management-app
```
## Building and Running the Docker Image
Build the Docker Image:

```bash
docker build -t property-management-app .
```
Run the Docker Container:

```bash
docker run -d -p 8000:8000 property-management-app
```
Open your web browser and go to http://localhost:8000 to access the application.

## Testing the API
You can test the API using tools like Postman or cURL. Refer to the [backend/README.md](https://github.com/ettalha0x/property_management_app/blob/main/README.md) file for a complete guide on the available API endpoints, their usage,   and how to authenticate using JWT tokens.

## API Endpoints Guide
The API supports CRUD operations for properties, tenants, and rental payments. Below are the base endpoints:

Properties: /properties/
Tenants: /tenants/
Payments: /payments/
Users: /users/
Please refer to the backend/README.md file for detailed documentation on the API endpoints.
