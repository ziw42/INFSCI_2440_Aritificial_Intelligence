import numpy as np

def get_p_b_cd():
    # you need to implement this method.
    p_b_cd = np.zeros((3,3,2),dtype = np.float)

    # Read the file
    f = open(data_add)
    f.readline()
    line = f.readline()
    # We use this while loop to iterate over the file
    # Count the instances of different combination of b and c and d
    while line:
        temp = line.split("\t")
        # b is on the 3rd column, c on the 4th and d on the 5th
        b = int(temp[2])
        c = int(temp[3])
        d = int(temp[4])
        # Count of this combination of b,c,d +1
        p_b_cd[b-1][c-1][d-1] += 1
        line = f.readline()

    # Now in p_b_cd, all the elements are counts
    # We then will transform all of the elements to probabilities
    t = 0
    # Iterate over c
    for t in range(3):
        # Iterate over d
        for i in range(2):
            sum = 0
            # Iterate over b
            for j in range(3):
                sum += p_b_cd[j][t][i]
            # Sum is the count of instances of all values of b given specific values of c and d
            # p_b_cd[j][t][i] is the count of instances of a specific value of b given specific values of c and d
            for j in range(3):
                # Probability = count/number of all instances
                p_b_cd[j][t][i] /= sum
    f.close()

    # Return the result
    return p_b_cd

def get_p_a_be():
    # you need to implement this method.
    # This function is basically the same as get_p_b_cd()
    p_a_be = np.zeros((2,3,2),dtype = np.float)
    # Read the file
    f = open(data_add)
    f.readline()
    line = f.readline()
    sum = 0
    # We use this while loop to iterate over the file
    # Count the instances of different combination of a and b and e
    while line:
        sum += 1
        temp = line.split("\t")
        # a is on the 2 column, and b is on the 3rd, e is on the 6th
        a = int(temp[1])
        b = int(temp[2])
        e = int(temp[5])
        # Count of this combination of a,b,e +1
        p_a_be[a - 1][b - 1][e - 1] += 1
        line = f.readline()

    # Now in p_a_be, all the elements are counts
    # We then will transform all of the elements to probabilities

    # Iterate over b
    for t in range(3):
        # Iterate over e
        for i in range(2):
            sum = 0
            # Iterate over a
            for j in range(2):
                sum += p_a_be[j][t][i]
            # Sum is the count of instances of all values of b given specific values of c and d
            # p_b_cd[j][t][i] is the count of instances of a specific value of b given specific values of c and d
            for j in range(2):
                # Probability = count/number of all instances
                p_a_be[j][t][i] /= sum

    f.close()

    return p_a_be


# following lines are main function:
data_add = "data//assign2_BNdata.txt"

# probability distribution of b.
p_b_cd=get_p_b_cd()
for c in range(3):
    for d in range(2):
        for b in range(3):
            print("P(b=" + str(b+1) + "|c=" + str(c+1) + ",d=" + str(d+1) + ")=" + str(p_b_cd[b][c][d]))


# probability distribution of a.
p_a_be=get_p_a_be()
for b in range(3):
    for e in range(2):
        for a in range(2):
            print("P(a=" + str(a+1) + "|b=" + str(b+1) + ",e=" + str(e+1) + ")=" + str(p_a_be[a][b][e]))

