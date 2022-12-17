# Opponent A = Rock, B = Paper , C = Scissors
# Personal X = lose, Y = Draw, Z = Win 

# Rock = 1p, Paper = 2p, Scissors = 3p 
# Loss = 0p, Draw = 3p, Win = 6p 

opponent_moves = []
personal_response = []

personal_points = 0 

# get the moves made by the opponent and my response
with open('day_two/input.txt', 'r') as f:
    content = f.read()

    for i in content:
        if i in ['A','B','C']:
            opponent_moves.append(i)
        elif i == " " or i == '\n':
            pass 
        else:
            personal_response.append(i)

# Which throw am I making
def throw_made(opponent_move, result):
    if opponent_move == "A" and result == 'X': # if he throws rock and I lose I threw Scissors
        point = 3
    elif opponent_move == "A" and result == 'Y':
        point = 1
    elif opponent_move == "A" and result == 'Z': 
        point = 2
    elif opponent_move == "B" and result == 'X': 
        point = 1
    elif opponent_move == "B" and result == 'Y': 
        point = 2
    elif opponent_move == "B" and result == 'Z': 
        point = 3
    elif opponent_move == "C" and result == 'X': 
        point = 2
    elif opponent_move == "C" and result == 'Y': 
        point = 3
    elif opponent_move == "C" and result == 'Z': 
        point = 1
    return point

# How many points do I receive
def result_points(result):
    if result == 'X':
        points = 0
    elif result == 'Y':
        points = 3 
    else:
        points = 6
    return points

for i in range(len(personal_response)):
    personal_points += throw_made(opponent_moves[i], personal_response[i])
    personal_points += result_points(personal_response[i])

print(personal_points)