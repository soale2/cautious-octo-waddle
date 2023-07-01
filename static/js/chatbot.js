// chatbot.js

// Function to handle the form submission
function submitQuery() {
    var userInput = document.getElementById('user-query').value;
    var csrfToken = getCookie('csrftoken');  // Retrieve the CSRF token using the getCookie function

    fetch('/api/chatbot/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({
            query: userInput,
        }),
    })
    .then(function (response) {
        return response.json();
    })
    .then(function (data) {
        displayResponse(data.response);
    })
    .catch(function (error) {
        console.error('Error:', error);
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
  