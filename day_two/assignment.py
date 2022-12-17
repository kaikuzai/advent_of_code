# Opponent A = Rock, B = Paper , C = Scissors
# Me X = Rock, Y = Paper, Z = Scissors

# Rock = 1p, Paper = 2p, Scissors = 3p 
# Loss = 0p, Draw = 3p, Win = 6p 

opponent_moves = []
personal_moves = []

opponent_points = 0
personal_points = 0 

#functions 
def points_for_throws(throw):
    if throw in ['A','X']:
        point = 1
    elif throw in ['B', 'Y']:
        point = 2
    else:
        point = 3
    return point 

def letters_to_words(throw):
    if throw in ['A','X']:
        throw = 'Rock'
    elif throw in ['B', 'Y']:
        throw = 'Paper'
    else:
        throw = 'Scissors'
    return throw 


def game_results(personal, opponent):
    if personal == opponent: # in case of draw
        my_points = 3
        their_points = 3
    elif (personal == 'Rock' and opponent == 'Scissors') or (personal == 'Paper' and opponent == 'Rock') or (personal == 'Scissors' and opponent == 'Paper'): # in case of win 
        my_points = 6
        their_points = 0
    else: # in case of loss 
        my_points = 0
        their_points = 6

    return my_points, their_points


# get the moves made by the opponent 
with open('day_two/input.txt', 'r') as f:
    content = f.read()

    for i in content:
        if i in ['A','B','C']:
            opponent_moves.append(i)
        elif i == " " or i == '\n':
            pass 
        else:
            personal_moves.append(i)


#calculation 
for i in range(len(personal_moves)):
    personal_points += points_for_throws(personal_moves[i])
    opponent_points += points_for_throws(opponent_moves[i])

    # print(f'I have thrown {personal_moves[i]} which gives me {points_for_throws(personal_moves[i])} points so my total is now {personal_points}')

    personal_throw = letters_to_words(personal_moves[i])
    opponent_throw = letters_to_words(opponent_moves[i])

    my_points, their_points = game_results(personal_throw, opponent_throw)

    personal_points += my_points
    opponent_points += their_points

print(personal_points)
print(opponent_points)
