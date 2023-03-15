const form = document.querySelector('form');
const username = document.getElementById('username');
const email = document.getElementById('email');
const password = document.getElementById('password');
const password2 = document.getElementById('confirm_password');

form.addEventListener('submit', (event) => {
  if (password.value !== password2.value) {
    event.preventDefault();
    alert('Passwords do not match');
  }
});
