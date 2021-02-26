# '''
# Is there a strategy for increasing the odds of winning at Rock, Paper, Scissors? If so, does it also work for Rock, Paper, Scissors, Lizard, Spock?

# 1. Calculate the odds of wining if both you (the player) and your opponent randomly guess for every round.
# 2. Calculate the odds of wining if you apply the following stategy:
#     a. if you win a round, repeat your previous choice 
#     b. if you lose a round, play the option that was not previously played (i.e. you: scissors, opponent: rock. On the next round, you: paper)
#     c. If the round results in a draw, make a random choice on the next round  

# Which option results in a higher win rate? 

# The strategy was based on a paper by Wang, et al. where exprimental evidence was gathered to support how evolutionary game theory can be used to describe the dynamical behavior of the classic Rock, Paper, Scissor game. They observed that winners tend to repeat the action that resulted in a win, and randomly choose a new option if they lost on the previous round.

# This project was inspired by Numberphile's video on YouTube: Winning at Rock Paper Scissors - Numberphile
# available here: https://youtu.be/rudzYPHuewc    

# Ref: Physica A: Statistical Mechanics and its Applications, Volume 392, Issue 20, 15 October 2013, Pages 4997-5005
# available here: https://arxiv.org/abs/1301.3238v3

# ''' 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
# start_time = time.time()

# Make payout matrix/dataframe for all possible outcomes:
# 0 = loss, 1 = draw, 2 = win, row index = player choices (Rock, Paper or Scissors), column index = opponent choices (Rock, Paper or Scissors)

payout = np.array([[1, 0, 2], 
                    [2, 1, 0], 
                    [0, 2, 1]])
RPS = ['Rock', 'Paper', 'Scissors']
mat = pd.DataFrame(payout, columns = RPS, index= RPS)

# initialize accumulators for outcomes and outcome rates 
draw = 0
win = 0
loss = 0
win_rate = []
loss_rate = []
draw_rate = []
player_RPS_rand = []
opponent_RPS_rand = []


draw_strat = 0
win_strat = 0
loss_strat = 0
win_rate_strat = []
loss_rate_strat = []
draw_rate_strat = []
player_RPS_strat = []
opponent_RPS_strat = []

sims = 100000 # Number of simulations to run 

# you (player) and opponent make a random choice for each round  
for i in range (1, sims+1):
    player = np.random.choice(RPS)
    opponent = np.random.choice(RPS)
    player_RPS_rand.append(player)
    opponent_RPS_rand.append(opponent)
    if mat.loc[player][opponent] ==0:
        loss+= 1
    elif mat.loc[player][opponent] ==1:
        draw+= 1
    elif mat.loc[player][opponent] ==2:
        win+= 1
    win_rate.append(win/i) 
    loss_rate.append(loss/i)
    draw_rate.append(draw/i)

# print ('wins (%, random): {:.2f}\n'.format((win/sims)*100), 'loses (%, random): {:.2f}\n'.format((loss/sims)*100), 'draws(%, random): {:.2f}\n'.format((draw/sims)*100))

# Apply the strategy.
# For the 1st round, both you (player) and opponent make a random choice of what to play 
player = np.random.choice(RPS)
opponent = np.random.choice(RPS)

for j in range (1, sims+1):
    player_RPS_strat.append(player)
    opponent_RPS_strat.append(opponent)
    if mat.loc[player][opponent] ==0:
        loss_strat+= 1
        RPS_new = RPS.copy()
        for k in [player, opponent]:
            RPS_new.remove(k)
        opponent = opponent
        player = RPS_new[0]
        # if you loose the round, play the option that was not played on the next round.
        # Assume that the opponent will repeat their answer on the next round    

    elif mat.loc[player][opponent] ==1:
        draw_strat+= 1
        player = np.random.choice(RPS)
        opponent = np.random.choice(RPS)
        # if the round results in a draw, both player and opponent ramdomly choose an option on the next round. 

    elif mat.loc[player][opponent] ==2:
        win_strat+= 1
        player = player
        opponent = np.random.choice(RPS)
        # if you win the round, repeat your answer on the next round.
        # the opponent will randomly choose their answer on the next round 

    win_rate_strat.append(win_strat/j) 
    loss_rate_strat.append(loss_strat/j)
    draw_rate_strat.append(draw_strat/j)

