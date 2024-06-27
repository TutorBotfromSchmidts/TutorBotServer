def temp_html_v0():
    html = """
<!doctype html>
<html>
<head>
<meta charset="UTF-8">
<title>Teaching Chatbot</title>
<link rel="stylesheet" type="text/css" href="/static/style.css" />
</head>
<body>
<!-- Version 1.0.0 -->
<p>&nbsp;</p>
    <h1>Project Management Learning Center&nbsp;</h1>
    <br>
    <p>This site is used for both Learning and Testing your knowledge. It will start in Learn mode.  You can request a quiz from the chatbot at any time.</p><br>

    <button id="learnButton">Learn</button>
    <button id="testButton">Test</button><br><br><br><br>

    <label for="responseOutput">Response:</label>
    <input type="text" id="responseOutput" readonly />
    <br>
    <label for="userInput">Request:</label>
    <input type="text" id="userInput" />
    <button id="sendButton">Send</button>
    <br>

    <script>
        const baseURL = window.location.origin;

        async function setCookie() {
            const response = await fetch(`${baseURL}/set-cookie/`, {
                method: 'GET',
                credentials: 'include'  // Include credentials (cookies) with the request
            });
            const data = await response.json();
            console.log(data.message);  // For debugging
        }

        // Call the setCookie function on page load
        window.onload = setCookie;

        document.getElementById('sendButton').addEventListener('click', async () => {
            const userInput = document.getElementById('userInput').value;
            const responseOutput = document.getElementById('responseOutput');

            const response = await fetch(`${baseURL}/chatbot/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: userInput }),
                credentials: 'include'  // Include credentials (cookies) with the request
            });

            if (response.ok) {
                const data = await response.json();
                responseOutput.value = data.text;
            } else {
                console.error("Error:", response.status, response.statusText);
            }
        });
    </script>
</body>
</html>
    """
    return html


def temp_html_v1():
    html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Teaching Chatbot</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <!-- Version 1.0.1 -->
    <div class="container">
        <h1>Project Management Learning Center</h1>
        <br>
        <p>This site is used for both Learning and Testing your knowledge. Select the buttons below to enter one of these modes.</p>
        <br>
		
    <button id="learnButton">Learn</button>
    <button id="testButton">Test</button><br><br><br><br>
	
        <label for="responseOutput">Response:</label>
        <div id="responseOutput" class="response-output"></div>

        <label for="userInput">Request:</label>
        <input type="text" id="userInput" class="user-input" />
        <button id="sendButton">Send</button>
    </div>

