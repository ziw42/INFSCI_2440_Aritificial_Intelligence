if __name__ == "__main__":
    import ExtractGraph
    import BeamSearch

    graph = ExtractGraph.ExtractGraph()
    beam_search = BeamSearch.BeamSearch(graph)

    sentence = "<s> He and she are random"

    s = [0, 0.3, 0.7, 1, 1.3, 1.7, 2, 2.3, 2.5, 3, 3.2, 3.8]
    for param_lambda in s:
        sentence_prob = beam_search.beamSearchV2(sentence, 10, param_lambda, 20)
        print(str(sentence_prob.score) + "\t" + sentence_prob.string)



