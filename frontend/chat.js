async function sendMessage() {
    const messageInput = document.getElementById('message');
    const messagesDiv = document.getElementById('messages');
    const message = messageInput.value;
    
    messagesDiv.innerHTML += `<p><strong>You:</strong> ${message}</p>`;
    messageInput.value = '';

    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message })
        });
        
        const data = await response.json();
        messagesDiv.innerHTML += `<p><strong>AI:</strong> ${data.response}</p>`;
    } catch (error) {
        console.error('Error:', error);
    }
}
