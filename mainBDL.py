from machine import I2C, Pin
import ahtx0
import time
from hardware import oled
import machine
import utime
import select
import sys
 
ledWarning = Pin(12, Pin.OUT)
i2c = I2C(0, scl=Pin(1), sda=Pin(0))
sensor = ahtx0.AHT20(i2c)
ultimoTempo = 0
momentoRegistro = 0
poller = select.poll()
poller.register(sys.stdin, select.POLLIN)
inicio = utime.ticks_ms()

while True:
    if poller.poll(0):
        if(sys.stdin.readline().strip() == "dump"):
            try:
                with open('dadosCSV.csv','r') as f:
                    for i in f.readlines():
                        print(i)
            except:
                print("Nenhum dado registrado ainda")
    if(utime.ticks_diff(utime.ticks_ms(), ultimoTempo) > 60000):
        ultimoTempo = utime.ticks_ms()
        
        ledWarning.on()
        
        temp = sensor.temperature
        hum = sensor.relative_humidity
        momentoRegistro = "{}:{}".format(
            (int(utime.ticks_diff(utime.ticks_ms(), inicio)/1000)//60),
            (int(utime.ticks_diff(utime.ticks_ms(), inicio)/1000)%60)
        )
        
        temp_str = "{:.2f} C".format(temp)
        hum_str = "{:.2f} %".format(hum)
        time.sleep_ms(1500)
        ledWarning.off()
            
        print("Temp:", temp_str)
        print("Umid:", hum_str)
        print("Momento:", momentoRegistro)
        print("------------------")
        
        leitura = (temp, hum, momentoRegistro)
        
        writeFormat = "{}, {}, {}\n".format(leitura[0],leitura[1], leitura[2])
        with open('dadosCSV.csv','a') as f:
            f.write(writeFormat)
          
