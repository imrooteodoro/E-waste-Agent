function toggleChat() {
    var chatbot = document.getElementById("chatbot");
    chatbot.style.display = chatbot.style.display === "block" ? "none" : "block";
  }

  function typeMessage(element, message) {
    let index = 0;
    element.innerHTML = "";
    const span = document.createElement('span');
    element.appendChild(span);

    function addChar() {
      if (index < message.length) {
        span.innerHTML += message.charAt(index);
        index++;
        setTimeout(addChar, 0.1);
        var chatBody = document.getElementById("chatBody");
        chatBody.scrollTop = chatBody.scrollHeight;
      } else {
        element.innerHTML = message;
      }
    }
    addChar();
  }

  function sendMessage() {
    let userInput = document.getElementById("userInput").value.trim();
    let chatBody = document.getElementById("chatBody");
    let sendBtn = document.getElementById("sendBtn");

    if (userInput === "") return;

    sendBtn.disabled = true;

    let userMessage = document.createElement("div");
    userMessage.className = "message user-message";
    userMessage.textContent = userInput;
    chatBody.appendChild(userMessage);


    //Endpoint ou url post do Bot
    const postEndpoint = ''

    fetch(`${postEndpoint}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ user_message: userInput })
    })
      .then(response => response.json())
      .then(data => {
        let botMessage = document.createElement("div");
        botMessage.className = "message bot-message";
        chatBody.appendChild(botMessage);
        typeMessage(botMessage, data.bot_response);
      })
      .catch(error => {
        console.error('Erro:', error);
        sendBtn.disabled = false;
      });

    document.getElementById("userInput").value = "";
  }

  document.getElementById("userInput").addEventListener("input", function() {
    let sendBtn = document.getElementById("sendBtn");
    sendBtn.disabled = !this.value.trim();
  });

  document.getElementById("userInput").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
      event.preventDefault();
      sendMessage(); 
    }
  });

//Endpoint Get para obter informações do bot  
  const GetEndpoint = ''

  async function fetchAbout() {
    const aboutEndpoint = `${GetEndpoint}`;
    const aboutContent = document.getElementById('aboutContent');

    try {
      const response = await fetch(aboutEndpoint);
      if (!response.ok) {
        aboutContent.textContent = 'Erro ao carregar informações: ' + response.statusText;
        console.error('Erro ao fazer a requisição:', response.statusText);
        return;
      }

      const data = await response.json();
      aboutContent.textContent = JSON.stringify(data, null, 2); 
      console.log('Resposta do /about:', data);
    } catch (error) {
      aboutContent.textContent = 'Erro de conexão.';
      console.error('Erro de conexão:', error);
    }
  }

  setInterval(fetchAbout, 20000);

  fetchAbout();