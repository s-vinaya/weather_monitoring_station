import thingspeak
import time
import Adafruit_DHT
from Adafruit_BMP085 import BMP085
#from Adafruit_BMP085 import BMP085
 
channel_id = 1432028 # PUT CHANNEL ID HERE
write_key  = 'VVLNHP056PKMTWMC' # PUT YOUR WRITE KEY HERE
read_key   = 'H74VO6K43883VVI2' # PUT YOUR READ KEY HERE
pin = 4
sensor = Adafruit_DHT.DHT11
bmp = BMP085(0x77)


 
def measure(channel):
    try:
        
         pressure = bmp.readPressure()
        
         humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
         if humidity is not None and temperature is not None:
             print("Temp={0:0.1f}*C Humidity={1:0.1f}%".format(temperature,humidity))  
        
         else:
             print("did not")
        
        # write
         response = channel.update({'field1': temperature, 'field2': humidity ,'field3':pressure})
        
        # read
         read = channel.get({})
         print("Read:", read)
        
    except:
         print("connection failed")
 #api_key=read_key
 
if _name=='main_' :
    channel = thingspeak.Channel(id=channel_id, write_key=write_key)
    while True:
        measure(channel)
        # free account has an api limit of 15sec
        #time.sleep(15)
