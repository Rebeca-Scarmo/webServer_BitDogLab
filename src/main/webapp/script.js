function carregarDados() {

    fetch('/coleta-de-dados/api/dados') 
        .then(response => response.json())
        .then(dados => {
            const corpoTabela = document.getElementById('corpo-tabela');
            let linhasHtml = '';

            dados.forEach(leitura => {
                linhasHtml += `
                    <tr>
                        <td class="col-id">${leitura.id}</td>
                        <td>${leitura.temperatura.toFixed(4)}</td>
                        <td>${leitura.umidade.toFixed(4)}</td>
                    </tr>
                `;
            });

            corpoTabela.innerHTML = linhasHtml;
        })
        .catch();
}


window.onload = carregarDados;