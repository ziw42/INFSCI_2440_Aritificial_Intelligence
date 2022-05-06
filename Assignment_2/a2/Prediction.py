import Filtering


def prediction(evidence_data_add, prior, start_day, end_day):
    # you need to implement this method.

    # List that stores the probability of rain
    x_prob_rain = []
    # x_prob_sunny[i] = 1 - x_prob_rain[i]

    # Use the filter function we implement before to get the results of the first 100 days
    x_prob_rain_filter = Filtering.filtering(evidence_data_add, prior, 100)
    # Here we do not need the sensor model anymore, so we just initialize the transition model
    transition_model = [[0.7, 0.3], [0.3, 0.7]]
    for i in range(start_day, end_day+1):
        x_prob_rain.append(0.0)

    # Here is the same as what we did in the filter function, we will firstly calculate the probability of the first
    # day (the first day of the prediction period)
    # We use the last day's probability of the result from filter function as the prior probability
    x0 = x_prob_rain_filter[len(x_prob_rain_filter)-1]
    # s is simply the probability, but with our alpha
    # s[0] is the probability of rain, s[1] is the probability of sun
    s = []
    s.append(transition_model[0][0]*x0 + transition_model[1][0]*(1-x0))
    s.append(transition_model[0][1]*x0 + transition_model[1][1]*(1-x0))
    # Calculae the alpha and times it to s[0]
    x_prob_rain[0] = 1 / (s[0] + s[1]) * s[0]

    # Here we use a for loop to calculate the probabilities of rain from the 2nd day to the end we set
    # (2nd and end day of prediction period)
    # Steps are basically the same as the code above
    for t in range(start_day+1, end_day+1):
        # Here is the only difference, here we do NOT use the probability from the filter result as prior
        # We use the probability of the day before we predicted as prior instead
        prob_rain = x_prob_rain[t-start_day-1]
        prob_sunny = (1-prob_rain)
        s = []
        s.append(transition_model[0][0] * prob_rain + transition_model[1][0]*prob_sunny)
        s.append(transition_model[0][1] * prob_rain + transition_model[1][1]*prob_sunny)
        x_prob_rain[t-start_day] = 1 / (s[0] + s[1]) * s[0]

    # All the probabilities of rain are stroed in the x_prob_rain list
    return x_prob_rain


# following lines are main function:
evidence_data_add = "data//assign2_umbrella.txt"
start_day = 101
end_day = 150
# the prior distribution on the initial state, P(X0). 50% rainy, and 50% sunny on day 0.
prior = [0.5, 0.5]

x_prob_rain=prediction(evidence_data_add, prior, start_day, end_day)
for i in range(start_day, end_day+1):
    print("Day " + str(i) + ": rain " + str(x_prob_rain[i-start_day]) + ", sunny " + str(1 - x_prob_rain[i-start_day]))
    # print("Day " + str(i+1) + ": rain " + str(x_prob_rain[i]) + ", sunny " + str(1 - x_prob_rain[i]))
