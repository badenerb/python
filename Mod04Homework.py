#Baden Erb
#Mod 04 HomeWork

import sys, random, os, getpass, shutil, zipfile

the_desktop = os.path.join('C:\\Users',getpass.getuser(),'Desktop')

os.chdir(the_desktop)

with open('alert_data.csv', 'w') as b:
    b.write('Date, Time,Priority,Classification,'+'Description,Source IP,Destination IP\n')

with open('alert.fast.maccdc2012_00000.pcap','r') as e:
    for i in e:
        split1 = i.split('[**]')
        date_time = split1[0]           		#date/time
        attack_date = date_time[:5]     	        #date
        attack_time = date_time[6:11]   	        #time
        split2 = split1[1].split('] ')
        description = split2[1].strip() 		#description
        split3 = split1[2].split('] [')
        classification = split3[0]
        classification = classification.strip(' [')
        classification = classification[16:]    	#classification
        priority = split3[1].strip(' [Priority: ')
        priority = priority[:1]                         #priority
        ip = split3[1]
        ip_split = ip.split(' ')
        source_ip = ip_split[3]
        dest_ip = ip_split[5]                           #ip
        with open('alert_data.csv', 'a') as b:
            b.write(attack_date + ',' + attack_time + ',' + priority + ',' + classification +',' + description + ',' + source_ip + ',' + dest_ip)
