import time

class TokenBucket:

    def __init__(self, tokens, time_unit, forward_callback, drop_callback):
        self.tokens = tokens
        self.time_unit = time_unit
        self.forward_callback = forward_callback
        self.drop_callback = drop_callback
        self.bucket = tokens
        self.last_check = time.time()

        # tokens our number of tokens
        # when our tokens are added
        # called when the packet is forwarded
        # called when the packets should be dropped
        # our bucket is prefilled with tokens to 
        # will be updated later with a curr timestamp

    def handle(self, packet):
        current = time.time()
        time_passed = current - self.last_check #a:
        self.last_check = current #b:

        self.bucket = self.bucket + \
            time_passed * (self.tokens / self.time_unit) #c:

        if (self.bucket > self.tokens): #d:
            self.bucket = self.tokens

        if (self.bucket < 1): #e:
            self.drop_callback(packet)
        else:
            self.bucket = self.bucket - 1 #f:
            self.forward_callback(packet)

        # handle accepts one param packet
        # our curr time into curr
        #a: time passed between now and the previous handle call is put into time_passed
        #b: update last check to curr timestamp
        #c: use maths to configure how many tokens will be added to our bucket
        #d: reset the bucket if higher value than default value
        #e: if bucket doesn't have the required amount of packets, drop the bucket
        #f: else, remove one token 


# TESTS

def forward(packet):
    print("Packet Forwarded: " + str(packet))


def drop(packet):
    print("Packet Dropped: " + str(packet))


throttle = TokenBucket(1, 1, forward, drop)

packet = 0

while True:
    time.sleep(0.2)
    throttle.handle(packet)
    packet += 1
