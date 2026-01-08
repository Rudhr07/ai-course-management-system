// AI Course Management - Chatbot Frontend Logic
(function(){
  function qs(selector){ return document.querySelector(selector); }

  // Support both id namespaces
  const chatBtn = qs('#chat-toggle-btn') || qs('#ai-chatbot-button');
  const chatPanel = qs('#chat-panel') || qs('#ai-chatbot-box');
  const chatClose = qs('#chat-close') || qs('#ai-chatbot-close');
  const chatForm = qs('#chat-form') || qs('#ai-chat-form');
  const chatInput = qs('#chat-input') || qs('#ai-query');
  const chatBody = qs('#chat-body') || qs('#ai-chatbot-messages');
  const summarizeForm = qs('#ai-summarize-form');

  if(!chatBtn) return; // Nothing to do

  // Semester card click handlers
  document.querySelectorAll('.semester-card').forEach(card => {
    card.addEventListener('click', function(e) {
      // Don't navigate if clicking the button inside
      if (e.target.closest('a')) return;
      const url = this.getAttribute('data-url');
      if (url) {
        window.location.href = url;
      }
    });
  });

  // Toggle chat panel
  chatBtn.addEventListener('click', () => { 
    if(chatPanel) chatPanel.classList.toggle('open'); 
  });
  
  if(chatClose && chatPanel) {
    chatClose.addEventListener('click', () => chatPanel.classList.remove('open'));
  }

  // Create message element with proper styling
  function createMessage(role, text) {
    const msg = document.createElement('div');
    msg.className = 'chat-msg ' + (role === 'user' ? 'user' : 'bot');
    return msg;
  }

  // Append message to chat body
  function appendMessage(role, text){
    if(!chatBody) return;
    const msg = createMessage(role, text);
    chatBody.appendChild(msg);
    
    if(role === 'bot'){
      // Type-out bot responses word-by-word
      const words = String(text).split(/(\s+)/);
      let i = 0;
      msg.textContent = '';
      function step(){
        if(i >= words.length) { 
          chatBody.scrollTop = chatBody.scrollHeight; 
          return; 
        }
        msg.textContent += words[i];
        i++;
        chatBody.scrollTop = chatBody.scrollHeight;
        setTimeout(step, 20);
      }
      step();
    } else {
      msg.textContent = text;
      chatBody.scrollTop = chatBody.scrollHeight;
    }
    
    return msg;
  }

  // Create typing indicator
  function createTypingIndicator() {
    const indicator = document.createElement('div');
    indicator.className = 'typing-indicator';
    indicator.innerHTML = '<span></span><span></span><span></span>';
    return indicator;
  }

  // Stream AI response
  async function streamToAI(path, payload, onChunk){
    const resp = await fetch(path, {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams(payload)
    });
    if(!resp.body) return;
    const reader = resp.body.getReader();
    const decoder = new TextDecoder();
    let done = false;
    let buffer = '';
    while(!done){
      const {value, done: doneReading} = await reader.read();
      done = doneReading;
      if(value){
        const chunk = decoder.decode(value);
        buffer += chunk;
        if(onChunk) onChunk(chunk);
      }
    }
    return buffer;
  }

  // Handle chat form submission
  if(chatForm){
    chatForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const query = (chatInput && chatInput.value || '').trim();
      if(!query) return;
      
      // Add user message
      appendMessage('user', query);
      if(chatInput) chatInput.value = '';
      
      // Add typing indicator
      const typingIndicator = createTypingIndicator();
      chatBody.appendChild(typingIndicator);
      chatBody.scrollTop = chatBody.scrollHeight;
      
      // Create bot message container
      const msg = createMessage('bot', '');
      
      try {
        // Remove typing indicator and add message container
        typingIndicator.remove();
        chatBody.appendChild(msg);
        chatBody.scrollTop = chatBody.scrollHeight;
        
        // Stream the response
        await streamToAI('/ai/search', { query }, chunk => {
          msg.textContent += chunk;
          chatBody.scrollTop = chatBody.scrollHeight;
        });
      } catch (error) {
        typingIndicator.remove();
        msg.textContent = 'Sorry, I encountered an error. Please try again.';
        chatBody.appendChild(msg);
      }
    });
  }

  // Handle summarize form submission
  if(summarizeForm){
    summarizeForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const sel = qs('#ai-summary-semester');
      if(!sel || !sel.value) return;
      
      const semester = sel.value;
      appendMessage('user', 'Summarize semester ' + semester);
      
      // Add typing indicator
      const typingIndicator = createTypingIndicator();
      chatBody.appendChild(typingIndicator);
      chatBody.scrollTop = chatBody.scrollHeight;
      
      // Create bot message container
      const msg = createMessage('bot', '');
      
      try {
        // Remove typing indicator and add message container
        typingIndicator.remove();
        chatBody.appendChild(msg);
        chatBody.scrollTop = chatBody.scrollHeight;
        
        // Stream the response
        await streamToAI('/ai/summarize', { semester }, chunk => {
          msg.textContent += chunk;
          chatBody.scrollTop = chatBody.scrollHeight;
        });
      } catch (error) {
        typingIndicator.remove();
        msg.textContent = 'Sorry, I encountered an error. Please try again.';
        chatBody.appendChild(msg);
      }
      
      // Reset select
      sel.value = '';
    });
  }

})();
