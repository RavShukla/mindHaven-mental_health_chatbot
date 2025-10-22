// signup.js

document.addEventListener("DOMContentLoaded", () => {
  console.log("MindHaven Sign-Up Page Loaded");

  const form = document.querySelector("form");
  const nameInput = document.getElementById("name");
  const emailInput = document.getElementById("email");
  const passwordInput = document.getElementById("password");

  // ======== Form Submission Handler ========
  form.addEventListener("submit", (event) => {
    event.preventDefault(); // Prevent page reload

    const name = nameInput.value.trim();
    const email = emailInput.value.trim();
    const password = passwordInput.value.trim();

    // ======== Validation ========
    if (!name || !email || !password) {
      alert("⚠️ Please fill in all fields before continuing.");
      return;
    }

    if (!validateEmail(email)) {
      alert("📧 Please enter a valid email address.");
      return;
    }

    if (password.length < 6) {
      alert("🔒 Password must be at least 6 characters long.");
      return;
    }

    // ======== Simulate Sign-Up Success ========
    console.log("User Registered:", { name, email });

    alert(`🎉 Welcome ${name}! Your account has been created successfully.`);

    // Redirect to dashboard (same folder)
    window.location.href = "dashboard.html";

  });

  // Simple email validation helper
  function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
  }

});
