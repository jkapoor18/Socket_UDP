import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

my_ip = "0.0.0.0"
my_port = 9999
my_address = (my_ip, my_port)

s.bind(my_address)

def save_chat_history(sender_ip, message):
    filename = f"{sender_ip}_chat_history.txt"
    with open(filename, 'a') as file:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        file.write(f"[{timestamp}] {message}\n")

while True:
    data = s.recvfrom(100)
    new_data = data[0]
    final_msg = new_data.decode('ascii')
    print(final_msg)

    # Extract sender's IP address
    sender_ip = data[1][0]

    # Save chat history
    save_chat_history(sender_ip, final_msg)

    time.sleep(2)
