import argparse
import logging
import socket
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


parser = argparse.ArgumentParser(description="Check if port is open")
parser.add_argument("--service-name", required=True)
parser.add_argument("--ip", required=True)
parser.add_argument("--port", required=True)

args = parser.parse_args()

# Get arguments
SERVICE_NAME = str(args.service_name)
IP = str(args.ip)
PORT = int(args.port)

# Infinite loop
while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((IP, PORT))
    if result == 0:
        logger.info(
            "Port is open! Bye! Service:{} Ip:{} Port:{}".format(SERVICE_NAME, IP, PORT)
        )
        break
    else:
        logger.critical(
            "Port is not open! I'll check it soon! Service:{} Ip:{}"
            "Port:{}".format(SERVICE_NAME, IP, PORT)
        )
        time.sleep(5)
