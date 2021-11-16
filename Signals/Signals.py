import signal
import os
import time


def interrupt_handler(signum, frame):
    if signum == signal.SIGINT:
        print('Signal received - Warning that script termination has taken place')
        exit()


if __name__ == '__main__':
    # interupt signal and assign interrupt_handler
    signal.signal(signal.SIGINT, interrupt_handler)
    print("Press 'CTRL+C'")
    time.sleep(100)
