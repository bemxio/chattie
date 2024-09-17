# Chattie
A chat room with HTML capabilities (totally not an excuse for not sanitizing HTML) made using the classic web development trio, together with the [MessagePack](https://msgpack.org) and [`websockets`](https://pypi.org/project/websockets) libraries. Made for fun, as well as for learning more stuff about WebSockets!

## Running
### Client
You can simply double-click the `client/index.html` file or host it with any kind of a web server, it should work fine.

### Server
Make sure you are running Python 3.8 or higher.

1. Clone the repository to a directory of your choice.
2. Install the requirements using `python3 -m pip install -r server/requirements.txt`.
3. Done! Run the server using `python3 -m server <host> <port>`.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.