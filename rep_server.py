import zmq
import time

def main():
    ctx = zmq.Context()
    server = ctx.socket(zmq.REP)
    server.bind("tcp://*:8989")
    alive = True
    while alive:
        try:
            message = server.recv()
            print("Received:", message)
            time.sleep(3)
            server.send(b"World")
        except KeyboardInterrupt:
            print("Interrupted")
            alive = False
    else:
            server.close()
            ctx.term()

if __name__ == "__main__":
    main()