def gethand(player):
    x=players.index(player)
    return hands[x]


def Round(ingame):
    newingame=[]
    for i in range(0,len(ingame),2):
        if(i==len(ingame)-1):
            newingame.append(i)
        else:
            if gethand(ingame[i])!=gethand(i+1):
                if gethand(ingame[i])=='P' and gethand(ingame[i+1])=='R':
                    newingame.append(ingame[i])
                elif gethand(ingame[i])=='R' and gethand(ingame[i+1])=='P':
                    newingame.append(ingame[i+1])
                elif gethand(ingame[i]) == 'S' and gethand(ingame[i + 1]) == 'P':
                    newingame.append(ingame[i])
                elif gethand(ingame[i]) == 'P' and gethand(ingame[i + 1]) == 'S':
                    newingame.append(ingame[i + 1])
                elif gethand(ingame[i]) == 'R' and gethand(ingame[i + 1]) == 'S':
                    newingame.append(ingame[i])
                elif gethand(ingame[i]) == 'S' and gethand(ingame[i + 1]) == 'R':
                    newingame.append(ingame[i + 1])

    return newingame



players = list(range(11))
hands = ['R', 'R', 'P', 'S', 'R', 'S', 'S', 'R', 'P', 'R', 'S']
ingame = players.copy()
while(len(ingame)>1):
    ingame=Round(ingame)
if(len(ingame)>0):
    print(str(ingame[0])+" is winner")
else:
    print("no winner")













# def compare(player1,player2):
#     if player1 == player2:
#         return
#         tie = +1
#         return tie
#     elif player1 == 'R' and player2 == 'P':
#         return player1
#     elif player1 == 'P' and player2 == 'R':
#         return player2
#     elif player1 == 'S' and player2 == 'P':
#         return player1
#     elif player1 == 'P' and player2 == 'S':
#         return player2
#     elif player1 == 'R' and player2 == 'S':
#         return player1
#     else:
#         return player2
# for i in range(len(hands)):
#     if (hands[i]== hands[i+1]):
#         print ("tie")
#         hands.remove(i)
#         hands.remove(i+1)
#     elif (hands[i]=='R'and hands[i+1]=='P'):
#         print(i+"wins")
#         hands.remove(i+1)



