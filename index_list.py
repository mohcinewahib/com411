def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path
def run():
    i = 0
    j = 1
    p = []
    print("moving...")
    p = movements()
    for x in p:
        print(p[i] + "for" + p[j])
        i=i+1
        j=j+1
run()