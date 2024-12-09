document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const senha = document.getElementById('senha');
    const confirmacaoSenha = document.getElementById('confirmacao_senha');
    
    form.addEventListener('submit', function (event) {
        if (senha.value !== confirmacaoSenha.value) {
            alert('As senhas não coincidem!');
            event.preventDefault();
        }
    });
});
