# Global vars
current_loc = [0,29]
bad_moves = [[-1, 29]]

#Makes the map
y0_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
for x in y0_list:
        bad_moves.append([x, 0])
y1_list = [0, 12, 18, 22, 31]
for x in y1_list:
        bad_moves.append([x, 1])
y2_list = [0, 2, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 28, 30]
for x in y2_list:
        bad_moves.append([x, 2])
y3_list = [0, 2, 4, 14, 20, 22, 24, 26, 28, 30]
for x in y3_list:
        bad_moves.append([x, 3])
y4_list = [0, 1, 2, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 22, 23, 24, 26, 27, 28, 30]
for x in y4_list:
        bad_moves.append([x, 4])
y5_list = [0, 4, 14, 18, 30]
for x in y5_list:
        bad_moves.append([x, 5])
y6_list = [0, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30]
for x in y6_list:
        bad_moves.append([x, 6])
y7_list = [0, 2, 4, 10, 12, 16, 22, 24, 26, 30]
for x in y7_list:
        bad_moves.append([x, 7])
y8_list = [0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 24, 26, 27, 28, 30]
for x in y8_list:
        bad_moves.append([x, 8])
y9_list = [0, 2, 6, 8, 18, 20, 22, 24, 28, 30]
for x in y9_list:
        bad_moves.append([x, 9])
y10_list = [0, 2, 4, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 20, 22, 24, 26, 27, 28, 30]
for x in y10_list:
        bad_moves.append([x, 10])
y11_list = [0, 4, 6, 10, 20, 26, 30]
for x in y11_list:
        bad_moves.append([x, 11])
y12_list = [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20, 22, 24, 25, 26, 27, 28, 29, 30]
for x in y12_list:
        bad_moves.append([x, 12])
y13_list = [0, 4, 6, 14, 18, 20, 22, 28, 30]
for x in y13_list:
        bad_moves.append([x, 13])
y14_list = [0, 2, 3, 4, 6, 7, 8, 9, 10, 12, 14, 15, 16, 17, 18, 20, 22, 23, 24, 26, 28, 30]
for x in y14_list:
        bad_moves.append([x, 14])
y15_list = [0, 10, 12, 14, 20, 22, 26, 30]
for x in y15_list:
        bad_moves.append([x, 15])
y16_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 14, 15, 16, 18, 20, 22, 24, 25, 26, 27, 28, 30]
for x in y16_list:
        bad_moves.append([x, 16])
y17_list = [0, 2, 4, 8, 14, 18, 22, 26, 30]
for x in y17_list:
        bad_moves.append([x, 17])
y18_list = [0, 2, 4, 5, 6, 8, 10, 11, 12, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 30]
for x in y18_list:
        bad_moves.append([x, 18])
y19_list = [0, 6, 8, 12, 14, 20, 24, 28]
for x in y19_list:
        bad_moves.append([x, 19])
y20_list = [0, 1, 2, 4, 6, 8, 10, 11, 12, 14, 15, 16, 18, 19, 20, 22, 23, 24, 26, 27, 28, 30]
for x in y20_list:
        bad_moves.append([x, 20])
y21_list = [0, 4, 8, 10, 14, 20, 22, 26, 30]
for x in y21_list:
        bad_moves.append([x, 21])
y22_list = [0, 2, 3, 4, 5, 6, 8, 10, 11, 12, 14, 16, 17, 18, 20, 22, 24, 26, 28, 29, 30]
for x in y22_list:
        bad_moves.append([x, 22])
y23_list = [0, 2, 8, 10, 14, 18, 20, 24, 26, 28, 30]
for x in y23_list:
        bad_moves.append([x, 23])
y24_list = [0, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 20, 21, 22, 23, 24, 26, 27, 28, 30]
for x in y24_list:
        bad_moves.append([x, 24])
y25_list = [0, 4, 6, 16, 18, 22, 24, 26, 30]
for x in y25_list:
        bad_moves.append([x, 25])
y26_list = [0, 1, 2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 19, 20, 22, 24, 26, 28, 30]
for x in y26_list:
        bad_moves.append([x, 26])
y27_list = [0, 4, 6, 14, 18, 22, 26, 28, 30]
for x in y27_list:
        bad_moves.append([x, 27])
y28_list = [0, 1, 2, 4, 6, 8, 9, 10, 12, 13, 14, 15, 16, 18, 20, 21, 22, 24, 26, 28, 30]
for x in y28_list:
        bad_moves.append([x, 28])
y29_list = [4, 8, 18, 22, 24, 28, 30]
for x in y29_list:
        bad_moves.append([x, 29])
y30_list = y0_list
for x in y30_list:
        bad_moves.append([x, 30])


def moveCheck():
        # Varibles going to be passed into Player Choices Function
        # Tell whether a move should be offered
        canUp = True
        canDown = True
        canLeft = True
        canRight = True

        #Checks for win
        if current_loc == [30, 1]:
                print("You made it through the maze!")
        #Moves that show up in the bad_moves list are checked for
        else:
                if [current_loc[0], current_loc[1] + 1] in bad_moves:
                        canUp = False
                else:
                        canUp = True
                if [current_loc[0], current_loc[1] - 1] in bad_moves:
                        canDown = False
                else:
                        canDown = True
                if [current_loc[0] - 1, current_loc[1]] in bad_moves:
                        canLeft = False
                else:
                        canLeft = True
                if [current_loc[0] + 1, current_loc[1]] in bad_moves:
                        canRight = False
                else:
                        canRight = True
                move(canUp, canDown, canLeft, canRight)

def move(up, down, left, right):
        # Defs variable to check for move    
        original_loc = current_loc

        # If move is allowed tells the player
        # While the loc hasn't changed takes users answer and tries it until it works
        while original_loc == current_loc:
                print "You can move:%s %s %s %s" %(" Up," if up == True else "", "Down," if down == True else "", "Left," if left == True else "", "Right" if right == True else "")
                response = raw_input("Type your move.")
                response = response.lower()
                if response == "up":
                        response = 'u'
                if response == "down":
                        response = "d"
                if response == "left":
                        response = "l"
                if response == "right":
                        response = "r"

                if response == "u" and up == True:
                        current_loc[1] = current_loc[1] + 1
                        print("Moved Up!")
                        moveCheck()
                elif response == "d" and down == True:
                        current_loc[1] = current_loc[1] - 1
                        print("Moved Down!")
                        moveCheck()
                elif response == "l" and left == True:
                        current_loc[0] = current_loc[0] - 1
                        print("Moved Left!")
                        moveCheck()
                elif response == "r" and right == True:
                        current_loc[0] = current_loc[0] + 1
                        print("Moved Right!")
                        moveCheck()
                else:
                        print("That's not a valid move.")

# Startup

print ("Welcome to the PyMaze!")
print ("Try to make it through the maze without being able to see it")
print ("Hint: Spaces that you move in are the same size as the walls")
start = raw_input("Press enter to start!")
moveCheck()
