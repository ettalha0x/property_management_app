# Overview
    The goal is to create a simple property management application that can handle properties of various sizes. The app should enable property managers to add new properties, manage tenants, and monitor rent payments.

# Properties Management API
    List All Properties (Read - List View)
        Endpoint: GET /properties/
        Description: Retrieves a list of all properties.

    Retrieve a Single Property (Read - Detail View)
        Endpoint: GET /properties/{id}/
        Description: Retrieves a specific property by its id.

    Create a New Property (Create)
        Endpoint: POST /properties/
        Description: Creates a new property with the data provided in the request body.

    Update an Existing Property (Update - PUT)
        Endpoint: PUT /properties/{id}/
        Description: Updates an entire property record by its id. The request must include all fields.

    Partially Update a Property (Update - PATCH)
        Endpoint: PATCH /properties/{id}/
        Description: Partially updates a property by its id. Only the fields provided in the request will be updated.

    Delete a Property (Delete)
        Endpoint: DELETE /properties/{id}/
        Description: Deletes the property with the specified id.


# Tenants Management API
    List All Tenant (Read - List View)
        Endpoint: GET /Tenants/
        Description: Retrieves a list of all Tenant.

    Retrieve a Single Tenant (Read - Detail View)
        Endpoint: GET /Tenants/{id}/
        Description: Retrieves a specific Tenant by its id.

    Create a New Tenant (Create)
        Endpoint: POST /Tenants/
        Description: Creates a new Tenant with the data provided in the request body.

    Update an Existing Tenant (Update - PUT)
        Endpoint: PUT /Tenants/{id}/
        Description: Updates an entire Tenant record by its id. The request must include all fields.

    Partially Update a Tenant (Update - PATCH)
        Endpoint: PATCH /Tenants/{id}/
        Description: Partially updates a Tenant by its id. Only the fields provided in the request will be updated.

    Delete a Tenant (Delete)
        Endpoint: DELETE /Tenants/{id}/
        Description: Deletes the Tenant with the specified id.


# Payments Management API
    List All Payments (Read - List View)
        Endpoint: GET /Payments/
        Description: Retrieves a list of all Tenant.

    Retrieve a Single Payment (Read - Detail View)
        Endpoint: GET /Payments/{id}/
        Description: Retrieves a specific Payment by its id.

    Create a New Payment (Create)
        Endpoint: POST /Payments/
        Description: Creates a new Payment with the data provided in the request body.

    Update an Existing Payment (Update - PUT)
        Endpoint: PUT /Payments/{id}/
        Description: Updates an entire Payment record by its id. The request must include all fields.

    Partially Update a Payment (Update - PATCH)
        Endpoint: PATCH /Payments/{id}/
        Description: Partially updates a Payment by its id. Only the fields provided in the request will be updated.

    Delete a Payment (Delete)
        Endpoint: DELETE /Payments/{id}/
        Description: Deletes the Payment with the specified id.