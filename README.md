# project-3---battleship-python

# Sink the Battleship's Game

Battleship is a python terminal game which the user needs to sink the enemies battleship by submitting numbers between 1/99.  
# How to play? 

1. In this version , the player needs to enter numbers ranging from 1 to 99.

2. The player has a limited number of attempts (45), to sink the battleships if the user exceeds past the amount the game comes to an end.

3. The user will guess numbers across the grid to try indicate the location of the ship , the symbol will begin with a capital "S" when a ship has been 
struck, and will finish with a lowercase "s" when finished. If the location of were the user guessed is wrong the symbol will be marked with a capital "X" to show users attempt.

4. The game gives user feedback when they have submitted a false attempt Eg( letters) or Eg(duplication on numbers already submitted).

5. When the user has complety sunk all the battleships the Game will display feedback ( winner!! ).

# Existing features
 * The user first enters a number to start game
<img width="562" alt="Screen Shot 2023-01-13 at 00 00 15" src="https://user-images.githubusercontent.com/111317260/212209654-7b1bfc04-0dde-4bc4-8328-85b9c98f6b00.png">

* The Game has started and the random Battleships are generated by the computer for the user to destroy. The user then has a understanding of the game instructions the computers has to offer.
<img width="537" alt="Screen Shot 2023-01-13 at 00 27 41" src="https://user-images.githubusercontent.com/111317260/212209729-cb779618-f8e0-4a8a-b86a-fcfc27bb4fe2.png">
* The computer gives feedback if the number has already been used or If the user types an error.
<img width="428" alt="Screen Shot 2023-01-13 at 00 35 48" src="https://user-images.githubusercontent.com/111317260/212210943-b55c3a2e-4093-4a95-a5b6-2e7271ccc389.png">
<img width="405" alt="Screen Shot 2023-01-13 at 00 36 37" src="https://user-images.githubusercontent.com/111317260/212210950-39f017c8-55d6-4692-8370-b4b3570e6ca7.png">

* It also  Prints Winner!! when the user has sunk all the battleships ansd the game is over.
<img width="97" alt="Screen Shot 2023-01-13 at 00 41 38" src="https://user-images.githubusercontent.com/111317260/212210962-fa84e143-bb2f-43d0-ac64-493148fc4bd9.png">
# Completed Game 
<img width="572" alt="Screen Shot 2023-01-13 at 00 51 04" src="https://user-images.githubusercontent.com/111317260/212212503-4d7cb9bd-b2e1-46d1-bb88-07dcccb815fb.png">

# Future Features
* Allow users to adjust the amount of battleships they need to destroy which can adjust the number of attempts depending on grid size. 
* Alow the user to adjust the grid size. 

# Bugs

Solved Bugs 
* I had to make 2 seperate random.randrange to generate 2 ships to be located on the grid starting from ship1 (1-46) ship2 (48-99), Originally the location of the ships were pre set but i needed this to be generated everytime the game was reset so the game could be changed everytime.


# Testing 
 * Tested in my local terminal.
 * 

# Remaining Bugs 
  * No bugs remaining.
   
  
# Validator Testing 
  * I used linter to test my python which i fixed a couple of issues but had to leave a couple of minor errors as i could not find logical feedback to fix these issues. The code works prefectly with these minors underlining in the code.  
  

# Deployment 
  * This project was deployed using Code Institutes mock terminal for Heroku.
  
# Credits 
  *
