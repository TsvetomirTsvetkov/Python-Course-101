def gas_stations(distance, tank_size, stations):
    tank = tank_size
    length = len(stations)
    stops = []    
    to_next = 0

    for i in range(0,length - 1):
        if i == 0:
            tank -= stations[i]
        else:
            tank -= stations[i] - stations[i - 1]
            to_next = stations[i + 1] - stations[i]
        if tank <= 0 or tank <= to_next:
            stops.append(stations[i])
            tank = tank_size
    
    tank -= stations[length - 1] - stations[length - 2]
    
    if tank <= (distance - stations[length - 1]):
        stops.append(stations[length - 1])
    
    return stops
        
def main():
    print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))
    # Expected output : [80, 140, 220, 290]

    print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350])) 
    # Expected output : [70, 140, 210, 280, 350]

if __name__ == '__main__':
    main()