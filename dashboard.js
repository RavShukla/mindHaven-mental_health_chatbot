// Add simple in-page prompt UI (or incorporate into your analysis.html)
function openChatPrompt() {
  const userText = prompt("How are you feeling today? (type a few sentences)");
  if (!userText) return;

  fetch("http://localhost:5000/api/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text: userText })
  })
  .then(res => res.json())
  .then(data => {
    if (data.error) {
      alert("Error: " + data.error);
      return;
    }
    alert("AI Reply:\n\n" + data.reply + "\n\nMood detected: " + data.mood.label + " (polarity: " + data.mood.polarity.toFixed(2) + ")");
    // optionally open the mood plot in a new tab:
    window.open("http://localhost:5000/api/plot", "_blank");
  })
  .catch(err => {
    console.error(err);
    alert("Failed to contact backend. Is it running?");
  });
}

// bind to widget click (for your existing dashboard widgets)
document.addEventListener("DOMContentLoaded", () => {
  const widgets = document.querySelectorAll(".widget");
  if (widgets && widgets[1]) {
    widgets[1].addEventListener("click", (e) => {
      e.preventDefault();
      openChatPrompt();
    });
  }
});
s