<script>
       const baseURL = window.location.origin; 

        async function setCookie() {
            const response = await fetch(`${baseURL}/set-cookie/`, {
                method: 'GET',
                credentials: 'include'  // Include credentials (cookies) with the request
            });
            const data = await response.json();
            console.log(data.message);  // For debugging
        }

        // Call the setCookie function on page load
        window.onload = setCookie;

        document.getElementById('sendButton').addEventListener('click', async () => {
            const userInput = document.getElementById('userInput').value;
            const responseOutput = document.getElementById('responseOutput');

            const response = await fetch(`${baseURL}/chatbot/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: userInput }),
                credentials: 'include'  // Include credentials (cookies) with the request
            });

            if (response.ok) {
                const data = await response.json();
                const newResponse = data.text;
                // Convert URLs to clickable links
                const formattedUserInput = formatLinks(userInput);
                const formattedResponse = formatLinks(newResponse);

                // Append new response to existing content
                const userMessage = `<div class="user-message">User: ${formattedUserInput}</div>`;
                const botMessage = `<div class="bot-message">Bot: ${formattedResponse}</div>`;
                responseOutput.innerHTML += userMessage + botMessage;
            } else {
                console.error("Error:", response.status, response.statusText);
            }
        });

        function formatLinks(text) {
            const urlPattern = /(https?:\/\/[^\s]+)/g;
            return text.replace(urlPattern, '<a href="$1" target="_blank">$1</a>');
        }
    </script>
</body>
</html>
    """
    return html

def temp_html_v2():
    html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Teaching Chatbot</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <!-- Version 1.0.2 -->
    <div class="container">
        <div class="header">
            <h1>Project Management Learning Center</h1>
            <p>This site is used for both Learning and Testing your knowledge. Select the buttons below to enter one of these modes.</p>
            <button id="learnButton">Learn</button>
            <button id="testButton">Test</button>
        </div>
        <div class="chat-area">
            <label for="responseOutput">Response:</label>
            <div id="responseOutput" class="response-output"></div>

            <label for="userInput">Request:</label>
            <textarea id="userInput" class="user-input"></textarea>
            <button id="sendButton">Send</button>
        </div>
    </div>

<script>
       const baseURL = window.location.origin; 

        async function setCookie() {
            const response = await fetch(`${baseURL}/set-cookie/`, {
                method: 'GET',
                credentials: 'include'  // Include credentials (cookies) with the request
            });
            const data = await response.json();
            console.log(data.message);  // For debugging
        }

        // Call the setCookie function on page load
        window.onload = setCookie;

        async function sendMessage() {
            const userInputElement = document.getElementById('userInput');
            const userInput = userInputElement.value;
            const responseOutput = document.getElementById('responseOutput');

            const response = await fetch(`${baseURL}/chatbot/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: userInput }),
                credentials: 'include'  // Include credentials (cookies) with the request
            });

            if (response.ok) {
                const data = await response.json();
                const newResponse = data.text;
                // Convert URLs to clickable links
                const formattedUserInput = formatLinks(userInput);
                const formattedResponse = formatLinks(newResponse);
                const timestamp = new Date().toLocaleTimeString();

                // Append new response to existing content
                const userMessage = `<div class="user-message"><span class="message-text">User: ${formattedUserInput}</span><span class="timestamp">${timestamp}</span></div>`;
                const botMessage = `<div class="bot-message"><span class="message-text">Bot: ${formattedResponse}</span><span class="timestamp">${timestamp}</span></div>`;
                responseOutput.innerHTML += userMessage + botMessage;
                responseOutput.scrollTop = responseOutput.scrollHeight; // Scroll to the latest message

                // Clear the input field
                userInputElement.value = '';
                userInputElement.style.height = 'auto'; // Reset height after sending

                // Scroll to make the input box visible
                userInputElement.scrollIntoView({ behavior: 'smooth' });
            } else {
                console.error("Error:", response.status, response.statusText);
            }
        }

        document.getElementById('sendButton').addEventListener('click', sendMessage);
        document.getElementById('userInput').addEventListener('keypress', function(event) {
            if (event.key === 'Enter' && !event.shiftKey) {
                event.preventDefault();
                sendMessage();
            }
        });

        document.getElementById('userInput').addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = (this.scrollHeight) + 'px';
        });

        function formatLinks(text) {
            const urlPattern = /(https?:\/\/[^\s]+)/g;
            return text.replace(urlPattern, '<a href="$1" target="_blank">$1</a>');
        }
