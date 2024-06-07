import socket
import tkinter as tk

IP = socket.gethostbyname(socket.gethostname()) #Replace this with server ip address 
PORT = 4469
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

def authenticate(client, username, password):
    data = f"{username}@{password}"
    client.send(data.encode(FORMAT))
    response = client.recv(SIZE).decode(FORMAT)
    if response == "OK@Authenticated":
        print("Authentication successful")
        return True
    else:
        print("Authentication failed. Please try again.")
        return False

def get_credentials():
    def submit():
        nonlocal username, password
        username = username_entry.get()
        password = password_entry.get()
        root.destroy()
    username=None
    password=None
    root = tk.Tk()
    root.title("Login")
    root.geometry("250x100") 
    username_label = tk.Label(root, text="Username:")
    username_label.grid(row=0, column=0, sticky="e")
    username_entry = tk.Entry(root,width=15)
    username_entry.grid(row=0, column=1)
    username_entry.config(font=("Times New Roman",15)) 
    password_label = tk.Label(root, text="Password:")
    password_label.grid(row=1, column=0, sticky="e")
    password_entry = tk.Entry(root, show="*",width=15)
    password_entry.grid(row=1, column=1)
    password_entry.config(font=("Times New Roman", 15))
    submit_button = tk.Button(root, text="Submit", command=submit)
    submit_button.grid(row=2, columnspan=2,pady=20,padx=10)
    root.mainloop()
    return username, password

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    dta = client.recv(SIZE).decode(FORMAT)
    cd, messag = dta.split("@")
    if cd == "DISCONNECTED":
        print(f"[SERVER]: {messag}")
        return
    elif cd == "OK":
        print(f"{messag}")
    username, password = get_credentials()
    a=authenticate(client,username,password)
    if a==False:
       return
    while True:
        data = client.recv(SIZE).decode(FORMAT)
        cmd, msg = data.split("@")
        if cmd == "DISCONNECTED":
            print(f"[SERVER]: {msg}")
            break
        elif cmd == "OK":
            print(f"{msg}")

        data = input("> ")
        data = data.split(" ")
        cmd = data[0]
        if cmd == "HELP":
            client.send(cmd.encode(FORMAT))
        elif cmd == "LOGOUT":
            client.send(cmd.encode(FORMAT))
            break
        elif cmd == "LIST":
            client.send(cmd.encode(FORMAT))
        elif cmd == "UPLOAD":
            path = data[1]
            with open(f"{path}", "r") as f:
                text = f.read()
            filename = path.split("/")[-1]
            send_data = f"{cmd}@{filename}@{text}"
            client.send(send_data.encode(FORMAT))
        elif cmd == "DELETE":
            client.send(f"{cmd}@{data[1]}".encode(FORMAT))
    print("Disconnected From The Server")

if __name__ == "__main__":
    main()