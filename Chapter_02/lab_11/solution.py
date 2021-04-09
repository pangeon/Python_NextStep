ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ', 'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
linked_ports = []
counter = 0

size = len(ports)

linked_ports = [(ports[i], ports[j]) for i in range(size) for j in range(size) if j != i]

for i in range(size):
    for j in range(size):
        if linked_ports[i] != linked_ports[j]:
            counter += 1
        else:
            counter -= 1

for i in range(len(linked_ports)):
    print(linked_ports[i])

print("Number of directions: {}".format(counter))


        

