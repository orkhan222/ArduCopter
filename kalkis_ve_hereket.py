from dronekit import connect,VehicleMode,LocationGlobalRelative
import time
iha = connect('127.0.0.1:14550',wait_ready= True)

# print(iha.is_armable)
# print(iha.armed)
# iha.mode = VehicleMode('GUIDED')
# iha.armed = True
# iha.simple_takeoff(10)

def takeoff(irtifa):
    while iha.is_armable is not True:
        print('Iha arm edilebilir durumda degil.')
        time.sleep(1)
        
    print('Iha arm edilebiler.')
        # time.sleep(1)
        
    iha.mode = VehicleMode('GUIDED')
    print(str(iha.mode)+ 'moduna alindi.')
        # time.sleep(1)
        
    iha.armed = True
        
    while iha.armed is not True:
        print('Iha arm ediliyor...')
        time.sleep(0.5)
        
        
    print('Iha arm edildi.')
        
    iha.simple_takeoff(irtifa)
    
    while iha.location.global_relative_frame.alt < irtifa *0.9:
        print('Iha hedefe yukseliyor.')    
        time.sleep(1)
    
    # break
    # print('IHA arm edilebilir durumda degil!')
    # time.sleep(1)
    
takeoff(10)


konum = LocationGlobalRelative(-35.36226791, 149.16507340, 20)
iha.simple_goto(konum)