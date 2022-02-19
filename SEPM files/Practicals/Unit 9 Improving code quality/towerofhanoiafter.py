""" Simple code to implement Tower of Hanoi"""

COUNTER = 0


def print_move(move_from, move_to):
    """Function defined to print the moves between poles"""
    global COUNTER
    print(f'move disk from pole {move_from} to pole {move_to}')
    COUNTER += 1


def poles(num_of_disks, move_from, move_to, spare):
    """Function defined to move disks between poles"""
    if num_of_disks == 1:
        print_move(move_from, move_to)
    else:
        poles(num_of_disks-1, move_from, spare, move_to)
        poles(1, move_from, move_to, spare)
        poles(num_of_disks-1, spare, move_to, move_from)


num_of_disk = input('Enter number of disks: ')
print('')
poles(int(num_of_disk), 'A', 'C', 'B')
print('')
print(f'Total number of moves: {COUNTER}')
