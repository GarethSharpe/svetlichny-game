'''
Created on Jul 23, 2017
Finalized on Jul 26, 2017
adapted for ibmqx4 by Marcus Edwards on November 9, 2017

@author: Gareth Sharpe
'''

from random import choice

from IBMQuantumExperience import IBMQuantumExperience 

API_TOKEN = 'a0f9090f4b9b0a7f86cb31848730654bb4dbc35aab364a7d728162c96b264752d413b88daea7303c87f12e0a719345119c0f8a880a27d73b998887664a989fce' #'f7403a463f5e9f9e9fb5acd4e664f436d1ac3c5f323f11c235da7294e749bc3a564f7e2977579c3a600716fe5ea49b905c8c9bbace7bf2b4af44641207e35ae5'

api = IBMQuantumExperience(API_TOKEN)

def test_api_auth_token():
    '''
    Authentication with Quantum Experience Platform
    '''
    api = IBMQuantumExperience(API_TOKEN)
    credential = api.check_credentials()

    return credential

def connect():
    '''
    Attempt to connect to the Quantum Experience Platform
    ''' 
    connection_success = test_api_auth_token()

    if(connection_success == True):
        print("API authentication success.")
    else:
        print("API authentication failure.")
        exit()

def computed_svetlichny():
    
    api = IBMQuantumExperience(API_TOKEN)
    device = 'ibmqx4'
    
    qasm = """IBMQASM 2.0;include "qelib1.inc";qreg q[5];creg c[5];h q[0];cx q[2],q[1];cx q[1],q[0];"""
    
    # The referee chooses a three bit string r s t uniformly from the set {000, 011, 101, 110}
    set = ['000', '001', '010', '011', '100', '101', '110', '111']
    referee = choice(set)
    i = 2 * int(referee[0]) - 1
    j = 2 * int(referee[1]) - 1
    k = 2 * int(referee[2]) - 1
    
    q = 0
    index = 0
    for val in referee:
        if val == '1':
            q += 1
        else:
            qasm += "sdg q[" + str(index) + "];"
        index += 1
    
    qasm += "h q[0];h q[1];h q[2];measure q[0] -> c[0];measure q[1] -> c[1];measure q[2] -> c[2];"
        
    exp = api.run_experiment(qasm, device, 1)
   
    state = print_results(exp)
    state = state[2::]
    
    alice = int(state[2])
    bob = int(state[1])
    charlie = int(state[0])
    
    if alice == 0:
        alice = -1
    if bob == 0:
        bob = -1
    if charlie == 0:
        charlie = -1
    
    print("Referee: " + referee)
    print("i: " + str(i) + ", j: " + str(j) + ", k: " + str(k))
    print("q: " + str(q))
    print()
    print("Alice: " + str(alice))
    print("Bob: " + str(bob))
    print("Charlie: " + str(charlie))
    
    win = get_result(alice, bob, charlie, q)
    print("Win: " + str(win))
    return win
    
def get_result(a, b, c, q):
    condition = (-1) ** (q * (q-1) / 2)
    print("Condition: " + str(condition))
    return (a * b * c) == condition

def print_results(exp):
    '''
    Print the distribution of measured results from the given experiment
    Returns the measured state
    '''
    print("---------------------")
    print("RESULTS: ")
    print("---------------------")
    states = "State       | "
    probabilities = "Probability | "
    if 'result' in exp:
        for i in range(len(exp['result']['measure']['labels'])):
            state = exp['result']['measure']['labels'][i]
            probability = exp['result']['measure']['values'][i]
    
            states += str(state) + " | " 
            probabilities += "{:.3f}".format(probability) + " | "
    else:
        print("Bad API response!")
        
    print(states)
    print(probabilities)
    print()
    
    return state

def computed_game(rounds, file_name=None):
    
    if file_name:
        file = open(file_name, 'w')
        file.write("round, result, cumulative, average\n") 
    
    wins = 0
    
    i = 1
    while i <= rounds:
        print("--------------------")
        print("ROUND " + str(i))
        print("--------------------")
        result = computed_svetlichny()
        wins += result
        
        if file_name:
            file.write('{},{},{},{}\n'.format(i, result, wins, str(wins / i)))
    
        i += 1
    
    if file_name:
        print()
        print("File " + file_name + " has been created.")
        file.close()
    
    print()
    print("--------------------")
    print("FINAL RESULTS")
    print("--------------------")
    print("Rounds: " + str(rounds))
    print("Wins: ", str(wins))
    print("Losses: " + str(rounds - wins))
    print("P(win): " + str(wins / rounds))

#computed_game(10)
computed_game(100, "computed_results.txt")
