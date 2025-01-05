# Products API Setup

## Prerequisites
Make sure you have the following installed:
1. **Python 3.10+** - [Download here](https://www.python.org/downloads/)
2. **Virtualenv** - Create easily with help of Pycharm:
   Settings -> Project Settings -> Create New Python Interpreter using Virtual Env

---

## Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Database Setup
Apply migrations to set up the database: 
```bash
python manage.py migrate
```

## Run the Server
Preferred way is to Setup a Pycharm Configuration for runserver command.
```bash
python manage.py runserver
```
The application will be available at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## API Documentation
### Postman Collection
Use the attached Postman collection to test the APIs.
1. Download attached Postman Collection
2. Import the provided JSON file named `[Products_Demo.postman_collection.json](Products_Demo.postman_collection.json)`.

### Importing the Collection
1. Open Postman.
2. Go to **File** -> **Import**.
3. Select the `[Products_Demo.postman_collection.json](Products_Demo.postman_collection.json)` file.
4. Click **Import**.

### Running Requests in Postman
1. Ensure the collection is imported.
2. Select the desired API request from the collection.
3. Input any necessary body parameters in JSON format.
4. Click Send and check the response in the lower panel.

