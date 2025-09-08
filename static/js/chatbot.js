// Minimal chatbot frontend logic
(function(){
  function qs(selector){ return document.querySelector(selector); }

  // support both id namespaces
  const chatBtn = qs('#chat-toggle-btn') || qs('#ai-chatbot-button');
  const chatPanel = qs('#chat-panel') || qs('#ai-chatbot-box');
  const chatClose = qs('#chat-close') || qs('#ai-chatbot-close');
  const chatForm = qs('#chat-form') || qs('#ai-chat-form');
  const chatInput = qs('#chat-input') || qs('#ai-query');
  const chatBody = qs('#chat-body') || qs('#ai-chatbot-messages');
  const summarizeForm = qs('#ai-summarize-form');

  if(!chatBtn) return; // nothing to do

  // Semester card click handlers
  document.querySelectorAll('.semester-card').forEach(card => {
    card.addEventListener('click', function() {
      const url = this.getAttribute('data-url');
      if (url) {
        window.location.href = url;
      }
    });
  });

  chatBtn.addEventListener('click', ()=> { if(chatPanel) chatPanel.classList.toggle('open'); });
  if(chatClose && chatPanel) chatClose.addEventListener('click', ()=> chatPanel.classList.remove('open'));

  function appendMessage(role, text){
    if(!chatBody) return;
    const msg = document.createElement('div');
    msg.className = 'chat-msg ' + (role === 'user' ? 'user' : 'bot');
    chatBody.appendChild(msg);
    // type-out bot responses word-by-word for smoothness
    if(role === 'bot'){
      const words = String(text).split(/(\s+)/);
      let i = 0;
      msg.textContent = '';
      function step(){
        if(i >= words.length) { chatBody.scrollTop = chatBody.scrollHeight; return; }
        msg.textContent += words[i];
        i++;
        chatBody.scrollTop = chatBody.scrollHeight;
  setTimeout(step, 25); // faster, snappier word-by-word typing
      }
      step();
    } else {
      msg.textContent = text;
      chatBody.scrollTop = chatBody.scrollHeight;
    }
  }


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

  if(chatForm){
    chatForm.addEventListener('submit', async (e)=>{
      e.preventDefault();
      const query = (chatInput && chatInput.value || '').trim();
      if(!query) return;
      appendMessage('user', query);
      if(chatInput) chatInput.value = '';
      // Streaming response
      const msg = document.createElement('div');
      msg.className = 'chat-msg bot';
      chatBody.appendChild(msg);
      chatBody.scrollTop = chatBody.scrollHeight;
      await streamToAI('/ai/search', { query }, chunk => {
        msg.textContent += chunk;
        chatBody.scrollTop = chatBody.scrollHeight;
      });
    });
  }

  if(summarizeForm){
    summarizeForm.addEventListener('submit', async (e)=>{
      e.preventDefault();
      const sel = qs('#ai-summary-semester');
      if(!sel) return;
      const semester = sel.value;
      appendMessage('user', 'Summarize semester ' + semester);
      // Streaming response
      const msg = document.createElement('div');
      msg.className = 'chat-msg bot';
      chatBody.appendChild(msg);
      chatBody.scrollTop = chatBody.scrollHeight;
      await streamToAI('/ai/summarize', { semester }, chunk => {
        msg.textContent += chunk;
        chatBody.scrollTop = chatBody.scrollHeight;
      });
    });
  }

})();
