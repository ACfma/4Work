# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 08:25:41 2022

@author: Andrea
"""


import random
import itertools

prev_play, opponent = "P",["S","P","P","P","P","S","S","R","S","P","P","P","P","S","S","P"]
opponent_history = []

class MarkovChain():

    def __init__(self, order, decay=1.0):
        self.decay = decay
        self.matrix = self.create_matrix(order)

    @staticmethod
    def create_matrix(order):

        def create_keys(order):            

            keys = ['R', 'P', 'S']

            for i in range(int(order * 2 - 1)):
                key_len = len(keys)
                for i in itertools.product(keys, ''.join(keys)):
                    keys.append(''.join(i))
                keys = keys[key_len:]

            return keys

        keys = create_keys(order)

        matrix = {}
        for key in keys:
            matrix[key] = {'R': {'prob' : 1 / 3,
                                 'n_obs' : 0
                                },
                           'P': {'prob' : 1 / 3,
                                 'n_obs' : 0
                                },
                           'S': {'prob' : 1 / 3,
                                 'n_obs' : 0
                                }
                          }

        return matrix

    def update_matrix(self, pair, input):
        
        for i in self.matrix[pair]:
            self.matrix[pair][i]['n_obs'] = self.decay * self.matrix[pair][i]['n_obs']

        self.matrix[pair][input]['n_obs'] = self.matrix[pair][input]['n_obs'] + 1
        
        n_total = 0
        for i in self.matrix[pair]:
            n_total += self.matrix[pair][i]['n_obs']
            
        for i in self.matrix[pair]:
            self.matrix[pair][i]['prob'] = self.matrix[pair][i]['n_obs'] / n_total            

    def predict(self, pair):

        probs = self.matrix[pair]

        return max([(i[1]['prob'], i[0]) for i in probs.items()])[1]        
    
order = 1    
markov_model = MarkovChain(order, 1)
order = int(order*2)
class RandomPredictor():

    @staticmethod
    def predict():
        return random.choice(['R','P','S'])
for o in opponent:
    prev_play = o
    opponent_history.append(prev_play)
    play = ['R','P','S']
    
    oppst = "".join(opponent_history)
    
    opponent_history = [x for x in  opponent_history if x]
    beat = {'R': 'P', 'P': 'S', 'S': 'R'}
        
        
    random_predictor = RandomPredictor()
    
    
    if len(opponent_history)<=order:
        pair_diff2 = ''
        if len(opponent_history)<order:
            pair_diff1 = ''
        else:
            pair_diff1 = "".join(opponent_history[-(order):])
    else:
        pair_diff2 = "".join(opponent_history[-(order+1):-1])
        pair_diff1 = "".join(opponent_history[-(order):])

    if pair_diff2 != '':
        markov_model.update_matrix(pair_diff2, opponent_history[-1])
        guess = markov_model.predict(pair_diff1)
    else:
        guess = random_predictor.predict()
