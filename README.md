# RPSLS_Simulation
Is there a strategy for increasing the odds of winning at Rock, Paper, Scissors? If so, does it also work for Rock, Paper, Scissors, Lizard, Spock? I think there is!

1. Calculate the odds of wining if both you (the player) and your opponent randomly guess for every round.
2. Calculate the odds of wining if you apply the following stategy:
    a. if you win a round, repeat your previous choice 
    b. if you lose a round, play the option that was not previously played (i.e. you: scissors, opponent: rock. On the next round, you: paper)
    c. If the round results in a draw, make a random choice on the next round  

Which option results in a higher win rate? 


After 100,000 simulations, the win rate vs. randomly guessing for:
    RPS: 33% --> 50%
    RPSLS: 40% --> 57%

The strategy was based on a paper by Wang, et al. where exprimental evidence was gathered to support how evolutionary game theory can be used to describe the dynamical behavior of the classic Rock, Paper, Scissor game. They observed that winners tend to repeat the action that resulted in a win, and randomly choose a new option if they lost on the previous round.

This project was inspired by Numberphile's video on YouTube: Winning at Rock Paper Scissors - Numberphile
available here: https://youtu.be/rudzYPHuewc    

Ref: Physica A: Statistical Mechanics and its Applications, Volume 392, Issue 20, 15 October 2013, Pages 4997-5005
available here: https://arxiv.org/abs/1301.3238v3
