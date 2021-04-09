ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ', 'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
counter = 0
def show_flights(generator):
    global counter
    while True:
        try:
            print("Each direction:", next(generator))
            counter += 1
        except StopIteration:
            print("End interation...")
            break

linked_ports_one_way_unique_generator = ((start_station, end_station) for start_station in ports for end_station in ports if start_station < end_station)
show_flights(linked_ports_one_way_unique_generator)
print("Number of directions (one way unique): {}".format(counter))

