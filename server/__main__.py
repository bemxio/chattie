from server import chattie
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="(%(asctime)s) [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)

server = chattie.Server(*sys.argv[1:])
server.run()