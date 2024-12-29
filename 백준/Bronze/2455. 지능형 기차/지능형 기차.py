def max_passengers_on_train(train_stations):
    current_passengers = 0
    max_passengers = 0

    for off, on in train_stations:
        current_passengers += on - off  
        max_passengers = max(max_passengers, current_passengers)  

    return max_passengers

train_stations = [tuple(map(int, input().split())) for _ in range(4)]

result = max_passengers_on_train(train_stations)

print(result)
