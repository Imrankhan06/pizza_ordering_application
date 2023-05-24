# Pizza Ordering App

This is a pizza ordering application built with Django and Django REST framework.

## Setup

1. Install Docker: Make sure you have Docker installed on your system.

2. Clone the repository: Clone this repository to your local machine.

3. Build and run the Docker containers: Open a terminal and navigate to the project directory. Run the following command to build and run the Docker containers:

   ```
   docker-compose up --build
   ```

   This will build the Docker image and start the containers for the Django app and PostgreSQL database.

4. Access the app: Once the containers are up and running, you can access the Django app at `http://localhost:8000`.

## Running Tests

To run the tests for the app, follow these steps:

1. Make sure the Docker containers are running.

2. Open a new terminal window.

3. Navigate to the project directory.

4. Run the following command to run the tests:

   ```
   docker-compose run web python manage.py test
   ```

   This will execute the test suite and display the test results.

## API Documentation

The app exposes the following APIs:

- List all orders:
  - Method: GET
  - URL: `http://localhost:8000/orders/`

- Create a new order:
  - Method: POST
  - URL: `http://localhost:8000/orders/`
  - Request Body: Provide the necessary data for the order creation.
  - Eg:
  ```json
    {
      "flavors": [
        {"flavor": "salami"}
      ],
      "sizes": [
        {"size": "large"}
      ],
      "customer": {
        "name": "John Doe",
        "address": "123 Main St",
        "phone_number": "555-1234"
      },
      "delivery_status": "pending",
      "quantity": 2
    }
    ```

- Retrieve an order:
  - Method: GET
  - URL: `http://localhost:8000/orders/<order_id>/`
  - Replace `<order_id>` with the ID of the specific order.

- Update an order:
  - Method: PUT
  - URL: `http://localhost:8000/orders/<order_id>/`
  - Replace `<order_id>` with the ID of the specific order.
  - Request Body: Provide the updated data for the order.
  - Eg:
  ```json
    {
      "flavors": [
        {"flavor": "margarita"},
        {"flavor": "salami"}
      ],
      "sizes": [
        {"size": "small"},
        {"size": "large"}
      ],
      "customer": {
        "name": "John Doe",
        "address": "123 Main St",
        "phone_number": "555-1234"
      },
      "delivery_status": "delivered",
      "quantity": 4
    }
    ```

- Delete an order:
  - Method: DELETE
  - URL: `http://localhost:8000/orders/<order_id>/`
  - Replace `<order_id>` with the ID of the specific order.

Make sure to replace `<order_id>` with the actual order ID when making requests to retrieve, update, or delete a specific order.