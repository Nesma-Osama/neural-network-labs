import numpy as np

# TODO [1]: implement the guessing_game function
def guessing_game(max_value:int,attempts:int): # hint: return type is tuple[bool, list[int], int]:
    correct_guess:int=np.random.randint(1,max_value+1)
    user_guess=None
    user_guesses:list[int]=[]
    while attempts >0 and user_guess!=correct_guess:
        try:
            user_guess=int(input(f"Please enter your guess, You have {attempts} attempts "))
            user_guesses.append(user_guess)
            attempts-=1
            if(user_guess==correct_guess):
                print(f"Congratulations your guess are correct with attempts left {attempts}")
                return (True,user_guesses,correct_guess)
            elif(user_guess>correct_guess):
                 print(f"your guess are too High than the correct guess with attempts left {attempts}")
            else : print(f"your guess are too low than the correct guess with attempts left {attempts}")     
        except ValueError:
            print("You must enter a number only  try again")
            continue    
    return (False,user_guesses,correct_guess)    
        
        

# TODO [2]: implement the play_game function
def play_game()-> None:
    max_value:int = 20
    attempts:int = 5
    result=guessing_game(max_value,attempts)
    is_win:bool=result[0]
    #print(result[0],result[1],result[2])
    if(is_win):
        assert result[2] in result[1], "❌ Error: Winning number not found in guesses!"
        return
    else: 
        assert result[2] not in result[1], "❌ Error: Losing player guessed the correct number!"
        answer = input("Do you want to play again? (yes/no): ").strip().lower()
        if(answer.lower()=="yes"):
            play_game()
        else :return    
            
        
        
    