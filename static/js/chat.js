const chatBox = document.getElementById('chat-box');
const chatInput = document.getElementById('chat-input');
const sendButton = document.getElementById('send-btn');
const roomName = JSON.parse(document.getElementById('room-name').textContent);

// Establish WebSocket connection
const chatSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/chat/' + roomName + '/'
);

// Function to add a new message to the chat box and autoscroll
function addMessageToChatBox(message) {
    const messageElement = document.createElement('div');
    messageElement.textContent = message;
    messageElement.style.marginBottom = '5px';
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the bottom
}

// Event listener for receiving messages from WebSocket
chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    addMessageToChatBox(data.message);
};

// Event listener for WebSocket close
chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

// Send message function
function sendMessage() {
    const message = chatInput.value.trim();
    if (message) {
        chatSocket.send(JSON.stringify({
            'message': message
        }));
        chatInput.value = ''; // Clear the input field
    }
}

// Event listener for send button click
sendButton.onclick = sendMessage;

// Event listener for Enter key to send message
chatInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

