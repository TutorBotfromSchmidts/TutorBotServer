def temp_html_v5():
    html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Teaching Chatbot</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>

    <div class="container">
        <div class="header">        <!-- Header section with title and instructions -->
            <h1>TutorBot Learning Center</h1>
            <p>Select your class from the dropdown below and then select the lesson you would like to work on.</p>
            <br>
            <!-- Dropdowns for selecting class and lesson -->
            <div>
                <label for="classDropdown">Class:</label>
                <select id="classDropdown">
                    <option value="">Select a class</option>
                </select>

                <label for="lessonDropdown">Lesson:</label>
                <select id="lessonDropdown">
                    <option value="">Select a lesson</option>
                </select>
                <!-- Display the current loaded lesson -->
                <p id="lessonNameDisplay">No lesson loaded</p>
            </div>
        </div>
        <!-- Chat area for interaction -->
        <div class="chat-area">
            <label for="responseOutput">Response:</label>
            <div id="responseOutput" class="response-output"></div>
            <label for="userInput">Request:</label>
            <div class="input-container">
                <!-- Loading indicator -->
                <div id="thinkingIndicator" class="loader" style="display: none;"></div>
                <textarea id="userInput" class="user-input"></textarea>
            </div>
        </div>
    </div>
        <footer>
            <!-- Send button for submitting requests -->
            <button id="sendButton">Send</button>
            <button id="copyButton">Copy</button>
        </footer>

    <!-- Scripts for dynamic behavior and data fetching -->
    <script>
// Base URL of the application
const baseURL = window.location.origin;
// Variable to track selected class ID for requests
let selectedClassId = null;

// Event listener to initialize the application once the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    console.log('Initializing application...');
    initializeApp();
});

// Function to initialize the application
function initializeApp() {
    setCookie() // Set a session cookie
        .then(fetchClasses) // Fetch available classes after setting the cookie
        .catch(error => console.error('Initialization error:', error)); // Log any initialization errors
    addEventListeners(); // Add event listeners for user interactions
}

// Function to set a session cookie
async function setCookie() {
    try {
        const response = await fetch(`${baseURL}/set-cookie/`, {
            method: 'GET',
            credentials: 'include' // Include credentials (cookies) in the request
        });
        if (!response.ok) throw new Error(`Failed to set cookie: ${response.statusText}`);
        const data = await response.json();
        console.log('Cookie set:', data.message); // Log the response message
    } catch (error) {
        console.error('Error setting cookie:', error); // Log any errors that occur
        throw error; // Rethrow the error to be caught in the promise chain
    }
}

// Function to fetch available classes from the server
async function fetchClasses() {
    try {
        console.log('Fetching classes...');
        const response = await fetch(`${baseURL}/classes/`, {
            method: 'GET',
            credentials: 'include'
        });
        if (!response.ok) throw new Error(`Failed to fetch classes: ${response.statusText}`);
        const data = await response.json();
        console.log('Classes fetched:', data); // Log the fetched data
        data.directories.sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase())); // Sort lessons alphabetically (case-insensitive)
        populateDropdown('classDropdown', data.directories, 'Select a class'); // Populate the class dropdown with fetched data
    } catch (error) {
        console.error('Error fetching classes:', error); // Log any errors that occur
    }
}

// Function to fetch lessons based on the selected class
async function fetchLessons() {
    try {
        const lessonDropdown = document.getElementById('lessonDropdown');
        lessonDropdown.innerHTML = '<option value="">Select a lesson</option>'; // Clear the lesson dropdown
        if (selectedClassId) {
            const response = await fetch(`${baseURL}/classes/${selectedClassId}/conundrums/`, {
                method: 'GET',
                credentials: 'include'
            });
            if (!response.ok) throw new Error(`Failed to fetch lessons: ${response.statusText}`);
            const data = await response.json();
            console.log('Lessons fetched:', data); // Log the fetched data
            data.files.sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase())); // Sort lessons alphabetically (case-insensitive)
            populateDropdown('lessonDropdown', data.files, 'Select a lesson'); // Populate the lesson dropdown with fetched data
        }
    } catch (error) {
        console.error('Error fetching lessons:', error); // Log any errors that occur
    }
}

// Function to populate a dropdown with items
function populateDropdown(dropdownId, items, defaultOptionText) {
    const dropdown = document.getElementById(dropdownId);
    dropdown.innerHTML = `<option value="">${defaultOptionText}</option>`; // Set the default option
    items.forEach(item => {
        const option = document.createElement('option');
        option.value = item;
        option.textContent = item;
        dropdown.appendChild(option); // Add each item as an option in the dropdown
    });
}

