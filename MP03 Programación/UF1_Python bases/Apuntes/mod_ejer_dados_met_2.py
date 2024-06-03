import random

player=""
bot= "Bot"
points_player = 0
points_bot = 0

ranking = ""
menu_cabecera = "1)New Game\n2)New Player\n3)Ranking\n4)Exit"

usuario = False
exit= False


while exit== False:
 print(menu_cabecera)
 opc=int(input("Opcion: "))


 if opc == 1:
     if usuario== False:
         print("Player not found, enter name before playing")
         input("Enter to go to menu")

     elif usuario == True:
         #PARTIDA
         points_player= 0
         points_bot= 0
         for i in range (10):
             dado1_player = random.randint(1, 6)
             dado2_player = random.randint(1, 6)
             dado1_bot = random.randint(1, 6)
             dado2_bot = random.randint(1, 6)

             #turno player
             turno = "Dado 1 = {}, Dado 2 = {} Sum= {}".format(dado1_player,dado2_player,dado1_player+dado2_player)
             print("Turno de {}".format(player),"\n",turno)
             if (dado1_player+dado2_player)%2 == 0:
                 if dado1_player>dado2_player:
                     print("Lucky! {} wins +{} points!".format(player,dado1_player)+"\n")
                     points_player += dado1_player
                 else:
                     print("Lucky! {} wins +{} points!".format(player, dado2_player)+"\n")
                     points_player += dado2_player
             else:
                 if dado1_player>dado2_player:
                     print("Unlucky... {} loses -{} points!".format(player,dado2_bot)+"\n")
                     points_player -= dado2_player
                 else:
                     print("Unlucky... {} loses -{} points!".format(player, dado1_player)+"\n")
                     points_player -= dado1_player

             #turno bot
             turno = "Dado 1 = {}, Dado 2 = {} Sum= {}".format(dado1_bot, dado2_bot, dado1_bot + dado2_bot)
             print("Turno de {}".format(bot), "\n",turno)
             if (dado1_bot+dado2_bot)%2 == 0:
                 if dado1_bot>dado2_bot:
                     print("Lucky! {} wins +{} points!".format(bot,dado1_bot)+"\n")
                     points_bot += dado1_bot
                 else:
                     print("Lucky! {} wins +{} points!".format(bot, dado2_bot)+"\n")
                     points_bot += dado2_bot


             else:
                 if dado1_bot > dado2_bot:
                     print("Unlucky... {} loses -{} points!".format(bot, dado2_bot)+"\n")
                     points_bot -= dado2_bot
                 else:
                     print("Unlucky... {} loses -{} points!".format(bot, dado1_bot)+"\n")
                     points_bot -= dado1_bot
             print("Points {} = {}".format(bot, points_bot) + "\n" + "Points {} = {}".format(player, points_player) + "\n")


          #si el player gana, ingresar puntos
         if points_player>points_bot:
             print(""*30,"\n","{} WINS !!!!!!!".format(player),"\n",""*30)
             print("cuenta de ; es igual a ",ranking.count(";"))
             print(ranking)
             if ranking.count(";")==0:
                 ranking = player + ":" + str(points_player) + ";"
                 print("0 a 1")

             elif ranking.count(";")>0:
                 for i in range(ranking.count(";")):
                     print("i es igual a",i)
                     if i == 0:
                         inicionombre = 0
                         finalnombre = ranking.index(":")
                         iniciopuntos = ranking.index(":") + 1
                         finalpuntos = ranking.index(";")

                     elif i!=0:
                         inicionombre = ranking.index(";", finalnombre) + 1
                         finalnombre = ranking.index(":", finalnombre + 1)
                         iniciopuntos = ranking.index(":", finalpuntos) + 1
                         finalpuntos = ranking.index(";", finalpuntos + 1)
                         print(points_player, " comparado con " , ranking[iniciopuntos:finalpuntos])

                     if points_player > int(ranking[iniciopuntos:finalpuntos]):
                         ranking = ranking[:inicionombre] + player + ":" + str(points_player) + ";" + ranking[inicionombre:]
                         print("2 a 1")
                         break
                     elif int(ranking[iniciopuntos:finalpuntos]) == points_player:
                         ranking = ranking[:finalpuntos + 1] + player + ":" + str(points_player) + ";" + ranking[finalpuntos + 1:]
                         print("2 a 2")
                         break
                     elif int(ranking[iniciopuntos:finalpuntos]) > points_player and i == ranking.count(";") - 1:
                         ranking = ranking[:finalpuntos + 1] + player + ":" + str(points_player) + ";"
                         print("2 a 3")
                         break

             usuario = False

         else:
             print(""*30,"\n","{} WINS !!!!!!!".format(bot),"\n",""*30)
             usuario = False

 elif opc==2:
    player = input("Insert player name: ")
    usuario = True
#RANKING
 elif opc==3:
     cabecera_ranking= "RANKING".center(30,"*")+"\n"
     print(cabecera_ranking)
     print(ranking)
     for i in range(ranking.count(";")):
         if i == 0:
             inicionombre = 0
             finalnombre = ranking.index(":")
             iniciopuntos = ranking.index(":") + 1
             finalpuntos = ranking.index(";")

         else:
             inicionombre = ranking.index(";", finalnombre) + 1
             finalnombre = ranking.index(":", finalnombre + 1)
             iniciopuntos = ranking.index(":", finalpuntos) + 1
             finalpuntos = ranking.index(";", finalpuntos + 1)

         print(ranking[inicionombre:finalnombre].ljust(20), ranking[iniciopuntos:finalpuntos].rjust(10))
     print("*"*30)

 elif opc==4:
     exit= True
