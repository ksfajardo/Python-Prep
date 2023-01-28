import sys
import os

montanas = {'nombre':[  'Everest','K2','Kanchenjunga','Lhotse','Makalu',
                        'Cho Oyu','Dhaulagiri','Manaslu','Nanga Parbat','Annapurna I'],
            'orden':[1,2,3,4,5,6,7,8,9,10],
            'cordillera':['Himalaya','Karakórum','Himalaya','Himalaya','Himalaya'
                        ,'Himalaya','Himalaya','Himalaya','Karakórum','Himalaya'],
            'pais': ['Nepal','Pakistán','Nepal','Nepal','Nepal','Nepal','Nepal','Nepal',
                    'Pakistán','Nepal'],
            'altura':[8849,8611,8586,8516,8485,8188,8167,8163,8125,8091]}

pt3=open('clase09_ejmio3.csv','w')

for claves in montanas.keys():
    if(claves=='altura'):
        pt3.write(str(claves)+'\n')
    else:    
        pt3.write(str(claves)+',')

for i in range (10):
    pt3.write(str(montanas['nombre'][i])+','+str(montanas['orden'][i])+','+str(montanas['cordillera'][i])+','+str(montanas['pais'][i])+','+str(montanas['altura'][i])+'\n')

pt3.close()

print (float(os.path.getsize('clase09_ejmio3.csv'))/1048576) \

os.makedirs('montanas_altas')
os.system('copy clase09_ejmio3.csv montanas_altas')

os.listdir('montanas_altas')