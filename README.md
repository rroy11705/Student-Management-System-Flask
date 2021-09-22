# Student-Management-System-Flask

## Description

This is a simple API using Flask and MongoDB. The application can perform CRUD operations and store the data in the 
database. The motivation of the project is to learn the basic concepts of Flask and MongoDB and implement them.
* **Flask** is a lightweight web application framework designed to get results fast and leave room to make the app more detailed in the future.
   Here we do not having to follow a strict convention, hence it could accelerate the development process and gives developers the added flexibility.
* As a document database, **MongoDB** makes it easy for developers to store structured or unstructured data. It uses a JSON-like format to store documents. This format directly maps to native objects in most modern programming languages, making it a natural choice for developers, as they don’t need to think about normalizing data. MongoDB can also handle high volume and can scale both vertically or horizontally to accommodate large data loads.

---

## Pre-requisites
At least Python 3.6 installed. 
* [Installation guide on Windows](https://docs.python.org/3.6/using/windows.html)
* [Installation guide on Unix](https://docs.python.org/3.6/using/unix.html)
* [Installation guide on Macintosh](https://docs.python.org/3.6/using/mac.html)

---

## Getting Started

1. Clone the repository using:
    > git clone https://github.com/rroy11705/Student-Management-System-Flask.git

2. Go to console, open the folder and install dependencies from _requirements.txt_ file using:
    > pip install -r requirements.txt

3. Make Sure you have mongodb installed and running. 
   You can refer to the [official installation guide of mongodb](https://docs.mongodb.com/manual/installation/).

4. In _config.py_ change your mongodb __username__ and __password__.

5. From console run the _run-app.py_ using:
    > python run-app.py

6. Use Postman to check the endpoints.

---
## Endpoints

### 1. /api/create-user
To create a user using POST method.

The Input format for this endpoint is:
![create-user-input](resources/create-user-input.png)

The Successful Output of this endpoint is:
![create-user-output](resources/create-user-output.png)

If email already exist then the output is:
![create-user-duplicate](resources/create-user-duplicate.png)


### 2. /api/get-user/<user_id>
To get an existing user by User ID using GET method.

The Input format for this endpoint is:
![get-user-input](resources/get-user-input.png)

The Successful Output of this endpoint is:
![get-user-output](resources/get-user-output.png)

If User ID does not exist then the output is:
![get-user-404](resources/get-user-404.png)


### 3. /api/update-user/<user_id>
To update data of an existing user by User ID using PUT method.

The Input format for this endpoint is:
![update-user-input](resources/update-user-input.png)

The Successful Output of this endpoint is:
![update-user-output](resources/update-user-output.png)

If User ID does not exist in db then the output is:
![update-user-404](resources/update-user-404.png)


### 3. /api/delete-user/<user_id>
To delete an existing user by User ID using DELETE method.

The Input format for this endpoint is:
![delete-user-input](resources/delete-user-input.PNG)

The Successful Output of this endpoint is:
![delete-user-output](resources/delete-user-output.PNG)

---

# Credits

I would like to appreciate Xoriant Solutions Pvt. Ltd. to give us the opportunity to learn new technology for making this API. 
I would also like to appreciate our mentor Onkar, who made us understand key concepts and guided us in the learning path.

---

## LICENSE

[MIT License](https://github.com/rroy11705/Student-Management-System-Flask/blob/main/LICENSE)
Copyright (c) 2021 Rahul Roy