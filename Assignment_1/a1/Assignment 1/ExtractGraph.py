from math import log


class ExtractGraph:

    # key is head word; value stores next word and corresponding probability.
    graph = {}

    # Assign the path of sentences file.
    sentences_add = "data//assign1_sentences.txt"

    def __init__(self):
        # Extract the directed weighted graph, and save to {head_word, {tail_word, probability}}

        # Open the sentences file and use a while loop to process all the lines in it.
        s = open(self.sentences_add)
        # Line stands for one line in the file.
        line = s.readline()
        dic = {}
        while line:
            # For each line.
            #   Delete \n in it.
            line = line.replace("\n", "")
            #   Divide it into words to count and calculate the probability.
            words = line.split(" ")
            length = len(words)
            t = 0
            while t < length-1:
                # There are always some blank chars in the line, we ignore them.
                if words[t] == "":
                    pass
                # If this word is already in the dic, we update the probability of the tail words that follow this
                # head word.
                elif words[t] in dic:
                    # Get the probabilities of the tail words that follow this head.
                    temp = dic[words[t]]
                    # If this tail word has already shown after this head, we update its count by +1.
                    if words[t+1] in temp:
                        temp[words[t+1]] += 1
                    # Or it has not shown after this head, we add the tail into the dic that stores the counts.
                    else:
                        temp[words[t+1]] = 1
                # If this head has not shown, we add it and the tail we found this time into the dic.
                else:
                    dic[words[t]] = {words[t+1]: 1}
                t += 1

            # Move to the next line.
            line = s.readline()

        # Because we just only count the tails, we then have to calculate their probabilities.
        for t in dic:
            # Get the sum of counts of all tails that belong to one head.
            num = float(sum(dic[t].values()))
            # Calculate and store their probabilities.
            for i in dic[t]:
                dic[t][i] /= num

        # Close the file and return the result.
        s.close()
        self.graph = dic
        return

    # This function is used to get the probability of the tail word shows after the head word.
    def getProb(self, headWord, tailWord):
        # Firstly judge whether we have seen this head word.
        if headWord in self.graph:
            # Then we judge whether this tail has shown after this head.
            if tailWord in self.graph[headWord]:
                # If it has, return the probability we stored.
                return self.graph[headWord][tailWord]

        # Else, if we have not seen this head or this tail has not shown after this head, we return 0.
        return 0

if __name__ == "__main__":
    a = ExtractGraph()
    a1 = a.getProb("<s>", "He")
    a2 = a.getProb("He", "said")
    a3 = a.getProb("said", ".")
    print(a1)
    print(a2)
    print(a3)
    print(a1*a2*a3)
    print(log(a1*a2*a3))