# print ('wins (%, w/strat.): {:.2f}\n'.format((win_strat/sims)*100), 'loses (%, w/strat.): {:.2f}\n'.format((loss_strat/sims)*100), 'draws(%, w/strat.): {:.2f}\n'.format((draw_strat/sims)*100))

# Establish all accumulators for the player and opponent in RPS for both the random guesssing and applying Wang et al.'s strategy   
player_RPS_rand_Rock = 0
player_RPS_rand_Paper = 0
player_RPS_rand_Scissors = 0
opponent_RPS_rand_Rock = 0
opponent_RPS_rand_Paper = 0
opponent_RPS_rand_Scissors = 0

for i in player_RPS_rand:
    if i == RPS[0]:
        player_RPS_rand_Rock+=1
    elif i == RPS[1]:
        player_RPS_rand_Paper+=1
    elif i == RPS[2]:
        player_RPS_rand_Scissors+=1

for i in opponent_RPS_rand:
    if i == RPS[0]:
        opponent_RPS_rand_Rock+=1
    elif i == RPS[1]:
        opponent_RPS_rand_Paper+=1
    elif i == RPS[2]:
        opponent_RPS_rand_Scissors+=1

player_RPS_strat_Rock = 0
player_RPS_strat_Paper = 0
player_RPS_strat_Scissors = 0
opponent_RPS_strat_Rock = 0
opponent_RPS_strat_Paper = 0
opponent_RPS_strat_Scissors = 0

for i in player_RPS_strat:
    if i == RPS[0]:
        player_RPS_strat_Rock+=1
    elif i == RPS[1]:
        player_RPS_strat_Paper+=1
    elif i == RPS[2]:
        player_RPS_strat_Scissors+=1

for i in opponent_RPS_strat:
    if i == RPS[0]:
        opponent_RPS_strat_Rock+=1
    elif i == RPS[1]:
        opponent_RPS_strat_Paper+=1
    elif i == RPS[2]:
        opponent_RPS_strat_Scissors+=1


# Make payout matrix/dataframe for all possible outcomes:
# 0 = loss, 1 = draw, 2 = win, row index = player choices (Rock, Paper, Scissors, Lizard, Spock), column index = opponent choices (Rock, Paper, Scissors, Lizard, Spock)
results_mat = np.array([[0,-1, 1, 1, -1],
                        [1, 0, -1, -1, 1],
                        [-1, 1, 0, 1, -1],
                        [-1, 1, -1, 0, 1],
                        [1, -1, 1, -1, 0]]) +1
RPSLS = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
mat_RPSLS = pd.DataFrame(results_mat, index = RPSLS, columns = RPSLS)

# initialize accumulators for outcomes and outcome rates 
draw_RPSLS = 0
win_RPSLS = 0
loss_RPSLS = 0
win_rate_RPSLS = []
loss_rate_RPSLS = []
draw_rate_RPSLS = []
player_RPSLS_rand = []
opponent_RPSLS_rand = []

draw_strat_RPSLS = 0
win_strat_RPSLS = 0
loss_strat_RPSLS = 0
win_rate_strat_RPSLS = []
loss_rate_strat_RPSLS = []
draw_rate_strat_RPSLS = []
player_RPSLS_strat = []
opponent_RPSLS_strat = []

# you (player) and opponent make a random choice for each round  
for i in range (1, sims+1):
    player = np.random.choice(RPSLS)
    opponent = np.random.choice(RPSLS)
    player_RPSLS_rand.append(player)
    opponent_RPSLS_rand.append(opponent)
    if mat_RPSLS.loc[player][opponent] ==0:
        loss_RPSLS+= 1
    elif mat_RPSLS.loc[player][opponent] ==1:
        draw_RPSLS+= 1
    elif mat_RPSLS.loc[player][opponent] ==2:
        win_RPSLS+= 1
    win_rate_RPSLS.append(win_RPSLS/i) 
    loss_rate_RPSLS.append(loss_RPSLS/i)
    draw_rate_RPSLS.append(draw_RPSLS/i)

# print ('wins (%, random): {:.2f}\n'.format((win_RPSLS/sims)*100), 'loses (%, random): {:.2f}\n'.format((loss_RPSLS/sims)*100), 'draws(%, random): {:.2f}\n'.format((draw_RPSLS/sims)*100))

