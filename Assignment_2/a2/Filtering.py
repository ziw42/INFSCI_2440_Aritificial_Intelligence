def filtering(evidence_data_add, prior, total_day):
    # you need to implement this method.

    x_prob_rain = []
    # x_prob_sunny[i] = 1 - x_prob_rain[i]

    # Initialize the x_prob_rain list, set all probability to 0
    for i in range(total_day):
        x_prob_rain.append(0.0)

    # Read the data file
    f = open(evidence_data_add)
    # The probabilities in transition model and sensor model tables
    transition_model = [[0.7, 0.3], [0.3, 0.7]]
    sensor_model = [[0.9, 0.1], [0.2, 0.8]]

    #
    # Notice, here we firstly calculate the 1st (not 0th) day's probability of rain because the 0th day's probability
    # is stored in prior, not x_prob_rain
    #
    #
    # Look the data from the data file, we only need to see if it is "n" for no, or "t" for take
    # If bring umbrella, u = 0
    # If not, u = 1
    if f.readline().split("\t")[1][0] == "n":
        u1 = 1
    else:
        u1 = 0
    # s1 is P(R)
    # s1[0] is P(R|r=rain), s1[1] is P(R|r=sun)
    s1 = []
    s1.append(transition_model[0][0]*prior[0] + transition_model[1][0]*prior[1])
    s1.append(transition_model[0][1]*prior[0] + transition_model[1][1]*prior[1])
    # s2 us P(R|u)
    # s2[0] is P(rain|u), s2[1] is P(sun|u)
    s2 = []
    s2.append(sensor_model[0][u1]*s1[0])
    s2.append(sensor_model[1][u1]*s1[1])
    # calculate alpha, and times with P(rain|u) to get the probability of (rain|u)
    # Store it into x_prob_rain[0]
    x_prob_rain[0] = 1/(s2[0]+s2[1])*s2[0]

    # Now we use for loop to calculate all the probabilities from the 2nd day to the end we set
    # The meaning of the variables and the steps are the same as former steps
    for t in range(1, total_day):
        if f.readline().split("\t")[1][0] == "n":
            u = 1
        else:
            u = 0
        s1 = []
        # The only difference is here, we use the x_prob_rain[t-1] and 1-x_prob_rain[t-1] as the prior here
        prob_rain = x_prob_rain[t-1]
        prob_sunny = 1-prob_rain
        s1.append(transition_model[0][0] * prob_rain + transition_model[1][0] * prob_sunny)
        s1.append(transition_model[0][1] * prob_rain + transition_model[1][1] * prob_sunny)
        s2 = []
        s2.append(sensor_model[0][u] * s1[0])
        s2.append(sensor_model[1][u] * s1[1])
        x_prob_rain[t] = 1 / (s2[0] + s2[1]) * s2[0]
    f.close()

    # All probabilities are stroed in x_prob_rain
    return x_prob_rain


# following lines are main function:
evidence_data_add = "data//assign2_umbrella.txt"
total_day = 100
# the prior distribution on the initial state, P(X0). 50% rainy, and 50% sunny on day 0.
prior = [0.5, 0.5]

x_prob_rain=filtering(evidence_data_add, prior, total_day)
for i in range(100):
    print("Day " + str(i+1) + ": rain " + str(x_prob_rain[i]) + ", sunny " + str(1 - x_prob_rain[i]))
