import socket
import subprocess

run_again = True

while run_again:

    print("Searching for Ips...")
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    network_ip = local_ip[:local_ip.rfind('.')+1]

    for i in range(1, 255):
        ip = network_ip + str(i)
        response = subprocess.run(['ping', '-n', '1', '-w', '1', ip], 
        stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        if response.returncode == 0:
            try:
                hostname = socket.gethostbyaddr(ip)[0]
            except socket.herror:
                hostname = "Not Found"
            print(f"{ip}\t{hostname}")
    again=str(input("Would you Like to check Ips again?: "))
    if again == "no":
        run_again = False