# Apply the strategy.
# For the 1st round, both you (player) and opponent make a random choice of what to play 
player = np.random.choice(RPSLS)
opponent = np.random.choice(RPSLS)

for j in range (1, sims+1):
    player_RPSLS_strat.append(player)
    opponent_RPSLS_strat.append(opponent)
    RPSLS_rem=[]
    if mat_RPSLS.loc[player][opponent] ==0:
        loss_strat_RPSLS+= 1
        RPSLS_new = RPSLS.copy()
        for k in [player, opponent]:
            RPSLS_new.remove(k)
        for i in RPSLS_new:
            if mat_RPSLS.loc[i][opponent] ==2:
                RPSLS_rem.append(i)
        opponent = opponent
        player = np.random.choice(RPSLS_rem)
        # if you loose the round, play the option that was not played on the next round. In this case, there would be two remaining options to choose from. 
        # Assume that the opponent will repeat their answer on the next round    

    elif mat_RPSLS.loc[player][opponent] ==1:
        draw_strat_RPSLS+= 1
        player = np.random.choice(RPSLS)
        opponent = np.random.choice(RPSLS)
        # if the round results in a draw, both player and opponent ramdomly choose an option on the next round. 

    elif mat_RPSLS.loc[player][opponent] ==2:
        win_strat_RPSLS+= 1
        player = player
        opponent = np.random.choice(RPSLS)
        # if you win the round, repeat your answer on the next round.
        # the opponent will randomly choose their answer on the next round 

    win_rate_strat_RPSLS.append(win_strat_RPSLS/j) 
    loss_rate_strat_RPSLS.append(loss_strat_RPSLS/j)
    draw_rate_strat_RPSLS.append(draw_strat_RPSLS/j)

# print ('wins (%, w/strat.): {:.2f}\n'.format((win_strat_RPSLS/sims)*100), 'loses (%, w/strat.): {:.2f}\n'.format((loss_strat_RPSLS/sims)*100), 'draws(%, w/strat.): {:.2f}\n'.format((draw_strat_RPSLS/sims)*100))

# Establish all accumulators for the player and opponent RPSLS in both the random guesssing and applying Wang et al.'s strategy   

player_RPSLS_rand_Rock = 0
player_RPSLS_rand_Paper = 0
player_RPSLS_rand_Scissors = 0
player_RPSLS_rand_Lizard = 0
player_RPSLS_rand_Spock = 0

opponent_RPSLS_rand_Rock = 0
opponent_RPSLS_rand_Paper = 0
opponent_RPSLS_rand_Scissors = 0
opponent_RPSLS_rand_Lizard = 0
opponent_RPSLS_rand_Spock = 0

for i in player_RPSLS_rand:
    if i == RPSLS[0]:
        player_RPSLS_rand_Rock+=1
    elif i == RPSLS[1]:
        player_RPSLS_rand_Paper+=1
    elif i == RPSLS[2]:
        player_RPSLS_rand_Scissors+=1
    elif i == RPSLS[3]:
        player_RPSLS_rand_Lizard+=1
    elif i == RPSLS[4]:
        player_RPSLS_rand_Spock+=1

for i in opponent_RPSLS_rand:
    if i == RPSLS[0]:
        opponent_RPSLS_rand_Rock+=1
    elif i == RPSLS[1]:
        opponent_RPSLS_rand_Paper+=1
    elif i == RPSLS[2]:
        opponent_RPSLS_rand_Scissors+=1
    elif i == RPSLS[3]:
        opponent_RPSLS_rand_Lizard+=1
    elif i == RPSLS[4]:
        opponent_RPSLS_rand_Spock+=1

player_RPSLS_strat_Rock = 0
player_RPSLS_strat_Paper = 0
player_RPSLS_strat_Scissors = 0
player_RPSLS_strat_Lizard = 0
player_RPSLS_strat_Spock = 0

opponent_RPSLS_strat_Rock = 0
opponent_RPSLS_strat_Paper = 0
opponent_RPSLS_strat_Scissors = 0
opponent_RPSLS_strat_Lizard = 0
opponent_RPSLS_strat_Spock = 0

