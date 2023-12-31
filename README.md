# Vendor-Management-System

The Vendor Management System is a web application developed using Django and Django REST Framework. It is designed to handle vendor profiles, track purchase orders, and calculate vendor performance metrics. This documentation provides a comprehensive guide for both technical and non-technical users on how to use and navigate the system.

*Login Credentials:* ( If using `docker` or ran `auto_create_superuse` management command )

```
username: admin
password: admin
```


## Features

1. **Vendor Management:**
   - Create, update, and delete vendors.

2. **Purchase Order Management:**
   - Create, update, and delete purchase orders.
   - acknowledge purchase orders

3. **Vendor Performance Metrics:**
   - Calculate vendor performance metrics.


## Getting Started

### Virtual Environment

### Virtual Environment setup

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

3. **To Deactivate the virtual environment:**

    ```
    deactivate
    ```
### ENV file setup

`env.example` showcase an example env file

You can create a file named `env` local to your system which can be deteceted by the project to configure your custom database credentials and specifications


### Installing

#### Clone the repository

```
git clone https://github.com/salty-ivy/vendor-management-system.git
```

#### Install the required packages

```
pip install poetry
```

```
poetry install
```

#### Run the server Using the Makefile

The Makefile in this project provides several targets that can be used to perform common tasks. To use the Makefile, open a terminal or command prompt and navigate to the root directory of your project.

- Available Targets
    - **db**: Perform database migrations, `makemigrations`, `migrate`

        ```
        make db
        ```

    - **runserver**: Start the development server, `runserver`.

        ```
        make runserver
        ```

- Other available commnds
    - **app**: Create a new Django app, `startapp`.

        ```
        make app NAME=<app_name>
        ```

    - **superuser**: Create a superuser for the Django admin, `createsuperuser` .

        ```
        make superuser
        ```

    - **urls**: lists all URL path for all regitered and available endpoints, `show_urls` by `django-extensions`
        ```
        make urls
        ```

    - **auto_create_superuser**: A custom management command in vendor app that creates a super user with `username = admin` and `password = admin`
    ```
    make auto_create_superuser
    ```

    - **tests**: Run all available tests
        ```
        make tests
        ```

    - **test-specific <name>**: Run a specific test whose modular path is passed as an argument
        ```
        make test-specific NAME=vendor.tests
        ```

You can run these commands by executing make followed by the target name in your terminal. For example, to start the development server, you can run `make runserver`.

#### Run with Docker

dockerfile and docker-compose has been setup to use alpine image `sqlite3` databse with consistent volume, it servers as an instant start up via docker daemon.
It will:
- migrate database schema
- create super user
- start the server

```
docker-compose build && docker compose up
```

#### Open the browser and go to http://localhost:8000

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Django REST Framework](http://www.django-rest-framework.org/) - The REST API framework used

### Additional third party dependency

* [djnagorestframework-simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) - For token based authentications
* [django-extensions](https://django-extensions.readthedocs.io/en/latest/) - For shell based visualisation of available URLs

## API Endpoints

### Login/Token

* POST /api/token/ - Return `access` and `refresh` tokens
* POST /api/token/refresh/ - Returns a new set of `access` and `refresh` tokens

### Vendor

* *GET* `/api/vendors/` - List all vendors
* *POST* `/api/vendors/` - Create a new vendor
* *GET* `/api/vendors/{pk}/` - Retrieve a vendor
* *PUT* `/api/vendors/{pk}/` - Update a vendor
* *DELETE* `/api/vendors/{pk}/` - Delete a vendor
* *GET* `/api/vendors/{pk}/performance/` - Rrturns vendors performance records and historical performance of each order issues to that vendor

Details of  [Vendor endpoints here](src/docs/vendor/endpoints.md)

### Purchase Order

* *GET* `/api/purchase_orders/` - List all purchase orders
* *POST* `/api/purchase_orders/` - Create a new purchase order
* *GET* `/api/purchase_orders/{pk}/` - Retrieve a purchase order
* *PUT* `/api/purchase_orders/{pk}/` - Update a purchase order
* *DELETE* `/api/purchase_orders/{pk}/` - Delete a purchase order
* *POST* `/api/purchase_orders/{pk}/acknowledge/` -  Update acknowledgment_date and trigger the recalculation of average_response_time.

Details of  [Purchase Order endpoints here](src/docs/order/endpoints.md)

## Test Suite

Tests are structured in 2 ways
- unit tests which are under `vendor`, `order` directories testing their specific endpoints
- `tests` directory on root level is provided directory for any integration test suite

To run the test suite, run the following command:
```
make tests
```

To run a specific test you can provide modular path to that project

```
make test-specific NAME=vendor.tests # runs only vendor app's tests
```
