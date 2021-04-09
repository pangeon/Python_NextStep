ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ', 'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
linked_ports = []
counter = 0
for i in range(len(ports)):
    for j in range(len(ports)):
        if(ports[i] != ports[j]):
            linked_ports.append((ports[i], ports[j]))
            counter += 1

for i in range(len(linked_ports)):
    print(linked_ports[i])

print("Number of directions: {}".format(counter))
        

