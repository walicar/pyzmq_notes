import zmq

### DEALER
# usually you wait for replies just using a REQ socket,
# but with dealer, you can send any amount of messages
# without waiting for replies...

def main():
    ctx = zmq.Context()
    client = ctx.socket(zmq.DEALER)
    client.connect("tcp://localhost:8989")
    msg = b"Hello"
    identity = b"Battler"
    print("Sending:", msg)
    # send 
    # client.send_multipart([identity, b'', msg], zmq.MORE) # optional
    client.send_multipart([b'', msg], zmq.MORE) # sending to a REP socket
    recv = client.recv_multipart()
    print("Received:", recv)
    return

if __name__ == "__main__":
    main()