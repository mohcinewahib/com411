def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions
def menu():
    lo = []
    dir = input("Please select a direction: ")
    lo = directions()
    for index in range(len(lo)):
        fruit = lo[index]
        print(f"{fruit}: {index}.")
menu()
def run():
    route = []
    i = 0
    print("Working out escape route...")
    while i <= 5:
        route = menu()
        route.append(menu[i])
        i = i +1
    run()