// Function to send a message to the chatbot
async function sendMessage() {
    try {
        const userInputElement = document.getElementById('userInput');
        const userInput = userInputElement.value;
        const responseOutput = document.getElementById('responseOutput');
        const thinkingIndicator = document.getElementById('thinkingIndicator');

        toggleThinkingIndicator(thinkingIndicator, true); // Show the thinking indicator

        const response = await fetch(`${baseURL}/chatbot/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: userInput }), // Send the user input as a JSON payload
            credentials: 'include'
        });

        toggleThinkingIndicator(thinkingIndicator, false); // Hide the thinking indicator

        if (!response.ok) throw new Error(`Failed to send message: ${response.statusText}`);
        const data = await response.json();
        updateChat(responseOutput, userInput, data.text); // Update the chat area with the bot's response

        userInputElement.value = ''; // Clear the user input
        adjustTextAreaHeight(userInputElement); // Adjust the height of the textarea
        userInputElement.scrollIntoView({ behavior: 'smooth' }); // Scroll the input into view
    } catch (error) {
        console.error('Error sending message:', error); // Log any errors that occur
    }
}

// Function to show or hide the thinking indicator
function toggleThinkingIndicator(indicator, show) {
    indicator.style.display = show ? 'block' : 'none';
}

// Function to update the chat area with user and bot messages
function updateChat(outputElement, userInput, botResponse) {
    const formattedUserInput = formatLinks(userInput); // Format links in the user input
    const formattedResponse = formatLinks(botResponse); // Format links in the bot response
    const timestamp = new Date().toLocaleTimeString(); // Get the current time

    const userMessage = `<div class="user-message"><span class="message-text">User: ${formattedUserInput}</span><span class="timestamp">${timestamp}</span></div>`;
    const botMessage = `<div class="bot-message"><span class="message-text">Bot: ${formattedResponse}</span><span class="timestamp">${timestamp}</span></div>`;
    outputElement.innerHTML += userMessage + botMessage; // Append the messages to the chat area
    outputElement.scrollTop = outputElement.scrollHeight; // Scroll to the bottom of the chat area
}

function copyToClipboard() {
    const responseOutput = document.getElementById('responseOutput').innerText;
    navigator.clipboard.writeText(responseOutput).then(() => {
        console.log('Content copied to clipboard!');
        alert('Content copied to clipboard!');  // Optional: alert the user of successful copy.
    }).catch(err => {
        console.error('Failed to copy text: ', err);
    });
}

// Function to format links in a given text
function formatLinks(text) {
    const urlPattern = /(https?:\/\/[^\s]+)/g;
    return text.replace(urlPattern, '<a href="$1" target="_blank">$1</a>'); // Replace URLs with clickable links
}

// Function to add event listeners for user interactions
function addEventListeners() {
    document.getElementById('sendButton').addEventListener('click', sendMessage); // Event listener for the send button
    document.getElementById('copyButton').addEventListener('click', copyToClipboard);
    document.getElementById('userInput').addEventListener('keypress', function(event) {
        if (event.key === 'Enter' && !event.shiftKey) {
            event.preventDefault(); // Prevent the default Enter key behavior (i.e., new line)
            sendMessage(); // Send the message when Enter is pressed
        }
    });

    document.getElementById('userInput').addEventListener('input', function() {
        adjustTextAreaHeight(this); // Adjust the height of the textarea when the input changes
    });

    document.getElementById('classDropdown').addEventListener('change', function() {
        if (!this.value) {
            console.warn('No class selected. Please select a class.');
            return; // Do nothing if no class is selected
        }
        selectedClassId = this.value; // Update the selected class ID
        fetchLessons(); // Fetch lessons for the selected class
    });

    document.getElementById('lessonDropdown').addEventListener('change', async function() {
        const selectedLesson = this.value;
        const lessonNameDisplay = document.getElementById('lessonNameDisplay');

        if (selectedLesson) {
            try {
                const response = await fetch(`${baseURL}/classes/${selectedClassId}/conundrums/${selectedLesson}`, {
                    method: 'GET',
                    credentials: 'include'
                });
                if (!response.ok) throw new Error(`Failed to fetch lesson content: ${response.statusText}`);
                const lessonContent = await response.text();
                sessionStorage.setItem('currentLesson', lessonContent); // Store the lesson content in session storage
                lessonNameDisplay.textContent = 'Loaded Lesson: ' + selectedLesson; // Display the loaded lesson name
            } catch (error) {
                console.error('Error fetching lesson content:', error); // Log any errors that occur
                lessonNameDisplay.textContent = 'Failed to load lesson'; // Display an error message
            }
        } else {
            lessonNameDisplay.textContent = 'No lesson selected'; // Display a default message if no lesson is selected
        }
    });
}

// Function to adjust the height of a textarea based on its content
function adjustTextAreaHeight(textarea) {
    textarea.style.height = 'auto'; // Reset the height to auto
    textarea.style.height = (textarea.scrollHeight) + 'px'; // Set the height to the scroll height
}

    </script>
</body>
</html>
   """
    return html