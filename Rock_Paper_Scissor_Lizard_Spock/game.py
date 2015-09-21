import random


#Taking User's Input
print 'Enter your choice'+':'+' '+'Rock, Paper, Scissor, Lizard, Spock';
user_choice = raw_input().lower();
print "Your choice:"+" "+user_choice.upper();

list = ['Rock', 'Paper', 'Scissor', 'Lizard', 'Spock'];
#Taking Computer's Input
computer_choice = random.choice(list).lower();
print "Computer choice:"+" "+computer_choice.upper();

if (user_choice=='rock'):
    if(computer_choice=='rock'):
        print "Oops! There's a Tie!";
    elif(computer_choice=='paper'):
        print 'Sorry! You loose the game!';
    elif(computer_choice=='scissor'):
        print 'Congratulations! You win the game!';
    elif(computer_choice=='lizard'):
        print 'Congratulations! You win the game!';
    else:
        print 'Sorry! You loose the game!';

elif (user_choice=='paper'):
    if(computer_choice=='rock'):
        print 'Congratulations! You win the game!';
    elif(computer_choice=='paper'):
        print "Oops! There's a Tie!";
    elif(computer_choice=='scissor'):
        print 'Sorry! You loose the game!';
    elif(computer_choice=='lizard'):
        print 'Sorry! You loose the game!';
    else:
        print 'Congratulations! You win the game!';

elif (user_choice=='scissor'):
    if(computer_choice=='rock'):
        print 'Sorry! You loose the game!';
    elif(computer_choice=='paper'):
        print 'Congratulations! You win the game!';
    elif(computer_choice=='scissor'):
        print "Oops! There's a Tie!";
    elif(computer_choice=='lizard'):
        print 'Congratulations! You win the game!';
    else:
        print 'Sorry! You loose the game!';

elif (user_choice=='lizard'):
    if(computer_choice=='rock'):
        print 'Sorry! You loose the game!';
    elif(computer_choice=='paper'):
        print 'Congratulations! You win the game!';
    elif(computer_choice=='scissor'):
        print 'Sorry! You loose the game!';
    elif(computer_choice=='lizard'):
        print "Oops! There's a Tie!";
    else:
        print 'Congratulations! You win the game!';

elif (user_choice=='spock'):
    if(computer_choice=='rock'):
        print 'Congratulations! You win the game!';
    elif(computer_choice=='paper'):
        print 'Sorry! You loose the game!';
    elif(computer_choice=='scissor'):
        print 'Congratulations! You win the game!';
    elif(computer_choice=='lizard'):
        print 'Sorry! You loose the game!';
    else:
        print "Oops! There's a Tie!";

else:
    print "You made an incorrect choice";