for i in player_RPSLS_strat:
    if i == RPSLS[0]:
        player_RPSLS_strat_Rock+=1
    elif i == RPSLS[1]:
        player_RPSLS_strat_Paper+=1
    elif i == RPSLS[2]:
        player_RPSLS_strat_Scissors+=1
    elif i == RPSLS[3]:
        player_RPSLS_strat_Lizard+=1
    elif i == RPSLS[4]:
        player_RPSLS_strat_Spock+=1

for i in opponent_RPSLS_strat:
    if i == RPSLS[0]:
        opponent_RPSLS_strat_Rock+=1
    elif i == RPSLS[1]:
        opponent_RPSLS_strat_Paper+=1
    elif i == RPSLS[2]:
        opponent_RPSLS_strat_Scissors+=1
    elif i == RPSLS[3]:
        opponent_RPSLS_strat_Lizard+=1
    elif i == RPSLS[4]:
        opponent_RPSLS_strat_Spock+=1

# Plot and save figure.
plt.xkcd()

fig, ax  = plt.subplots (nrows = 2, ncols =2, figsize= (20, 16))

chance = [win_rate, loss_rate, draw_rate]
sim= [win_rate_strat, loss_rate_strat, draw_rate_strat]
chance_RPSLS = [win_rate_RPSLS, loss_rate_RPSLS, draw_rate_RPSLS]
sim_RPSLS= [win_rate_strat_RPSLS, loss_rate_strat_RPSLS, draw_rate_strat_RPSLS]
colors  = ['r', 'g', 'b']
label_rand = ['Win Rate', 'Loss Rate', 'Draw Rate']

alpha = 0.4

for i in range (len(chance)):
    ax[0,0].plot(range(sims), chance_RPSLS[i], c =colors[i], label = '{} (random, {:.2f})'.format(label_rand[i], chance_RPSLS[i][-1]))
    ax[0,0].plot(range(sims), sim_RPSLS[i], c =colors[i], linestyle = ':', label = '{} (w/ strategy, {:.2f})'.format(label_rand[i], sim_RPSLS[i][-1]))
    ax[0,1].plot(range(sims), chance[i], c =colors[i], label = '{} (random, {:.2f})'.format(label_rand[i], chance[i][-1]), alpha = alpha)
    ax[0,1].plot(range(sims), sim[i], c =colors[i], linestyle = ':', label = '{} (w/ strategy, {:.2f})'.format(label_rand[i], sim[i][-1]), alpha = alpha)
# ax[0,0].legend(loc = 'upper left', mode = 'expand')
bb_1 = (fig.subplotpars.left+0.005, fig.subplotpars.top+0.02,  #add 0.015 to left
      fig.subplotpars.right/2-fig.subplotpars.left,0.1)

ax[0,0].legend(bbox_to_anchor=bb_1, mode="expand", loc="lower left",
               ncol=3, borderaxespad=-2, bbox_transform=fig.transFigure, prop={"size":11})


bb_2 = (fig.subplotpars.right/2+0.1, fig.subplotpars.top+0.02, 
      fig.subplotpars.right/2-fig.subplotpars.left,0.1)

ax[0,1].legend(bbox_to_anchor=bb_2, mode="expand", loc="lower left",
               ncol=3, borderaxespad=-2, bbox_transform=fig.transFigure, prop={"size":11})

ax[0,0].set_title('Rock, Paper, Scissors, Lizard, Spock',Fontsize = 16, fontweight='bold')
ax[0,0].set_ylabel('Outcome Rate', FontSize = 16, fontweight='bold')

ax[0,0].set_xlabel('Number of Simulations', FontSize = 16, fontweight='bold')

ax[0,1].set_title('Rock, Paper, Scissors',Fontsize = 16, fontweight='bold')
# ax[0,1].set_ylabel('Outcome Rate', FontSize = 16)
ax[0,1].set_xlabel('Number of Simulations', FontSize = 16, fontweight='bold')

width = 0.2  # the width of the bars

