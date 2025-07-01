// week_1 (previous week) - MutationObserver setup & send logs
const targetNode = document.getElementById('watched-area');

const callback = function(mutationsList, observer) {
  for (const mutation of mutationsList) {
    if (mutation.type === 'childList') {
      const logData = {
        website_id: 1,
        mutations: [mutation.type],
        addedNodes: [...mutation.addedNodes].map(node => node.outerHTML || node.textContent),
        timestamp: new Date().toISOString(),

        // week_2 (this week) - classify logs as normal or suspicious randomly
        type: isSuspicious() ? "suspicious" : "normal"
      };
      console.log("Log sent:", logData);
      fetch('http://localhost:8000/api/dom-log', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(logData),
      })
      .then(response => response.json())
      .then(data => console.log('✅ Success:', data))
      .catch(error => console.error('❌ Error:', error));
    }
  }
};

const observer = new MutationObserver(callback);
observer.observe(targetNode, { childList: true, subtree: true });

// week_1 - simulate DOM changes on button click
function addElement() {
  const newElement = document.createElement('p');
  newElement.textContent = 'New paragraph at ' + new Date().toLocaleTimeString();
  targetNode.appendChild(newElement);
}

// week_2 - random suspicious flag generator
function isSuspicious() {
  return Math.random() < 0.5;
}
