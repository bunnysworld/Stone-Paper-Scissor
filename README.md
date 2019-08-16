# STONE-PAPER-SCISSOR

- algorithm based on 'elif' conditions
- Here is basic ***Algorithm*** which i used here  to compare both ***user*** and ***computer*** input

```python
 elif player_inp == "stone" and comp_inp == "paper":
        print(f"YOUR GUESS IS : {player_inp} AND COMPUTER GUESS IS :{comp_inp}")
        print(" COMPUTER WINS 1 POINT")
        computer_score+=1
        print(f"COMPUTER POINT IS : {computer_score} AND YOUR POINT IS : {player_score}")
```
- after every win ***1*** point is incremented to the winner side

# Module used
>import random

```python
  list=["stone","paper","scissor"]
  comp_inp=random.choice(list)
```
- this ***random.choice()*** function basically store any of the ***one*** random data from the list
## Rules
- >you have only ***five*** number of attempts
- >after each win ***one*** point is incremented to winner side and ***neutral*** to lossing side
- >winner will be announced at the end of the game on the basis of their all over points that they had incremented during each play
- >during case of ***tie*** no point is assigned

## Screenshot
![Screenshot (25)](https://user-images.githubusercontent.com/42912055/63183441-97f91900-c072-11e9-96b6-33a3697eb887.png)