bars_RPSLS1 = [player_RPSLS_rand_Rock, player_RPSLS_rand_Paper, player_RPSLS_rand_Scissors, player_RPSLS_rand_Lizard, player_RPSLS_rand_Spock]
bars_RPSLS2 = [opponent_RPSLS_rand_Rock, opponent_RPSLS_rand_Paper, opponent_RPSLS_rand_Scissors, opponent_RPSLS_rand_Lizard, opponent_RPSLS_rand_Spock]
bars_RPSLS3 = [player_RPSLS_strat_Rock, player_RPSLS_strat_Paper, player_RPSLS_strat_Scissors, player_RPSLS_strat_Lizard, player_RPSLS_strat_Spock]
bars_RPSLS4 = [opponent_RPSLS_strat_Rock, opponent_RPSLS_strat_Paper, opponent_RPSLS_strat_Scissors, opponent_RPSLS_strat_Lizard, opponent_RPSLS_strat_Spock]

# Set position of bar on X axis
r_RPSLS1 = np.arange(len(RPSLS))
r_RPSLS2 = [x + width for x in r_RPSLS1]
r_RPSLS3 = [x + width for x in r_RPSLS2]
r_RPSLS4 = [x + width for x in r_RPSLS3]

ax[1,0].bar(r_RPSLS1, bars_RPSLS1, width=width, label='Player (random)')
ax[1,0].bar(r_RPSLS2, bars_RPSLS2, width=width, label='Opponent (random)')
ax[1,0].bar(r_RPSLS3, bars_RPSLS3, width=width, label='Player (w/ strategy)')
ax[1,0].bar(r_RPSLS4, bars_RPSLS4, width=width, label='Opponent (w/ strategy)')
ax[1,0].set_ylabel('Outcome Count', FontSize = 16, fontweight='bold')

ax[1,0].set_ylim([0, 40000])
bb_3 = (fig.subplotpars.left+0.015, (fig.subplotpars.top/2)+0.02, 
      fig.subplotpars.right/2.1-fig.subplotpars.left,0.1)

ax[1,0].legend(bbox_to_anchor=bb_3, mode="expand", loc="lower left",
               ncol=4, borderaxespad=-4.1, bbox_transform=fig.transFigure, prop={"size":11})

plt.sca(ax[1,0])
plt.xticks([z + width for z in range(len(bars_RPSLS1))], RPSLS, ha = 'left')

# ax[0,1]=plt.legend()

bars_RPS1 = [player_RPS_rand_Rock, player_RPS_rand_Paper, player_RPS_rand_Scissors]
bars_RPS2 = [opponent_RPS_rand_Rock, opponent_RPS_rand_Paper, opponent_RPS_rand_Scissors]
bars_RPS3 = [player_RPS_strat_Rock, player_RPS_strat_Paper, player_RPS_strat_Scissors]
bars_RPS4 = [opponent_RPS_strat_Rock, opponent_RPS_strat_Paper, opponent_RPS_strat_Scissors]

# Set position of bar on X axis
r_RPS1 = np.arange(len(RPS))
r_RPS2 = [x + width for x in r_RPS1]
r_RPS3 = [x + width for x in r_RPS2]
r_RPS4 = [x + width for x in r_RPS3]

ax[1,1].bar(r_RPS1, bars_RPS1, width=width, label='Player (random)', alpha= alpha)
ax[1,1].bar(r_RPS2, bars_RPS2, width=width, label='Opponent (random)',alpha= alpha)
ax[1,1].bar(r_RPS3, bars_RPS3, width=width, label='Player (w/ strategy)', alpha= alpha)
ax[1,1].bar(r_RPS4, bars_RPS4, width=width, label='Opponent (w/ strategy', alpha= alpha)
# ax4 = plt.xlabel('group', fontweight='bold')
ax[1,1].set_ylim([0, 40000])
bb_4 = (fig.subplotpars.right/2+0.11, (fig.subplotpars.top/2)+0.02, 
      fig.subplotpars.right/2.105-fig.subplotpars.left,0.1)

ax[1,1].legend(bbox_to_anchor=bb_4, mode="expand", loc="lower left",
               ncol=4, borderaxespad=-4.1, bbox_transform=fig.transFigure, prop={"size":11})


plt.sca(ax[1,1])
plt.xticks([r + width for r in range(len(bars_RPS1))], RPS, ha = 'left')

fig.suptitle('Applying the Strategy by Wang et al. vs. Randomly Guessing ({:,} simulations)'.format(sims), FontSize = 28, fontweight='bold')
plt.tight_layout()
# plt.savefig('RPSLS_RPS_sim.jpg')
plt.show()

# print("--- %s seconds ---" % (time.time() - start_time))