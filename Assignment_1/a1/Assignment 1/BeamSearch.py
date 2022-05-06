from math import log

import StringDouble
import ExtractGraph

class BeamSearch:

    graph = []

    def __init__(self, input_graph):
        self.graph = input_graph
        return

    def beamSearchV1(self, pre_words, beamK, maxToken):
    	# Basic beam search.
        # This is just the length normalization version with lambda=0.
        return self.beamSearchV2(pre_words, beamK, 0, maxToken)

    def beamSearchV2(self, pre_words, beamK, param_lambda, maxToken):
    	# Beam search with sentence length normalization.

        sentence = ""
        # Here we will set the initial best probability an extremely small number, so the first sentence we found is
        # better than the initial best.
        probability = -9999999999.99

        # Here, queue stores all the sentences that to be calculated.
        # "calculate" means we will calculate their score.
        # Because we will use log space, we sum the log score, the initial log score is 0, not 1.
        queue = {pre_words: 0}
        while queue:
            # tmp_que is the next queue.
            tmp_que = {}
            for t in queue:
                # Get the last word of the sentence that to be calculated.
                word = t.split(" ")[-1]
                # temp is the sorted list that stores the tail and the probability of this head word.
                temp = sorted(self.graph.graph[word].items(), key=lambda x: x[1], reverse=True)
                # Here we want to see if we have at least beamK tail words, if so, we just calculate first beamK tail
                # words. If not, we will calculate all the tail words we got.
                # rag = min(beamK, numOfTails)
                length = len(temp)
                if length < beamK:
                    rag = length
                else:
                    rag = beamK

                # Calculate the log scores of all sentences consist of these tail words.
                i = 0
                while i < rag:
                    # Store the score into the next queue, but here we do not divide the length yet, we will do this
                    # later.
                    tmp_que[t + " " + temp[i][0]] = log(self.graph.graph[word][temp[i][0]]) + queue[t]
                    i += 1
            # temp now is the sorted list of next queue.
            temp = sorted(tmp_que.items(), key=lambda x: x[1], reverse=True)
            # Again, rag = min(length(next queue), beamK).
            length = len(temp)
            if beamK > length:
                rag = length
            else:
                rag = beamK
            queue = {}

            # Here we judge whether this sentence is longer than max length, or it comes to </s>.
            t = 0
            while t < rag:
                # If it is longer than the max length, we just ignore it because we will not expand it anymore.
                # If not, we judge it whether comes to </s>.
                if len(temp[t][0].split(" ")) <= maxToken:
                    # If this sentence is complete, we see if its score divided by length is better than the current
                    # best. If it is better, we set current best to it. If it is not, we put it back to queue to expand.
                    if temp[t][0].split(" ")[-1] == "</s>":
                        i = 0
                        # ylambda = 1/|y|^lambda
                        ylambda = pow(len(temp[t][0].split(" ")), param_lambda)
                        # The reason we just divide the length here not before is we will store the score that has not
                        # been divided into the queue, so we can directly add the next log probability to the current
                        # score. If we store the score that has been divided by length, we have to multiply it by the
                        # length, then we can add the next probability.
                        if tmp_que[temp[t][0]] / ylambda > probability:
                            probability = tmp_que[temp[t][0]] / ylambda
                            sentence = temp[t][0]
                    else:
                        queue[temp[t][0]] = tmp_que[temp[t][0]]
                t += 1
        # Return the best sentences and the probability.
        probability
        return StringDouble.StringDouble(sentence, probability)
