# FTP SERVER USING SOCKET PROGRAMMING IN PYTHON

This project implements a simple FTP server using socket programming in Python. The client can connect to the server, authenticate with a username and password, and perform basic file operations such as listing files, uploading files and deleting files on the server.

## Features

- **Authentication**: The client must authenticate with a username and password before performing any operations.
- **File Operations**:
  - **LIST**: List all the files on the server.
  - **UPLOAD**: Upload a file to the server.
  - **DELETE**: Delete a file from the server.
  - **LOGOUT**: Disconnect from the server.
  - **HELP**: Display a list of available commands.

## Prerequisites

- Python 3.x
- Tkinter library for GUI (for client).
- Client and server connected to a common network.

## Getting Started

### Server Setup

1. Clone the repository to your server machine.
2. Ensure that the server_data directory exists in the same directory where server.py is present or edit the server.py file and replace the SERVER_DATA_PATH variable with the actual path where you want to store files on the server. 
3. Run the server.py file to start the server.

### Client Setup

1. Clone the repository to your client machine.
2. Edit the client.py file and replace the IP variable with the server's IP address.
3. Ensure that the client_data directory exists in the same directory where client.py is present or copy the actual path from which you want to upload files to the server.
4. Run the client.py file to start connection with the server.

## Usage

1. **Authentication:**

- When you run the client, a login window will appear. Enter your username and password to authenticate.

2. **Passwords:**

- The following usernames and passwords are hardcoded for this project:
   - `alice: password123`
   - `bob: securepass`
   - `charlie: letmein`
   - `dave: secretword`
   - `eve: 123456`
   - `frank: qwerty`
   - `grace: ilovepython`
   - `harry: mypassword`
   - `irene: p@ssw0rd`
   - `jason: pythonrocks`
- You can add or delete username and password in the server.py file.

3. **Commands:**

- After authentication, you can use the following commands:
   - **LIST:** Lists all the files on the server.
   - **UPLOAD `<path>`:** Uploads a file to the server. Replace `<path>` with the path of the file you want to upload.
   - **DELETE `<filename>`:** Deletes a file from the server. Replace `<filename>` with the name of the file you want   to delete from the server.
   - **LOGOUT:** Disconnects from the server.
   - **HELP:** Displays a list of available commands.


## Example

### Server Output

```[STARTING] Server is starting. 
[LISTENING] Server is listening on 192.168.29.147:4469.
[NEW CONNECTION] ('192.168.29.147', 50194) connected.
[ACTIVE CONNECTIONS] 1
[DISCONNECTED] ('192.168.29.147', 50194) disconnected
```

### Client Output

```Welcome to the File Server Login Page.
Authentication successful
Welcome to the File Server.
> HELP
LIST: List all the files from the server.
UPLOAD <path>: Upload a file to the server.
DELETE <filename>: Delete a file from the server.
LOGOUT: Disconnect from the server.
HELP: List all the commands.
> LIST
123.txt
ex.txt
> UPLOAD client_data/abc.txt
File uploaded successfully.
> LIST
123.txt
abc.txt
ex.txt
> DELETE abc.txt
File deleted successfully.
> LIST
123.txt
ex.txt
> LOGOUT
Disconnected From The Server
```

## NOTES

- Ensure that both the client and the server are on the same network.
- Replace the placeholder IP address in the client.py file with the actual server IP address.
- The server should be started before the client tries to connect.

## LICENSE

This project is licensed under the [MIT License](LICENSE) .

## Contributors

- [Shivadarshan](https://github.com/shivadarshan-devadiga)

## Feedback and Support

For any feedback or support regarding this project, please [open an issue](https://github.com/shivadarshan-devadiga/FTP-Server-Using-Socket-Programming-in-Python/issues) on GitHub.
