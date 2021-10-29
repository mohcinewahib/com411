def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions
def menu():
    dir = input("Please select a direction:")
    re = []
    re = directions()
    for index in range(len(re)):
        fruit = re[index]
        print(f"{fruit}: {index}.")
menu()