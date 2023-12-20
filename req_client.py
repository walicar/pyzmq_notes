import zmq

def main():
    ctx = zmq.Context()
    client = ctx.socket(zmq.REQ)
    client.connect("tcp://localhost:8989")
    msg = b"Hello"
    print("Sending:", msg)
    client.send(msg)
    recv = client.recv()
    print("Received:", recv)
    return

if __name__ == "__main__":
    main()