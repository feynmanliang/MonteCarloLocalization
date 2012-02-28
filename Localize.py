colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['red', 'green', 'red', 'green']


motions = [[0,0],[0,1],[1,0],[0,1]]

sensor_right = 1.0

p_move = 1.0

def show(p):
    for i in range(len(p)):
        print p[i]

# Initialize p as an array of 1s w/ dimensions = colors
p = [ ]
for i in range(len(colors)):
    p.append([])
    for j in range(len(colors[i])):
        p[i].append(1.0)


def sense(p, sensor):
    # Create non-normalized sense array
    q =  [ ]
    for i in range(len(colors)):
        q.append([])
        for j in range(len(colors[i])):
            # Adjust sensor error
            if (sensor == colors[i][j]):
                q[i].append(p[i][j] * sensor_right)
            else:
                q[i].append(p[i][j] * (1-sensor_right))

    # Count # terms for normalizing
    numTerms = 0;
    for i in range(len(q)):
        for j in range(len(q[i])):
            numTerms = numTerms + q[i][j]
    # Normalize
    for i in range(len(q)):
        for j in range(len(q[i])):
            q[i][j] = q[i][j] / numTerms
    return q

def move(p, move):
    # Create moved array
    q = [ ]
    for i in range(len(p)):
        q.append([])
        for j in range(len(p[i])):
            moved = p[(i-move[0]) % len (p)][(j-move[1]) % len (p[i])] * p_move
            nomove = p[i][j] * (1-p_move)
            q[i].append(moved + nomove )
    return q

if len(measurements)==len(motions):
    for k in range(len(measurements)):
        p = move(p, motions[k])
        p = sense(p, measurements[k])

show(p)