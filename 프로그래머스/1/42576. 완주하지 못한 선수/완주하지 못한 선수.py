import collections

def solution(participant, completion):
    p_dictionary = collections.Counter(participant)
    c_dictionary = collections.Counter(completion)
    
    for key in participant:
        if p_dictionary[key] != c_dictionary[key]:
            return key