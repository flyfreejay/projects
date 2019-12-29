'''
Date:       Oct 24th, 2019
Developer:  Jay Lee
version:    v0.01

Description: Enter ipv4 address and will scan the port from 1 to 500
and return if the port is open or not

inspired by 
https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/12-Final%20Capstone%20Python%20Project/02-Final%20Capstone%20Project%20Ideas.ipynb
https://www.pythoncircle.com/post/679/python-script-15-creating-a-port-scanner-in-8-lines-of-python/
https://www.tutorialspoint.com/python_penetration_testing/python_penetration_testing_network_scanner.html
'''
import socket

#get user input for the target ipv4 address
targetIp = input("Enter the target IP address: ")   

def portscan(port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET means ipv4 and SOCK_STREAM means socket time we are using
    sock.settimeout(1)
    result = sock.connect_ex((targetIp, port)) #It connects to the targetIp's port but if the connection fails, it just returns error constant
                                               #instead of raising an error
    sock.close()            #it closes the socket file descriptor and I don't know too much about the theory behind that
    return result
    

if __name__ == "__main__":
    for port in range(1001):
        if 0 == portscan(port):
            print("Port " + str(port) + " is open!")