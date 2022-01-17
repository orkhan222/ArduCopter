from dronekit import connect,VehicleMode
import time
iha = connect('127.0.0.1:14550',wait_ready= True)

# print(iha.is_armable)
# print(iha.armed)
# iha.mode = VehicleMode('GUIDED')
# iha.armed = True
# iha.simple_takeoff(10)

def takeoff(irtifa):
    while iha.is_armable:
        print('Iha arm edilebiler.')
        time.sleep(1)
        
        iha.mode = VehicleMode('GUIDED')
        print(str(iha.mode)+ 'moduna alindi.')
        time.sleep(1)
        
        iha.armed = True
        
        while iha.armed is not True:
            print('Iha arm ediliyor...')
            time.sleep(1)
        
        
        print('Iha arm edildi.')
        
        iha.simple_takeoff(irtifa)
        break
    print('IHA arm edilebilir durumda degil!')
    time.sleep(1)
    
takeoff(15)