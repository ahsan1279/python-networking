import socket

# targeted host and port. change it as you want.
target_host = "tcpbin.com"
target_port = 4242

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host,target_port))

# send some data
client.send(f"GET / HTTP?1.1\r\nHost: {target_host}\r\n\r\n".encode('utf-8'))

# receive some data
response = client.recv(4096)

print(response.decode())
client.close()


#More concise

"""
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((target_host,target_port))
    client.send(b"GET / HTTP?1.1\r\nHost: example.com\r\n\r\n")
    response = client.recv(4096)
    print(response.decode())
    
"""
