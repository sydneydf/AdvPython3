import socket


def client(_msg2send: str):
    """
    #Create client socket (AF_INET => IP, SOCK_STREAM => TCP
    @:param _msg2send: string to send to server
    :return:
    """

    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )
    sock.connect(('127.0.0.1', 5000))
    sock.send(_msg2send.encode())
    from_server = sock.recv(4096)
    sock.close()
    print(from_server.decode())


if __name__ == '__main__':
    input_Q = input("Ask the magic 8-ball a question: ")
    client(input_Q)
