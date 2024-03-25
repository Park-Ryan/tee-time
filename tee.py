import socket

targetip = "10.0.0.5"
minport = 1
maxport = 1000

def scanports(target_host, start_port, end_port):
    open_ports = []
    try:
        # Resolve target host to IP address
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print("Error: Unable to resolve target host.")
        return

    # Scan ports within the specified range
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout for the connection attempt
        result = sock.connect_ex((target_ip, port))  # Attempt to connect to the port
        if result == 0:
            open_ports.append(port)
        sock.close()

    return open_ports

if __name == "__main":
    target_host = input("Enter the target host: ")
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))

    open_ports = scan_ports(target_host, start_port, end_port)
    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(port)
    else:
        print("No open ports found.")
