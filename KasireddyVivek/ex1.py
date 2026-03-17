def robot_move(moves):
    x = 0
    y = 0

    for move in moves:
        direction, steps = move

        if direction == 'N':
            y += steps
        elif direction == 'S':
            y -= steps
        elif direction == 'E':
            x += steps
        elif direction == 'W':
            x -= steps

    return (x, y)

if __name__ == "__main__":
    moves = [('N',2), ('E',4), ('S',1), ('W',3)]
    result = robot_move(moves)
    print(result)