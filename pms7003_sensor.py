from pms7003 import Pms7003Sensor, PmsSensorException
from time import sleep

sensor = Pms7003Sensor('/dev/serial0')

while True:
    sleep(1)
    try:
        data_dict = sensor.read()
        pm1_0 = data_dict['pm1_0']
        pm2_5 = data_dict['pm2_5']
        pm10 = data_dict['pm10']
        print("pm1.0: %d, pm2.5: %d, pm10: %d" % (pm1_0, pm2_5, pm10))
    except PmsSensorException:
        print('Nahi chala')
        
sensor.close()