// chatbot.js

// Function to handle the form submission
function submitQuery() {
  const form = document.getElementById('chat-form');
  const queryInput = document.getElementById('user-query');
  const responseDiv = document.getElementById('response-div');

  const query = queryInput.value;

  fetch('/api/chatbot/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCookie('csrftoken'),
    },
    body: JSON.stringify({ query }),
  })
    .then(response => response.json())
    .then(data => {
      responseDiv.innerText = data.response;
    })
    .catch(error => {
      console.error('Error:', error);
      responseDiv.innerText = 'Error occurred while processing the request.';
    });
}

// Function to display the response in the chat log
function displayResponse(response) {
  var chatLog = document.getElementById('chat-log');
  var responseElement = document.createElement('p');
  responseElement.textContent = response;
  chatLog.appendChild(responseElement);
}

// Function to get the CSRF token from the cookie
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + '=') {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// Add an event listener to submit the form on button click
const submitButton = document.getElementById('submit-btn');
submitButton.addEventListener('click', submitQuery);