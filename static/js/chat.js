const chatBox = document.getElementById('chat-box');
const chatInput = document.getElementById('chat-input');
const sendButton = document.getElementById('send-btn');
const roomName = // get the room name from your context
const userName = // get the user name from your context or prompt the user for it

const chatSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/chat/' + roomName + '/'
);

// Function to display messages in the chat box
function displayMessage(user, message) {
    chatBox.innerHTML += '<div><strong>' + user + ':</strong> ' + message + '</div>';
}

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    displayMessage(data.user_name, data.message);  // Display the message with user name
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

// Event handler for the send button
sendButton.onclick = function() {
    const message = chatInput.value;
    chatSocket.send(JSON.stringify({
        'message': message,
        'user_name': userName  // Include user name in the message data
    }));
    chatInput.value = ''; // Clear input field
};
