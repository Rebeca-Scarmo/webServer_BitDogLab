function enviarDados(matriz, horaInicio, dataColeta){
	const sessao = { horaInicio: horaInicio, dataColeta: dataColeta };
	
	fetch("/webServer_DC4K/upload",{
		method:"POST",
		headers: {"Content-Type": "application/json"},
		body: JSON.stringify(sessao)
	})
	.then(resposta => resposta.json())
	.then(dados => {
		
    const idSessao = dados.id;
    const leituras = { idSessao: idSessao, leituras: matriz };
    
    fetch("/WebServer_DC4K/upload", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(leituras)
    });
})
}

function formataDados(){
	const arquivo = document.getElementById("InputFile").files[0];
	const leitor = new FileReader();
	leitor.onload = evento;
	leitor.readAsText(arquivo);
	
}

function evento(e){
	const horaInicio = document.getElementById("HoraColeta").value;
	const dataColeta = document.getElementById("DataColeta").value;
	const conteudo = e.target.result;
	const linhas = conteudo.split("\n");
	const matriz = [];
	for (let i =0; i<linhas.length;i++){
		const colunas = linhas[i].split(",");
		const leitura = {
        tempDentro: parseFloat(colunas[0]),
        umidDentro: parseFloat(colunas[1]),
        tempFora: parseFloat(colunas[2]),
        umidFora: parseFloat(colunas[3]),
        tempo: colunas[4]
    	}
    matriz.push(leitura);
	}
	enviarDados(matriz, horaInicio, dataColeta);
}
document.getElementById("BtnUpload").addEventListener("click",formataDados);