from .model.conviction_helper_functions import * 
from .model.sys_params import *

# observe restriction
# 'total_supply' >=  'effective_supply'+'funds'
# for 1Hive case where funds are in the same token
# as the supply.

genesis_states = { 
                'network':initialize_network(initial_values['n'],initial_values['m'],
                                            initial_values['initial_funds'],
                                            initial_values['supply']),
                'funds':initial_values['initial_funds'],
                'sentiment': initial_values['initial_sentiment'],
                'effective_supply': (initial_values['supply']-initial_values['initial_funds'])*.8, #force some slack into the inequality
                'total_supply': initial_values['supply'],

}
