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
        # will be updated later with a curr time stamp

        




