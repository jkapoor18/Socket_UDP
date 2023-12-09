import socket 
import os
from datetime import datetime

# Code for save chat history
def save_chat_history(ip_address, message):
    filename = f"{ip_address}_chat_history.txt"
    with open(filename, 'a') as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {message}\n")

# UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Target system address
#target_ip = "192.168.1.6"
target_ip = "192.168.1.12"
target_port = 9999
final_target = (target_ip, target_port)

# Taking input from user
username = input("Enter your username: ")

while True:
    # Take user input for message
    msg = input("Enter your message (type 'exit' to end): ")

    # Save chat history
    save_chat_history(target_ip, f"{username}: {msg}")

    # Encode message
    new_msg = msg.encode('ascii')

    # Send data
    s.sendto(new_msg, final_target)

    # Check if the user wants to exit
    if msg.lower() == 'exit':
        break

# Close the socket
s.close()
