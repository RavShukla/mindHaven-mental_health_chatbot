// index.js

// Wait for DOM to load
document.addEventListener("DOMContentLoaded", () => {
  console.log("MindHaven homepage loaded successfully.");

  // ====== Button Navigation ======
  const signupBtn = document.getElementById("signup");
  const loginBtn = document.getElementById("login");

  if (signupBtn) {
    signupBtn.addEventListener("click", () => {
      window.location.href = "signup.html";
    });
  }

  if (loginBtn) {
    loginBtn.addEventListener("click", () => {
      window.location.href = "login.html";
    });
  }

  // ====== Subtle Animation on Objective Text ======
  const objectiveText = document.getElementById("objectiveText");
  if (objectiveText) {
    objectiveText.style.opacity = "0";
    objectiveText.style.transition = "opacity 1.5s ease-in-out";

    setTimeout(() => {
      objectiveText.style.opacity = "1";
    }, 300);
  }

});
