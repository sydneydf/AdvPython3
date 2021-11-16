import socket
import random

QUEUE_SIZE = 5

mystery_responses = [
    "It is certain",
    "Outlook good",
    "You may rely on it",
    "Ask again later",
    "Concentrate and ask again",
    "Reply hazy, try again",
    "My reply is no",
    "My sources say no"
]


def server():
    """
    Listen for message
    :return: Random mystery response to client
    """
    serv = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )
    serv.bind(('', 5000))
    serv.listen(QUEUE_SIZE)

    # always listen for connections
    while True:
        conn, addr = serv.accept()
        print("Connecting")
        print(f"Connection: {addr}")
        from_client = ''

        # always listen for data
        while True:
            data = conn.recv(4096)
            # end of data - if none break
            if not data:
                break
            from_client += data.decode()
            print(from_client)
            conn.send(random.choice(mystery_responses).encode())

        conn.close()
        print("Client Disconnected")


if __name__ == '__main__':
    server()
