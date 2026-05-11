<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <title>DC4K - Monitor de Composteira</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>

    <div class="divUpload" id="DivUpload">
    	<label for="InputFile">Faça aqui o upload dos arquivos</label>
    	<input type="file" name="file" class="inputFile" id="InputFile">
    	
    	<label for="HoraColeta">Hora de Início da coleta:</label>
    	<input type="time" name="time" class="horaColeta" id="HoraColeta">
    	
    	<label for="DataColeta">Data da Coleta</label>
    	<input type="date" name="date" class="dataColeta" id="DataColeta">
    	
    	<button class="btnUpload" id="BtnUpload">Enviar</button>
    </div>
    
   	<div class="divGrafico" id="DivGrafico">
   	
   	</div>
    
    <div class="divTabela" id="DivTabela">
    
    </div>
    
	<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="js/script.js"></script>
    
    
</body>
</html>