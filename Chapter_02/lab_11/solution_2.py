ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ', 'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

def show_flights(ports_list):
    for i in range(len(ports_list)): 
        print("Each direction:", ports_list[i])

linked_ports = [(start_station, end_station) for start_station in ports for end_station in ports]
show_flights(linked_ports)
print("Number of directions: {}".format(len(linked_ports)))

linked_ports_two_way_unique = [(start_station, end_station) for start_station in ports for end_station in ports if start_station != end_station]
show_flights(linked_ports_two_way_unique)
print("Number of directions (two way unique): {}".format(len(linked_ports_two_way_unique)))

linked_ports_one_way_unique = [(start_station, end_station) for start_station in ports for end_station in ports if start_station < end_station]
show_flights(linked_ports_one_way_unique)
print("Number of directions (one way unique): {}".format(len(linked_ports_one_way_unique)))








        

