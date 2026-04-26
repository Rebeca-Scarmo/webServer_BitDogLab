from machine import I2C, Pin
import ahtx0
import machine
import utime
import select
import sys
import neopixel 
import time
##Variáveis Globais
    ##Configura a matriz de led para alertar quando está coletando
np = neopixel.NeoPixel(Pin(7),25)

    ##Configura o sensor I2C (estou utilizando apenas 1 dos sensores do modulo)
i2c = I2C(0, scl=Pin(1), sda=Pin(0))
sensor = ahtx0.AHT20(i2c)

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
    temp = sensor.temperature
    hum = sensor.relative_humidity
    momentoRegistro = registraMomentoFormat()
    
    time.sleep_ms(1500)
    
    leitura = (temp, hum, momentoRegistro)
    leitura = "{},{},{}\n".format(leitura[0],leitura[1], leitura[2])
    return leitura
    
def registraMomentoFormat ():
    segundos = int(utime.ticks_diff(utime.ticks_ms(), inicio) / 1000)
    momentoRegistro = "{}:{}".format(segundos // 60, segundos % 60)
    return momentoRegistro

def sinalizaColeta (onOff):
    if(onOff):
        np[0] = (0, 1, 0)
        np.write()
    else:
        np[0] = (0, 0, 0)
        np.write()
    
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
