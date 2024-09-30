circle_file = input()    #change for input()
dots_file = input()    #change for input()

with open(circle_file, 'r', encoding='utf-8') as circle_data:
    x, y = map(int, circle_data.readline().strip().split())
    radius = int(circle_data.readline())

with open(dots_file, 'r', encoding='utf-8') as dots_data:
    for dots in dots_data:
        dot_x, dot_y = map(int, dots.strip().split())
        result = (dot_x - x)**2 + (dot_y - y)**2

        if result == radius**2:
            print(0)
        elif result < radius**2:
            print(1)
        else:
            print(2)