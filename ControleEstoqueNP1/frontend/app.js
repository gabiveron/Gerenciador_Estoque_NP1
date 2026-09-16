const API_URL = 'http://localhost:8000';

// =========================================================================
// 1. DASHBOARD - Carrega as métricas dinamicamente na tela
// =========================================================================
function carregarDashboard() {
    // Busca produtos para contar o total
    fetch(`${API_URL}/produtos`)
        .then(res => res.json())
        .then(produtos => {
            document.getElementById('total-produtos').innerText = produtos.length;
        })
        .catch(err => console.error("Erro ao buscar produtos para o painel:", err));

    // Busca categorias para contar o total
    fetch(`${API_URL}/categorias`)
        .then(res => res.json())
        .then(categorias => {
            document.getElementById('categorias-ativas').innerText = categorias.length;
        })
        .catch(err => console.error("Erro ao buscar categorias para o painel:", err));

    // Busca movimentações do dia
    fetch(`${API_URL}/movimentacoes`)
        .then(res => res.json())
        .then(movimentacoes => {
            const hoje = new Date().toISOString().split('T')[0];

            // Filtra o histórico com base na estrutura de dados do seu Python
            const entradasHoje = movimentacoes.filter(m => m.tipo.toLowerCase() === 'entrada' && m.data.startsWith(hoje)).length;
            const saidasHoje = movimentacoes.filter(m => m.tipo.toLowerCase() === 'saida' && m.data.startsWith(hoje)).length;

            document.getElementById('entradas-hoje').innerText = entradasHoje;
            document.getElementById('saidas-hoje').innerText = saidasHoje;
        })
        .catch(err => console.error("Erro ao buscar movimentações para o painel:", err));
}

// =========================================================================
// 2. PRODUTOS - Operações CRUD completas mapeadas com seu Python
// =========================================================================

// GET - Listar todos os produtos (Ideal para desenhar tabelas)
function listarProdutos() {
    fetch(`${API_URL}/produtos`)
        .then(response => response.json())
        .then(produtos => {
            console.log("Lista de produtos do banco:", produtos);
            // Aqui você pode fazer um loop e jogar em uma <table> no HTML
        })
        .catch(error => console.error('Erro ao listar produtos:', error));
}

// POST - Cadastrar um novo produto (Não envia ID nem Quantidade, conforme seu back-end)
function cadastrarProduto(nome, localizacao, idCategoria, idFornecedor) {
    const novoProduto = {
        nome: nome,
        localizacao: localizacao,
        id_categoria: parseInt(idCategoria),
        id_fornecedor: parseInt(idFornecedor)
    };

    fetch(`${API_URL}/produtos`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(novoProduto)
    })
        .then(response => {
            if (response.ok) {
                alert("Produto cadastrado com sucesso!");
                carregarDashboard(); // Atualiza os blocos visuais na tela
            } else {
                alert("Erro ao cadastrar produto no servidor.");
            }
        })
        .catch(error => console.error('Erro no POST de produto:', error));
}

// PUT - Atualizar um produto existente enviando o ID na URL
function atualizarProduto(idProduto, nome, localizacao, idCategoria, idFornecedor) {
    const dadosAtualizados = {
        nome: nome,
        localizacao: localizacao,
        id_categoria: parseInt(idCategoria),
        id_fornecedor: parseInt(idFornecedor)
    };

    fetch(`${API_URL}/produtos/${idProduto}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(dadosAtualizados)
    })
        .then(response => {
            if (response.ok) {
                alert("Produto atualizado com sucesso!");
                carregarDashboard();
            } else {
                alert("Erro ao atualizar o produto.");
            }
        })
        .catch(error => console.error('Erro no PUT de produto:', error));
}

// DELETE - Excluir um produto passando o ID na URL
function deletarProduto(idProduto) {
    if (confirm(`Deseja realmente excluir o produto ID: ${idProduto}?`)) {
        fetch(`${API_URL}/produtos/${idProduto}`, {
            method: 'DELETE'
        })
            .then(response => {
                if (response.ok) {
                    alert("Produto removido com sucesso!");
                    carregarDashboard();
                } else {
                    alert("Erro ao excluir o produto.");
                }
            })
            .catch(error => console.error('Erro no DELETE de produto:', error));
    }
}

// Inicializa a busca dos contadores assim que a página abre
window.onload = carregarDashboard;
