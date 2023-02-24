import platform
import getpass
import socket
 
my_system = platform.uname()
hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)  

print(f"System: {my_system.system}")
print(f"Node Name: {my_system.node}")
print(f"Release: {my_system.release}")
print(f"Version: {my_system.version}")
print(f"Machine: {my_system.machine}")
print(f"Processor: {my_system.processor}")
print(f"IP Local: {IPAddr}")
print(f"SystemUsername: {getpass.getuser()}")