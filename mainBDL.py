from machine import Pin
import utime
import select
import sys
import time
import dht
import onewire
import ds18x20
##Variáveis Globais
    ##Configura led do pico para alertar quando está coletando
led = Pin("LED", Pin.OUT)

    ##Cria objetos do sensor DHT22 para umidade
dhtD = dht.DHT22(Pin(3))
dhtF = dht.DHT22(Pin(4))
    ##Cria barramente para o sensor ds18b20 de temperatura
owD = onewire.OneWire(Pin(2))
owF = onewire.OneWire(Pin(5))
    ##Cria controlador para o sensor ds18b20
dsD = ds18x20.DS18X20(owD)
dsF = ds18x20.DS18X20(owF)
    ##procura pelos sensores ds18b20
look4D = dsD.scan()
look4F = dsF.scan()
    ##Configurações para leitura do console
poller = select.poll()
poller.register(sys.stdin, select.POLLIN)

    ##Variaveis auxiliares
inicio = utime.ticks_ms()
marcaTempo = utime.ticks_ms() 
INTERVALO = 60000
    
def dumpConsole():
    if poller.poll(0):
        if(sys.stdin.readline().strip() == "dump"):
            try:
                with open('dadosCSV.csv','r') as f:
                    for i in f.readlines():
                        print(i)
            except:
                print("Nenhum dado registrado ainda")
                
def verificaTempo():
    global marcaTempo
    agora = utime.ticks_ms()
    if(utime.ticks_diff(agora, marcaTempo) > INTERVALO):
        marcaTempo = utime.ticks_add(marcaTempo, INTERVALO)
        return True
    else:
        return False
    
def coletaDadosFormat ():
    
    
    #coleta do dht22
    dhtD.measure()
    dhtF.measure()
    humF = dhtF.humidity()
    humD = dhtD.humidity()
    
    #coleta do ds18b20
    dsD.convert_temp()
    dsF.convert_temp()
    
    time.sleep_ms(750)
    
    tempD = dsD.read_temp(look4D[0])
    tempF = dsF.read_temp(look4F[0])
    
    momentoRegistro = registraMomentoFormat()
    
    
    leitura = (tempD, tempF, humD, humF, momentoRegistro)
    leitura = "{},{},{},{},{}\n".format(leitura[0],leitura[1], leitura[2], leitura[3], leitura[4])
    time.sleep_ms(750)
    return leitura
    
def registraMomentoFormat ():
    segundos = int(utime.ticks_diff(utime.ticks_ms(), inicio) / 1000)
    momentoRegistro = "{}:{}".format(segundos // 60, segundos % 60)
    return momentoRegistro

def sinalizaColeta (onOff):
    if(onOff):
       led.on()
    else:
        led.off()
    
def guardaDados (leitura):
    with open('dadosCSV.csv','a') as f:
            f.write(leitura)

def main ():
    
    while True:
        coleta = None
        dumpConsole()
        deve = verificaTempo()
        if deve:
            sinalizaColeta(1)
            coleta = coletaDadosFormat()
            sinalizaColeta(0) 
        if(coleta):
            guardaDados(coleta)
        time.sleep_ms(1000)
            
main()