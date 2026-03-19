def robot_move(moves):
    # Here we are initializing the robot position at the given origin of (0,0)
    # Where: 
        # x-axis represents the east-west direction (positive x is east, negative x is west)
        # y-axis represents the north-south direction (positive y is north, negative y is south)
    x = 0
    y = 0

    # Next, we will iterate through the list of moves and update the robot's position based on the direction and steps specified in each move. 
    # Each move is basically a tuple: (direction, steps)
    for move in moves:
        direction, steps = move # Unpacking the move tuple into direction and steps variables

        # We update position based on the direction 
        # So for example, north increases y, south decreases y, east increases x, and west decreases x

        if direction == 'N':
            y += steps
        elif direction == 'S':
            y -= steps
        elif direction == 'E':
            x += steps
        elif direction == 'W':
            x -= steps
    # Finally, we return the final position of the robot as a tuple (x, y)

    return (x, y)

# This is an example input to test the function. You can modify the moves list to test with different inputs.
if __name__ == "__main__":
    moves = [('N',2), ('E',4), ('S',1), ('W',3)]
    result = robot_move(moves)
    print(result)