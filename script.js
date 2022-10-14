function createMessageElement(message) {
    let element = document.createElement("div");
    element.className = "message";

    element.innerHTML += `<span class="message-author">${message.author}</span>`;
    element.innerHTML += `<span class="message-content">${message.content}</span>`;

    messages.appendChild(element);
}

const messages = document.getElementById("message-list");
const inputBox = document.getElementById("input-box");
const params = new URLSearchParams(window.location.search);

let ip = params.has("ip") ? params.get("ip") : prompt("Please enter the IP address of a server:");
let name = params.has("name") ? params.get("name") : prompt("Please enter your username:");
let protocol = "ws://";

if (ip.startsWith("https://") || ip.startsWith("wss://")) {
    protocol = "wss://";
}

ip = protocol + ip.slice(ip.indexOf("/") + 2);

const socket = new WebSocket(ip);

inputBox.addEventListener("keydown", (event) => {
    if (event.key != "Enter") {
        return;
    }

    socket.send(MessagePack.encode({
        author: name,
        content: inputBox.value
    }));

    inputBox.value = "";
});

socket.addEventListener("message", async (event) => {
    data = await MessagePack.decodeAsync(event.data.stream());

    for (let i = 0; i < data.length; i++) {
        createMessageElement(data[i]);
    }

    messages.scrollTop = messages.scrollHeight;
});
