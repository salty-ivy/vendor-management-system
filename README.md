# Vendor-Management-System

The Vendor Management System is a web application developed using Django and Django REST Framework. It is designed to handle vendor profiles, track purchase orders, and calculate vendor performance metrics. This documentation provides a comprehensive guide for both technical and non-technical users on how to use and navigate the system.

*Login Credentials:*

```
username: admin
password: admin
```


## Features

1. **Vendor Management:**
   - Create, update, and delete vendors.

2. **Purchase Order Management:**
   - Create, update, and delete purchase orders.

3. **Vendor Performance Metrics:**
   - Calculate vendor performance metrics.


## Getting Started

### Virtual Environment

It is recommended to use a virtual environment to run this project. Follow the steps below:

1. **Create a virtual environment:**

    ```
    python -m venv .venv
    ```
    ```
    python -m venv [Pick a name from .gitignore file]
    ```

2. **Activate the virtual environment:**

    - Linux :
        ```
        source .venv/bin/activate
        ```
    - Windows:
        ```
        venv\Scripts\activate
        ```

3. ** To Deactivate the virtual environment:**

    ```
    deactivate
    ```


### Installing

1. Clone the repository

    ```
    git clone https://github.com/salty-ivy/vendor-management-system.git
    ```

2. Install the required packages

    ```
    poetry install
    ```

3. Run the server Using the Makefile

    The Makefile in this project provides several targets that can be used to perform common tasks. To use the Makefile, open a terminal or command prompt and navigate to the root directory of your project.

    - Available Targets
        - **runserver**: Start the development server.

            ```
            make runserver
            ```
        - **db**: Perform database migrations

            ```
            make db
            ```

        - **app**: Create a new Django app.

            ```
            make app NAME=<app_name>
            ```

        - **superuser**: Create a superuser for the Django admin.

            ```
            make superuser
            ```

    You can run these commands by executing make followed by the target name in your terminal. For example, to start the development server, you can run `make runserver`.

4. Open the browser and go to http://localhost:8000

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Django REST Framework](http://www.django-rest-framework.org/) - The REST API framework used

## API Endpoints

### Vendor

* GET /api/vendors/ - List all vendors
* POST /api/vendors/ - Create a new vendor
* GET /api/vendors/{id}/ - Retrieve a vendor
* PUT /api/vendors/{id}/ - Update a vendor
* DELETE /api/vendors/{id}/ - Delete a vendor

### Purchase Order

* GET /api/purchase_orders/ - List all purchase orders
* POST /api/purchase_orders/ - Create a new purchase order
* GET /api/purchase_orders/{id}/ - Retrieve a purchase order
* PUT /api/purchase_orders/{id}/ - Update a purchase order
* DELETE /api/purchase_orders/{id}/ - Delete a purchase order

### Vendor Performance

* GET /api/vendor_performance/ - List all vendor performances


### Use Swagger UI to test the API

* Go to http://localhost:8000/swagger/

* Click on "Authorize" button on the top right corner

* Enter the following credentials:
```
tokenAuth (apiKey) : "Token e9c99278469375ec523d76d38ae2c33cb9d8a3b3"
```
and click on "Authorize" button

* Now you can test the API. Click on any endpoint and then click on "Try it out" button. Enter the required parameters and click on "Execute" button.

## Screenshots

![swagger api docs]()
![swagger authorization]()
![purchase order api]()

## Test Suite

To run the test suite, run the following command:
```
python manage.py test
```
