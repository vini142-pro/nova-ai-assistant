
const chatForm = document.getElementById("chatForm");
const messageInput = document.getElementById("messageInput");
const messages = document.getElementById("messages");
const welcomeSection = document.getElementById("welcomeSection");
const typingIndicator = document.getElementById("typingIndicator");
const sendButton = document.getElementById("sendButton");
const voiceButton = document.getElementById("voiceButton");

let isBusy = false;


// Display a message safely in the chat window
function addMessage(sender, text) {
    welcomeSection.hidden = true;

    const messageElement = document.createElement("div");
    messageElement.className = `message ${sender}`;

    const label = document.createElement("div");
    label.className = "message-label";
    label.textContent = sender === "user" ? "You" : "Nova";

    const bubble = document.createElement("div");
    bubble.className = "message-bubble";

    // textContent prevents messages from being interpreted as HTML
    bubble.textContent = text;

    messageElement.append(label, bubble);
    messages.appendChild(messageElement);

    scrollToLatest();
}


// Keep the latest message visible
function scrollToLatest() {
    const chatContainer = document.querySelector(".chat-container");

    chatContainer.scrollTop = chatContainer.scrollHeight;
}


// Show or hide the loading state
function setBusy(busy) {
    isBusy = busy;

    sendButton.disabled = busy;
    voiceButton.disabled = busy;
    messageInput.disabled = busy;

    typingIndicator.hidden = !busy;
}


// Automatically expand the input as the user types
messageInput.addEventListener("input", () => {
    messageInput.style.height = "auto";

    messageInput.style.height =
        Math.min(messageInput.scrollHeight, 140) + "px";
});


// Send a text message to FastAPI
async function sendMessage(message) {
    const cleanMessage = message.trim();

    if (!cleanMessage || isBusy) {
        return;
    }

    addMessage("user", cleanMessage);

    messageInput.value = "";
    messageInput.style.height = "auto";

    setBusy(true);

    try {
        const response = await fetch("/api/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: cleanMessage
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(
                data.detail || "Could not get a response."
            );
        }

        addMessage("assistant", data.reply);

    } catch (error) {
        console.error("Chat error:", error);

        addMessage(
            "assistant",
            "Sorry, something went wrong. Please check that the backend is running and try again."
        );

    } finally {
        setBusy(false);
        messageInput.focus();
    }
}


// Handle the send button
chatForm.addEventListener("submit", (event) => {
    event.preventDefault();
    sendMessage(messageInput.value);
});


// Enter sends; Shift + Enter adds a new line
messageInput.addEventListener("keydown", (event) => {
    if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault();
        chatForm.requestSubmit();
    }
});


// Handle suggested prompts
document.querySelectorAll(".suggestion").forEach((button) => {
    button.addEventListener("click", () => {
        sendMessage(button.dataset.message);
    });
});


// Use the existing Python microphone and voice modules
voiceButton.addEventListener("click", async () => {
    if (isBusy) {
        return;
    }

    setBusy(true);
    voiceButton.textContent = "⏳";

    try {
        const response = await fetch("/api/voice", {
            method: "POST"
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(
                data.detail || "Voice request failed."
            );
        }

        if (data.user_message) {
            addMessage("user", data.user_message);
            addMessage("assistant", data.reply);
        } else {
            addMessage("assistant", data.reply);
        }

    } catch (error) {
        console.error("Voice error:", error);

        addMessage(
            "assistant",
            "I couldn't complete the voice request. Check the microphone and backend, then try again."
        );

    } finally {
        setBusy(false);
        voiceButton.textContent = "🎙️";
    }
});
