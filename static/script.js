// script.js

function togglePassword(inputId) {
    var passwordInput = document.getElementById(inputId);
    var passwordToggle = document.querySelector(`#${inputId} + .password-toggle`);

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        passwordToggle.textContent = "Hide";
    } else {
        passwordInput.type = "password";
        passwordToggle.textContent = "Show";
    }
}

document.addEventListener("DOMContentLoaded", function () {
    var registerForm = document.getElementById("registerForm");

    registerForm.addEventListener("submit", function (event) {
        // Handle form submission, e.g., send data to the server
        event.preventDefault();
        alert("Registration successful!"); // Placeholder for form submission handling
    });
});