</script>
</body>
</html>

   """
    return html

def temp_html_v3():
    html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Teaching Chatbot</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <!-- Version 1.0.3 -->
    <div class="container">
        <div class="header">
            <h1>Project Management Learning Center</h1>
            <p>This site is used for both Learning and Testing your knowledge. Select the buttons below to enter one of these modes.</p>
        <br>
            /*<button id="learnButton">Learn</button>
            <button id="testButton">Test</button>*/
        </div>
        <div class="chat-area">
            <label for="responseOutput">Response:</label>
            <div id="responseOutput" class="response-output"></div>

            <label for="userInput">Request:</label>
            <div class="input-container">
			    <div id="thinkingIndicator" class="loader" style="display: none;"></div>
                <textarea id="userInput" class="user-input"></textarea>
            </div>
            <button id="sendButton">Send</button>
        </div>
    </div>

<script>
    const baseURL = window.location.origin; 

    async function setCookie() {
        const response = await fetch(`${baseURL}/set-cookie/`, {
            method: 'GET',
            credentials: 'include'  // Include credentials (cookies) with the request
        });
        const data = await response.json();
        console.log(data.message);  // For debugging
    }

    // Call the setCookie function on page load
    window.onload = setCookie;

    async function sendMessage() {
        const userInputElement = document.getElementById('userInput');
        const userInput = userInputElement.value;
        const responseOutput = document.getElementById('responseOutput');
        const thinkingIndicator = document.getElementById('thinkingIndicator');

        // Show the thinking indicator
        thinkingIndicator.style.display = 'block';

        const response = await fetch(`${baseURL}/chatbot/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: userInput }),
            credentials: 'include'  // Include credentials (cookies) with the request
        });

        // Hide the thinking indicator
        thinkingIndicator.style.display = 'none';

        if (response.ok) {
            const data = await response.json();
            const newResponse = data.text;
            // Convert URLs to clickable links
            const formattedUserInput = formatLinks(userInput);
            const formattedResponse = formatLinks(newResponse);
            const timestamp = new Date().toLocaleTimeString();

            // Append new response to existing content
            const userMessage = `<div class="user-message"><span class="message-text">User: ${formattedUserInput}</span><span class="timestamp">${timestamp}</span></div>`;
            const botMessage = `<div class="bot-message"><span class="message-text">Bot: ${formattedResponse}</span><span class="timestamp">${timestamp}</span></div>`;
            responseOutput.innerHTML += userMessage + botMessage;
            responseOutput.scrollTop = responseOutput.scrollHeight; // Scroll to the latest message

            // Clear the input field
            userInputElement.value = '';
            userInputElement.style.height = 'auto'; // Reset height after sending

            // Scroll to make the input box visible
            userInputElement.scrollIntoView({ behavior: 'smooth' });
        } else {
            console.error("Error:", response.status, response.statusText);
        }
    }

    document.getElementById('sendButton').addEventListener('click', sendMessage);
    document.getElementById('userInput').addEventListener('keypress', function(event) {
        if (event.key === 'Enter' && !event.shiftKey) {
            event.preventDefault();
            sendMessage();
        }
    });

    document.getElementById('userInput').addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = (this.scrollHeight) + 'px';
    });

    function formatLinks(text) {
        const urlPattern = /(https?:\/\/[^\s]+)/g;
        return text.replace(urlPattern, '<a href="$1" target="_blank">$1</a>');
    }
</script>
</body>
</html>


   """
    return html

