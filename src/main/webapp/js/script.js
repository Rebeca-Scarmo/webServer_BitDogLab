function enviarDados(){
	TODO
}

function formataDados(){
	const arquivo = document.getElementById("InputFile").files[0];
	
	enviarDados();
}
document.getElementById("BtnUpload").addEventListener("click",formataDados);