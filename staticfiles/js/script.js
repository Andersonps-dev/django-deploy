function removerProduto(element) {
    element.parentElement.remove();
}

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("produtoForm").addEventListener("submit", function(event) {
        alert("Produto adicionado com sucesso!");
    });
});