def temp_html_v4():
    html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Teaching Chatbot</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <!-- Version 1.0.4 -->
    <div class="container">
        <div class="header">
            <h1>Project Management Learning Center</h1>
            <p>Select your class from the dropdown below and then select the lesson you would like to work on.</p>
            <br>
            <div>
                <label for="classDropdown">Class:</label>
                <select id="classDropdown" onchange="fetchLessons()">
                    <option value="">Select a class</option>
                </select>

                <label for="lessonDropdown">Lesson:</label>
                <select id="lessonDropdown">
                    <option value="">Select a lesson</option>
                </select>
            </div>
        </div>
        <br>
        <br>
        <div class="chat-area">
            <label for="responseOutput">Response:</label>
            <div id="responseOutput" class="response-output"></div>

            <label for="userInput">Request:</label>
            <div class="input-container">
                <div id="thinkingIndicator" class="loader" style="display: none;"></div>
                <textarea id="userInput" class="user-input"></textarea>
            </div>
            <button id="sendButton">Send</button>
        </div>
    </div>

    <script>
        const baseURL = window.location.origin;

        async function setCookie() {
            const response = await fetch(`${baseURL}/set-cookie/`, {
                method: 'GET',
                credentials: 'include'  // Include credentials (cookies) with the request
            });
            const data = await response.json();
            console.log(data.message);  // For debugging
        }

        async function fetchClasses() {
            const response = await fetch(`${baseURL}/classes/`, {
                method: 'GET',
                credentials: 'include'  // Include credentials (cookies) with the request
            });

            if (response.ok) {
                const data = await response.json();
                const classDropdown = document.getElementById('classDropdown');

                // Clear existing options
                classDropdown.innerHTML = '<option value="">Select a class</option>';

                data.directories.forEach(classItem => {
                    const option = document.createElement('option');
                    option.value = classItem; // Use the directory name as the value
                    option.textContent = classItem; // Use the directory name as the text
                    classDropdown.appendChild(option);
                });
            } else {
                console.error("Error fetching classes:", response.status, response.statusText);
            }
        }

        async function fetchLessons() {
            const classDropdown = document.getElementById('classDropdown');
            const selectedClassId = classDropdown.value;
        
            const lessonDropdown = document.getElementById('lessonDropdown');
            lessonDropdown.innerHTML = '<option value="">Select a lesson</option>';  // Reset lesson dropdown
        
            if (selectedClassId) {
                const response = await fetch(`${baseURL}/classes/${selectedClassId}/conundrums/`, {
                    method: 'GET',
                    credentials: 'include'  // Include credentials (cookies) with the request
                });
        
                if (response.ok) {
                    const data = await response.json();
                    data.files.forEach(lesson => {  // Use data.files to get the list of files
                        const option = document.createElement('option');
                        option.value = lesson;  // Use the file name as the value
                        option.textContent = lesson;  // Use the file name as the text
                        lessonDropdown.appendChild(option);
                    });
                } else {
                    console.error("Error fetching lessons:", response.status, response.statusText);
                }
            }
        }


        // Call the setCookie and fetchClasses functions on page load
        window.onload = () => {
            setCookie();
            fetchClasses();
        };

        async function sendMessage() {
            const userInputElement = document.getElementById('userInput');
            const userInput = userInputElement.value;
            const responseOutput = document.getElementById('responseOutput');
            const thinkingIndicator = document.getElementById('thinkingIndicator');

            // Show the thinking indicator
            thinkingIndicator.style.display = 'block';

            const response = await fetch(`${baseURL}/chatbot/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: userInput }),
                credentials: 'include'  // Include credentials (cookies) with the request
            });

            // Hide the thinking indicator
            thinkingIndicator.style.display = 'none';

            if (response.ok) {
                const data = await response.json();
                const newResponse = data.text;
                // Convert URLs to clickable links
                const formattedUserInput = formatLinks(userInput);
                const formattedResponse = formatLinks(newResponse);
                const timestamp = new Date().toLocaleTimeString();

                // Append new response to existing content
                const userMessage = `<div class="user-message"><span class="message-text">User: ${formattedUserInput}</span><span class="timestamp">${timestamp}</span></div>`;
                const botMessage = `<div class="bot-message"><span class="message-text">Bot: ${formattedResponse}</span><span class="timestamp">${timestamp}</span></div>`;
                responseOutput.innerHTML += userMessage + botMessage;
                responseOutput.scrollTop = responseOutput.scrollHeight; // Scroll to the latest message

                // Clear the input field
                userInputElement.value = '';
                userInputElement.style.height = 'auto'; // Reset height after sending

                // Scroll to make the input box visible
                userInputElement.scrollIntoView({ behavior: 'smooth' });
            } else {
                console.error("Error:", response.status, response.statusText);
            }
        }

        document.getElementById('sendButton').addEventListener('click', sendMessage);
        document.getElementById('userInput').addEventListener('keypress', function(event) {
            if (event.key === 'Enter' && !event.shiftKey) {
                event.preventDefault();
                sendMessage();
            }
        });

        document.getElementById('userInput').addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = (this.scrollHeight) + 'px';
        });

        function formatLinks(text) {
            const urlPattern = /(https?:\/\/[^\s]+)/g;
            return text.replace(urlPattern, '<a href="$1" target="_blank">$1</a>');
        }

    </script>
</body>
</html>



   """
    return html

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
    <!-- Main container for the application -->
    <div class="container">
        <!-- Header section with title and instructions -->
        <div class="header">
            <h1>Project Management Learning Center</h1>
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
        <br>
        <br>
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
            <!-- Send button for submitting requests -->
            <button id="sendButton">Send</button>
        </div>
    </div>

    <!-- Scripts for dynamic behavior and data fetching -->
    <script>
        const baseURL = window.location.origin;
        let selectedClassId = null;  // Track selected class ID for requests
        const classDropdown = document.getElementById('classDropdown'); // Globally accessible dropdown element

        // Set a cookie on the client for session management
        async function setCookie() {
            const response = await fetch(`${baseURL}/set-cookie/`, {
                method: 'GET',
                credentials: 'include'
            });
            const data = await response.json();
            console.log(data.message);
        }

        // Fetch class options from server
        async function fetchClasses() {
            const response = await fetch(`${baseURL}/classes/`, {
                method: 'GET',
                credentials: 'include'
            });

            if (response.ok) {
                const data = await response.json();
                classDropdown.innerHTML = '<option value="">Select a class</option>';
                data.directories.forEach(classItem => {
                    const option = document.createElement('option');
                    option.value = classItem;
                    option.textContent = classItem;
                    classDropdown.appendChild(option);
                });
            } else {
                console.error("Error fetching classes:", response.status, response.statusText);
            }
        }

        // Fetch lessons based on selected class
        async function fetchLessons() {
            const lessonDropdown = document.getElementById('lessonDropdown');
            lessonDropdown.innerHTML = '<option value="">Select a lesson</option>';
        
            if (selectedClassId) {
                const response = await fetch(`${baseURL}/classes/${selectedClassId}/conundrums/`, {
                    method: 'GET',
                    credentials: 'include'
                });
        
                if (response.ok) {
                    const data = await response.json();
                    data.files.forEach(lesson => {
                        const option = document.createElement('option');
                        option.value = lesson;
                        option.textContent = lesson;
                        lessonDropdown.appendChild(option);
                    });
                } else {
                    console.error("Error fetching lessons:", response.status, response.statusText);
                }
            }
        }

        // Initial setup on page load
        document.addEventListener('DOMContentLoaded', () => {
            setCookie();
            fetchClasses();
        });

        // Handling message sending from chat interface
        async function sendMessage() {
            const userInputElement = document.getElementById('userInput');
            const userInput = userInputElement.value;
            const responseOutput = document.getElementById('responseOutput');
            const thinkingIndicator = document.getElementById('thinkingIndicator');

            thinkingIndicator.style.display = 'block';

            const response = await fetch(`${baseURL}/chatbot/`, {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ text: userInput }),
                credentials: 'include'
            });

            thinkingIndicator.style.display = 'none';

            if (response.ok) {
                const data = await response.json();
                const newResponse = data.text;
                const formattedUserInput = formatLinks(userInput);
                const formattedResponse = formatLinks(newResponse);
                const timestamp = new Date().toLocaleTimeString();

                const userMessage = `<div class="user-message"><span class="message-text">User: ${formattedUserInput}</span><span class="timestamp">${timestamp}</span></div>`;
                const botMessage = `<div class="bot-message"><span class="message-text">Bot: ${formattedResponse}</span><span the_timestamp="${timestamp}"></span></div>`;
                responseOutput.innerHTML += userMessage + botMessage;
                responseOutput.scrollTop = responseOutput.scrollHeight;

                userInputElement.value = '';
                userInputElement.style.height = 'auto';
                userInputElement.scrollIntoView({ behavior: 'smooth' });
            } else {
                console.error("Error:", response.status, response.statusText);
            }
        }

        // Additional event listeners for UI interactions
        document.getElementById('sendButton').addEventListener('click', sendMessage);
        document.getElementById('userInput').addEventListener('keypress', function(event) {
            if (event.key === 'Enter' && !event.shiftKey) {
                event.preventDefault();
                sendMessage();
            }
        });

        document.getElementById('userInput').addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = (this.scrollHeight) + 'px';
        });

        // Utility function to format links within text
        function formatLinks(text) {
            const urlPattern = /(https?:\/\/[^\s]+)/g;
            return text.replace(urlPattern, '<a href="$1" target="_blank">$1</a>');
        }

        // Event listener for class selection to manage class ID and load lessons
        document.getElementById('classDropdown').addEventListener('change', function() {
            if (!this.value) {
                console.warn('No class selected. Please select a class.');
                return; // Avoid executing fetchLessons if no class is selected
            }
            console.log('Class Selected');
            selectedClassId = this.value; // Update global variable upon change
            fetchLessons(); // Then fetch lessons based on the new class ID
        });
        
        document.getElementById('lessonDropdown').addEventListener('change', async function() {
            console.log('Lesson dropdown changed'); // Check if this log appears in the console
            const selectedLesson = this.value;
            const currentLessonName = document.getElementById('currentLessonName');
        
            if (selectedLesson) {
                const response = await fetch(`${baseURL}/classes/${selectedClassId}/conundrums/${selectedLesson}`, {
                    method: 'GET',
                    credentials: 'include'
                });
        
                if (response.ok) {
                    const lessonContent = await response.text();
                    sessionStorage.setItem('currentLesson', lessonContent);
                    lessonNameDisplay.textContent = 'Loaded Lesson: ' + selectedLesson;
                } else {
                    console.error("Error fetching lesson content:", response.status, response.statusText);
                    lessonNameDisplay.textContent = 'Failed to load lesson';
                }
            } else {
                currentLessonName.textContent = 'No lesson selected';
            }
        });

    </script>
</body>
</html>



   """
    return html