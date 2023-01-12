# pylint: disable=invalid-name
import random
def get_shot(guesses):

    ok = "n"
    while ok == "n":
        try:        # User Feedback
            shot = input("Please enter ur guess to sink the Battleship from numbers(1-99)=")
            shot = int(shot)
            if shot < 0 or shot > 99:
                print("Incorrect number, Please try again!")
            elif shot in guesses:
                print("Incorrect number, used before!")
            else:
                ok = 'y'
                break
        except:
            print("Incorrect entry, Please enter again")
    return shot
            # Game Board In terminal
def show_board(hit ,miss ,comp):
    print("         Sink the Battleship Game - Total Attempts (20) ")
    
    print("     0  1  2  3  4  5  6  7  8  9   ")


    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " _ "
            if place in miss: # Too indicate a miss 
                ch = " x "
            elif place in hit: # Too indicate the ship has been hit 
                ch = " S "  
            elif place in comp: # Too indicate the ship is completed 
                ch = " s "

            row = row + ch
            place = place + 1 
        print(x," ",row)

        # Scanning across Gameboard 
def check_shot(shot,ship1,ship2,hit,miss,comp):

    if shot in ship1:
        ship1.remove(shot)
        if len(ship1) > 0:
            hit.append(shot)
        else:
            comp.append(shot)
    elif shot in ship2:
        ship2.remove(shot)
        if len(ship2) > 0:
            hit.append(shot)
        else:
            comp.append(shot)
    else:
        miss.append(shot)
    return ship1,ship2,hit,miss,comp

startofShipTwo = random.randrange(50,90)
startofShip = random.randrange(46)
ship1 = [startofShip,startofShip+1,startofShip+2,startofShip+3,startofShip+4]
ship2 = [startofShipTwo,startofShipTwo+1,startofShipTwo+2,startofShipTwo+3]

hit = []
miss = []
comp = []

for i in range(99):
    guesses = hit + miss + comp 
    shot = get_shot(guesses)
    ship1,ship2,hit,miss,comp = check_shot(shot,ship1,ship2,hit,miss,comp)
    show_board(hit,miss,comp)
        # End game Result
    if len(ship1) < 1 and len(ship2) < 1:
        print("Winner!!")
