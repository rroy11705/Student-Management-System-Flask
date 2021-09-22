# Student-Management-System-Flask

---
## Endpoints

### 1. /api/create-user
To create a user using POST method.

The Input format for this endpoint is:
![img.png](resources/create-user-input.png)

The Successful Output of this endpoint is:
![img.png](resources/create-user-output.png)

If email already exist then the output is:
![img.png](resources/create-user-duplicate.png)

---

### 2. /api/get-user/<user_id>
To get an existing user by User ID using GET method.

The Input format for this endpoint is:
![img.png](resources/get-user-input.png)

The Successful Output of this endpoint is:
![img.png](resources/get-user-output.png)

If User ID does not exist then the output is:
![img.png](resources/get-user-404.png)

---

### 3. /api/update-user/<user_id>
To update data of an existing user by User ID using PUT method.

The Input format for this endpoint is:
![img.png](resources/update-user-input.png)

The Successful Output of this endpoint is:
![img.png](resources/update-user-output.png)

If User ID does not exist in db then the output is:
![img.png](resources/update-user-404.png)

---

### 3. /api/delete-user/<user_id>
To delete an existing user by User ID using DELETE method.

The Input format for this endpoint is:
![img.png](resources/delete-user-input.PNG)

The Successful Output of this endpoint is:
![img.png](resources/delete-user-output.PNG)

---