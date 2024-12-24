
# 📂 **FTP Server Using Socket Programming in Python** 🖥️

This project implements a simple **FTP server** using socket programming in Python. The client can connect to the server, authenticate with a username and password, and perform basic file operations such as listing files, uploading files, and deleting files on the server.

---

## 🚀 **Features**

- **Authentication**: The client must authenticate with a username and password before performing any operations.
- **File Operations**:
  - **LIST**: List all files on the server.
  - **UPLOAD `<path>`**: Upload a file to the server.
  - **DELETE `<filename>`**: Delete a file from the server.
  - **LOGOUT**: Disconnect from the server.
  - **HELP**: Display a list of available commands.

---

## 🛠️ **Prerequisites**

- Python 3.x
- Tkinter library for GUI (for the client).
- Client and server must be connected to a common network.

---

## 🚦 **Getting Started**

### **Server Setup**:

1. Clone the repository to your server machine.
2. Ensure that the `server_data` directory exists in the same directory as `server.py`. You can modify the `SERVER_DATA_PATH` variable in `server.py` to specify a custom location for storing server files.
3. Run the `server.py` file to start the server.

### **Client Setup**:

1. Clone the repository to your client machine.
2. Edit the `client.py` file and replace the `IP` variable with the actual IP address of the server.
3. Ensure that the `client_data` directory exists in the same directory as `client.py`. This directory should contain files you want to upload to the server.
4. Run the `client.py` file to connect to the server.

---

## 🔑 **Usage**

### **Authentication**:

- When you run the client, a login window will appear. Enter your **username** and **password** to authenticate.

### **Credentials**:

- The following usernames and passwords are hardcoded into the server for authentication:
  
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

You can modify the list of usernames and passwords in the `server.py` file.

### **Commands**:

After authentication, you can use the following commands:

- **LIST**: Lists all files on the server.
- **UPLOAD `<path>`**: Uploads a file from the specified path on the client to the server.
- **DELETE `<filename>`**: Deletes a file from the server.
- **LOGOUT**: Disconnects from the server.
- **HELP**: Displays a list of available commands.

---

## 🔎 **Example Usage**

### **Server Output**:

```bash
[STARTING] Server is starting.
[LISTENING] Server is listening on 192.168.29.147:4469.
[NEW CONNECTION] ('192.168.29.147', 50194) connected.
[ACTIVE CONNECTIONS] 1
[DISCONNECTED] ('192.168.29.147', 50194) disconnected
```

### **Client Output**:

```bash
Welcome to the File Server Login Page.
Authentication successful.
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
Disconnected from the server.
```

---

## ⚠️ **Notes**

- Ensure that both the client and server are on the same network.
- Replace the placeholder IP address in the `client.py` file with the actual IP address of the server.
- The server must be running before the client can connect.
- **File Paths**: The `client_data` directory on the client machine should contain the files you want to upload to the server.

---

## 📜 **License**

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 **Contributors**

- [Shivadarshan](https://github.com/shivadarshan-devadiga)

---

## 🛠️ **Feedback and Support**

For any feedback or support regarding this project, please [open an issue](https://github.com/shivadarshan-devadiga/FTP-Server-Using-Socket-Programming-in-Python/issues) on GitHub.

---

Thank you for exploring the **FTP Server Using Socket Programming in Python**! 💻
