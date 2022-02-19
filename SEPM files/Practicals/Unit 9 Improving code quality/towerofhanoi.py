counter = 0

def printMove(fr, to):
    global counter
    print('move disk from pole {} to pole {}'.format(fr, to))
    counter += 1

def Poles(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Poles(n-1, fr, spare, to)
        Poles(1, fr, to, spare)
        Poles(n-1, spare, to, fr)

n = input('Enter number of disks: ')
print('')
Poles(int(n), 'A', 'C', 'B')
print('')
print('Total number of moves: {}'.format(counter))
