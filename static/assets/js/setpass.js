
    const passwordInput = document.getElementById('floatingInputPassword');
    const eyeSlashIcon = document.getElementById('eyeSlashIcon');
    const eyeIcon = document.getElementById('eyeIcon');
document.addEventListener('DOMContentLoaded', function() {
    eyeSlashIcon.addEventListener('click', function() {
        if (passwordInput.type === 'password') {
            passwordInput.type = 'text';
            eyeSlashIcon.classList.add('d-none');
            eyeIcon.classList.remove('d-none');
           
        
        }
    });
    eyeIcon.addEventListener('click', function() {
        if (passwordInput.type === 'text') {
            passwordInput.type = 'password';
            eyeSlashIcon.classList.remove('d-none');
            eyeIcon.classList.add('d-none');
            
        }
    });
});


const passwordConfirmUpdateInput = document.getElementById('inputUserPasswordConfirmUpdate');
const passwordUpdateInput = document.getElementById('inputUserPasswordUpdate');
const eyeSlashIconUpdate = document.getElementById('eyeSlashIconUpdate');
const eyeIconUpdate = document.getElementById('eyeIconUpdate');
const eyeSlashIconConfirmUpdate = document.getElementById('eyeSlashIconConfirmUpdate');
const eyeIconConfirmUpdate = document.getElementById('eyeIconConfirmUpdate');
document.addEventListener('DOMContentLoaded', function() {
    eyeSlashIconConfirmUpdate.addEventListener('click', function() {
        if (passwordConfirmUpdateInput.type === 'password') {
            passwordConfirmUpdateInput.type = 'text';
            eyeSlashIconConfirmUpdate.classList.add('d-none');
            eyeIconConfirmUpdate.classList.remove('d-none');
           
        
        }
    });
    eyeIconConfirmUpdate.addEventListener('click', function() {
        if (passwordConfirmUpdateInput.type === 'text') {
            passwordConfirmUpdateInput.type = 'password';
            eyeSlashIconConfirmUpdate.classList.remove('d-none');
            eyeIconConfirmUpdate.classList.add('d-none');
            
        }
    });

    eyeSlashIconUpdate.addEventListener('click', function() {
        if (passwordUpdateInput.type === 'password') {
            passwordUpdateInput.type = 'text';
            eyeSlashIconUpdate.classList.add('d-none');
            eyeIconUpdate.classList.remove('d-none');
           
        
        }
    });
    eyeIconUpdate.addEventListener('click', function() {
        if (passwordUpdateInput.type === 'text') {
            passwordUpdateInput.type = 'password';
            eyeSlashIconUpdate.classList.remove('d-none');
            eyeIconUpdate.classList.add('d-none');
            
        }
    });
});