// Função para validar a senha do cadastro
function validarSenha() {
    var password = document.getElementById('senha').value
    var confirm_password = document.getElementById('confirmar_senha').value
    // Verificar o tamanho da senha 
    if (password.length < 6) {
        alert('A senha deve ter pelo menos 6 dígitos.')
        return false
    }
    // Verificar se a senha possui uma letra maiúscula, um número e um caractere especial.
    var uppercaseRegex = /[A-Z]/;
    var numberRegex = /[0-9]/;
    var specialRegex = /[!|@|#|$|%|^|&|*|(|)|-|_]/;
    if (!uppercaseRegex.test(password) || !numberRegex.test(password) || !specialRegex.test(password)) {
        alert('A senha deve conter pelo menos uma letra maiúscula, um número e um caractere especial.')
        return false
    }
    // Verificar se os campos senha e confirmação de senha tem valores iguais
    if (password != confirm_password) {
        alert('As senhas não são iguais.')
        return false
    }
    return true
}