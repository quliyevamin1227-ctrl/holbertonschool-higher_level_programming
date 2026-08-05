# Basics of HTTP/HTTPS

## Difference between HTTP and HTTPS

### HTTP
- HTTP stands for HyperText Transfer Protocol.
- Data is sent in plain text.
- It does not encrypt communication.
- Uses port 80.

### HTTPS
- HTTPS stands for HyperText Transfer Protocol Secure.
- Uses SSL/TLS encryption.
- Protects data from attackers.
- Uses port 443.

---

## Structure of an HTTP Request

Example:

GET /index.html HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Accept: text/html

Components:
- Method
- Path
- HTTP Version
- Headers
- Body (optional)

---

## Structure of an HTTP Response

Example:

HTTP/1.1 200 OK
Content-Type: text/html

<html>...</html>

Components:
- Status Code
- Status Message
- Headers
- Body

---

## Common HTTP Methods

### GET
Description:
Retrieve data.

Use case:
Loading a web page or API data.

### POST
Description:
Send data to the server.

Use case:
Submitting a registration form.

### PUT
Description:
Update an existing resource.

Use case:
Updating user information.

### DELETE
Description:
Delete a resource.

Use case:
Removing a user account.

---

## Common HTTP Status Codes

### 200 OK
Request completed successfully.

Example:
Opening a normal web page.

### 201 Created
A resource was successfully created.

Example:
Creating a new account.

### 301 Moved Permanently
The resource has moved.

Example:
Redirecting from HTTP to HTTPS.

### 404 Not Found
The requested page does not exist.

Example:
Opening an invalid URL.

### 500 Internal Server Error
A server-side error occurred.

Example:
The website crashes due to a server problem.
