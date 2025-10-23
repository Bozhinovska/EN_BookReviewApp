function searchBooks() {
    let input = document.getElementById('search-input').value.toLowerCase();
    let books = document.getElementsByClassName('book-item');

    Array.from(books).forEach(book => {
        let title = book.querySelector('.book-title').textContent.toLowerCase();
        if (title.includes(input)) {
            book.style.display = '';
        } else {
            book.style.display = 'none';
        }
    });
}
function showEditForm(button) {
            var reviewId = button.getAttribute('data-review-id');
            var editForm = document.getElementById('edit-form-' + reviewId);
            if (editForm.style.display === 'none') {
                editForm.style.display = 'block';
            } else {
                editForm.style.display = 'none';
            }
}
function validateLoginForm() {
            var email = document.getElementById('email').value;
            var password = document.getElementById('password').value;

            if (email === '') {
                alert('Please enter an E-mail');
                return false;
            }

            if (password === '') {
                alert('Please enter a password');
                return false;
            }


            var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailPattern.test(email)) {
                alert('Please enter a valid e-mail');
                return false;
            }

            return true;
        }

        function validateRegisterForm() {
            var name = document.getElementById('name').value;
            var surname = document.getElementById('surname').value;
            var email = document.getElementById('email').value;
            var password = document.getElementById('password').value;
            var confirmPassword = document.getElementById('confirm_password').value;

            if (name === '' || surname === '' || email === '' || password === '' || confirmPassword === '') {
                alert('Every field is required');
                return false;
            }

            var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailPattern.test(email)) {
                alert('Please enter a valid e-mail');
                return false;
            }

            if (password !== confirmPassword) {
                alert('Passwords does not match');
                return false;
            }

            if (password.length < 6) {
                alert('Password must have at least 6 characters');
                return false;
            }

            return true;
}
