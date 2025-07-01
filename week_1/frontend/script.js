// js/script.js

// Target node to observe
const targetNode = document.getElementById('watched-area');

// Callback function for MutationObserver
const callback = function (mutationsList, observer) {
  for (const mutation of mutationsList) {
    if (mutation.type === 'childList') {
      const logData = {
        type: mutation.type,
        addedNodes: [...mutation.addedNodes].map(node => node.outerHTML || node.textContent),
        timestamp: new Date().toISOString()
      };
      //  Log it in the browser console 
       console.log("Log sent:", logData);
      // Send DOM change log to backend
      fetch('http://localhost:8000/api/dom-log', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(logData),
      })
      .then(response => response.json())
      .then(data => console.log('Success:', data))
      .catch(error => console.error('Error:', error));
    }
  }
};

// Create and start observer
const observer = new MutationObserver(callback);
observer.observe(targetNode, { childList: true, subtree: true });

// Simulate DOM change on button click
function addElement() {
  const newElement = document.createElement('p');
  newElement.textContent = 'New paragraph at ' + new Date().toLocaleTimeString();
  targetNode.appendChild(newElement);
}
