'''
Created on Jul 22, 2017
Finalized on Jul 26, 2017

@author: Gareth Sharpe
'''

from random import choice

def classical_svetlichny():
    # The referee chooses a three bit string r s t uniformly from the set {000, 011, 101, 110}
    set = ['000', '001', '010', '011', '100', '101', '110', '111']
    referee = choice(set)
    i = 2 * int(referee[0]) - 1
    j = 2 * int(referee[1]) - 1
    k = 2 * int(referee[2]) - 1
    
    q = 0
    for val in referee:
        if val == '1':
            q += 1
    
    print("Referee: " + referee)
    print("i: " + str(i) + ", j: " + str(j) + ", k: " + str(k))
    print("q: " + str(q))
    print()
    
    # The referee sends r to Alice, s to Bob, and t to Charlie.
    # To maximize their chance of success, each player returns a '1', regardless of r s t
    alice = i
    bob = j
    charlie = k
     
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

def classical_game(rounds, file_name=None):
    
    if file_name:
        file = open(file_name, 'w')
        file.write("round, result, cumulative, average\n") 
    
    wins = 0
    
    i = 1
    while i <= rounds:
        print("--------------------")
        print("ROUND " + str(i))
        print("--------------------")
        result = classical_svetlichny()
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

# classical_game(100, "class_results.txt")
