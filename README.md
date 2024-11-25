## HTTP Server

This repository contains my implementation of a HTTP server in C. The server is capable of handling basic HTTP requests and supports dynamic content generation through CGI script.

### Features

  - Connection Handling:
        Accepts incoming connections from web browsers or other HTTP clients.

  - Request Processing:
        Parses incoming HTTP requests.
        Processes the requested resource with the following behavior:
    - Directory Request: Lists the directory contents.
    - File Request: Cats the contents of a regular file.
    - CGI Script: Executes CGI scripts to dynamically generate responses (includes a sample Python script that greets the user and displays system information).
    - Non-Existent Resource: Returns an appropriate HTTP error message.

  - Concurrency:
        Supports concurrent client connections using fork().

### How to use
1- Clone the repo:
```
git clone <repository-url>
cd HTTP-server
```
2- Build the Server: Compile the source code:
```
gcc -o httpserver httpserver.c
```
3- Run the Server: Start the server on a specified port (e.g., 8080):
```
./http_server 8080
```
4- Access the Server: Open a web browser or use tools like curl to send requests:
curl http://localhost:8080

### sample output

Directory listing using url: http://localhost:8888
![image](https://github.com/user-attachments/assets/38dade67-f7ce-452b-891f-a564b077a2c6)

File content using url: http://localhost:8888/home/fatma/file
![image](https://github.com/user-attachments/assets/a9221104-a280-4cbb-a2b7-5f51313f85e2)

Running cgi script to greet user using url: http://localhost:8888/cgi-bin/info.py?name=fatma
![image](https://github.com/user-attachments/assets/2bc191e7-aef9-4ab0-9586-cb8ce9b491da)

Running cgi script to display sytem info using url: http://localhost:8888/cgi-bin/info.py?name=info
![image](https://github.com/user-attachments/assets/ead92cb5-980e-4a67-ad19-9e515ef1e8b0)

HTTP error message for non-existent resource:
![image](https://github.com/user-attachments/assets/65f17138-0b27-4919-8e68-c0ada62c8d13)





