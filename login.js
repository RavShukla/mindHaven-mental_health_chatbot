// login.js

document.addEventListener("DOMContentLoaded", () => {
  console.log("MindHaven Login Page Loaded");

  const loginForm = document.getElementById("loginForm");
  const emailInput = document.getElementById("username");
  const passwordInput = document.getElementById("password");

  // ======== Handle Form Submit ========
  loginForm.addEventListener("submit", (event) => {
    event.preventDefault();

    const email = emailInput.value.trim();
    const password = passwordInput.value.trim();

    // ======== Basic Validation ========
    if (!email || !password) {
      alert("⚠️ Please fill out both email and password.");
      return;
    }

    if (!validateEmail(email)) {
      alert("📧 Please enter a valid email address.");
      return;
    }

    // ======== Simulated Login Success ========
    // In a real project, you’d make an API call here (e.g., fetch or axios)
    console.log("Logging in with:", email);

    alert("✅ Login successful! Redirecting to your dashboard...");
    setTimeout(() => {
      window.location.href = "html/dashboard.html";
    }, 800);
  });

  // ======== Forgot Password Link ========
  const forgotLink = document.querySelector(".footer-link[href='#']");
  if (forgotLink) {
    forgotLink.addEventListener("click", (e) => {
      e.preventDefault();
      alert("🔑 Password recovery feature coming soon!");
    });
  }

  // ======== Email Validation Function ========
  function validateEmail(email) {
    const pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
    return pattern.test(email);
  }
});
