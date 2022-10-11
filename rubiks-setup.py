class rubiks:
    
    def __init__(self):
        
        self.cube = [[[]*3]*3]*6
        
        self.turnOrder = []
 
        self.cube[0] = [["R","R","R"],["R","R","R"],["R","R","R"]]
        self.cube[1] = [["B","B","B"],["B","B","B"],["B","B","B"]]
        self.cube[2] = [["W","W","W"],["W","W","W"],["W","W","W"]]
        self.cube[3] = [["G","G","G"],["G","G","G"],["G","G","G"]]
        self.cube[4] = [["Y","Y","Y"],["Y","Y","Y"],["Y","Y","Y"]]
        self.cube[5] = [["O","O","O"],["O","O","O"],["O","O","O"]]


    
    
    
    def __str__(self):
        print("") #Spacer
        #Print out the red section
        for x in range(3):
            for y1 in range(3):
                print(" ", end = " ") #Padding
            print("| ", end = "")
            
            for y2 in range(3):
                print("%s" % self.cube[0][x][y2], end = " ") #Red
            print("| ", end = "")    
            print("")
        
        #Print out the underline
        for x in range(1):
            for y1 in range(3):
                print(" ", end = " ")
            for y2 in range(5):
                print("-", end = " ")
            print("")
           
        #Print out the middle section
        for x in range(3):
            for y1 in range(3):
                print("%s" % self.cube[1][x][y1], end = " ") #Blue
            print("| ", end = "")
            for y2 in range(3):
                print("%s" % self.cube[2][x][y2], end = " ") #White
            print("| ", end = "")
            for y3 in range(3):
                print("%s" % self.cube[3][x][y3], end = " ") #Green
            print("| ", end = "")
            for y4 in range(3):
                print("%s" % self.cube[4][x][y4], end = " ") #Yellow
            print("")

        #Print out the underline
        for x in range(1):
            for y1 in range(3):
                print(" ", end = " ")
            for y2 in range(5):
                print("-", end = " ")
            print("")
         
         
        #Print out the orange section
        for x in range(3):
            for y1 in range(3):
                print(" ", end = " ") #Padding
            print("| ", end = "")
            
            for y2 in range(3):
                print("%s" % self.cube[5][x][y2], end = " ") #Orange
            print("| ", end = "") 
            print("")
            
        print("")
        #return("Print complete")
        return("")

    
    def pOrder(self): #Prints the order of turns
        print("Turn order: " + str(self.turnOrder))
    
    def backToOrig(self): #Prints the reverse order of turns
        returnOrder = []
        for each in self.turnOrder:
            if each == "U":
                returnOrder.append("U-")
            if each == "U-":
                returnOrder.append("U")
            if each == "R":
                returnOrder.append("R-")
            if each == "R-":
                returnOrder.append("R")
            if each == "L":
                returnOrder.append("L-")
            if each == "L-":
                returnOrder.append("L")
        print("Order to return back to original: " + str(returnOrder[::-1]))

        
    
    def turn(self, turn):
        if turn == "U":
            self.turnOrder.append("U")
            tempHolder = self.cube[1][0]
            self.cube[1][0] = self.cube[2][0]
            self.cube[2][0] = self.cube[3][0]
            self.cube[3][0] = self.cube[4][0]
            self.cube[4][0] = tempHolder
            
            #Rotate side 0:
            tempHolder2 = self.cube[0][0][0]
            self.cube[0][0][0] = self.cube[0][2][0]
            self.cube[0][2][0] = self.cube[0][2][2]
            self.cube[0][2][2] = self.cube[0][0][2]
            self.cube[0][0][2] = tempHolder2
            
            tempHolder3 = self.cube[0][0][1]
            self.cube[0][0][1] = self.cube[0][1][0]
            self.cube[0][1][0] = self.cube[0][2][1]
            self.cube[0][2][1] = self.cube[0][1][2]
            self.cube[0][1][2] = tempHolder3

            print("Finished turning up")

        if turn == "U-":
            self.turnOrder.append("U-")
            tempHolder = self.cube[2][0]
            self.cube[2][0] = self.cube[1][0]
            self.cube[1][0] = self.cube[4][0]
            self.cube[4][0] = self.cube[3][0]
            self.cube[3][0] = tempHolder
            
            #Rotate side 0:
            tempHolder2 = self.cube[0][0][0]
            self.cube[0][0][0] = self.cube[0][0][2]
            self.cube[0][0][2] = self.cube[0][2][2]
            self.cube[0][2][2] = self.cube[0][2][0]
            self.cube[0][2][0] = tempHolder2
            
            tempHolder3 = self.cube[0][0][1]
            self.cube[0][0][1] = self.cube[0][1][2]
            self.cube[0][1][2] = self.cube[0][2][1]
            self.cube[0][2][1] = self.cube[0][1][0]
            self.cube[0][1][0] = tempHolder3
            
            print("Finished turning up (CC)")


        if turn == "L":
            self.turnOrder.append("L")
            tempHolder1 = self.cube[0][0][0]
            tempHolder2 = self.cube[0][1][0]
            tempHolder3 = self.cube[0][2][0]
            
            self.cube[0][0][0] = self.cube[4][2][2]
            self.cube[0][1][0] = self.cube[4][1][2]
            self.cube[0][2][0] = self.cube[4][0][2]
            
            self.cube[4][0][2] = self.cube[5][2][0]
            self.cube[4][1][2] = self.cube[5][1][0]
            self.cube[4][2][2] = self.cube[5][0][0]
            
            self.cube[5][0][0] = self.cube[2][0][0]
            self.cube[5][1][0] = self.cube[2][1][0]
            self.cube[5][2][0] = self.cube[2][2][0]
            
            self.cube[2][0][0] = tempHolder1
            self.cube[2][1][0] = tempHolder2
            self.cube[2][2][0] = tempHolder3
            
            #Rotate side 1:
            tempHolder4 = self.cube[1][0][0]
            self.cube[1][0][0] = self.cube[1][2][0]
            self.cube[1][2][0] = self.cube[1][2][2]
            self.cube[1][2][2] = self.cube[1][0][2]
            self.cube[1][0][2] = tempHolder4
            
            tempHolder5 = self.cube[1][0][1]
            self.cube[1][0][1] = self.cube[1][1][0]
            self.cube[1][1][0] = self.cube[1][2][1]
            self.cube[1][2][1] = self.cube[1][1][2]
            self.cube[1][1][2] = tempHolder5
            
            print("Finished turning left")
        
        if turn == "L-":
            self.turnOrder.append("L-")
            tempHolder1 = self.cube[0][0][0]
            tempHolder2 = self.cube[0][1][0]
            tempHolder3 = self.cube[0][2][0]
            
            self.cube[0][0][0] = self.cube[2][0][0]
            self.cube[0][1][0] = self.cube[2][1][0]
            self.cube[0][2][0] = self.cube[2][2][0]
            
            self.cube[2][0][0] = self.cube[5][0][0]
            self.cube[2][1][0] = self.cube[5][1][0]
            self.cube[2][2][0] = self.cube[5][2][0]
            
            self.cube[5][0][0] = self.cube[4][2][2]
            self.cube[5][1][0] = self.cube[4][1][2]
            self.cube[5][2][0] = self.cube[4][0][2]
            
            self.cube[4][0][2] = tempHolder3
            self.cube[4][1][2] = tempHolder2
            self.cube[4][2][2] = tempHolder1
            
            #Rotate side 1:
            tempHolder4 = self.cube[1][0][0]
            self.cube[1][0][0] = self.cube[1][0][2]
            self.cube[1][0][2] = self.cube[1][2][2]
            self.cube[1][2][2] = self.cube[1][2][0]
            self.cube[1][2][0] = tempHolder4
            
            tempHolder5 = self.cube[1][0][1]
            self.cube[1][0][1] = self.cube[1][1][2]
            self.cube[1][1][2] = self.cube[1][2][1]
            self.cube[1][2][1] = self.cube[1][1][0]
            self.cube[1][1][0] = tempHolder5
            
            print("Finished turning left (CC)")


        if turn == "R":
            self.turnOrder.append("R")
            tempHolder1 = self.cube[0][0][2]
            tempHolder2 = self.cube[0][1][2]
            tempHolder3 = self.cube[0][2][2]
            
            self.cube[0][0][2] = self.cube[2][0][2]
            self.cube[0][1][2] = self.cube[2][1][2]
            self.cube[0][2][2] = self.cube[2][2][2]
            
            self.cube[2][0][2] = self.cube[5][0][2]
            self.cube[2][1][2] = self.cube[5][1][2]
            self.cube[2][2][2] = self.cube[5][2][2]
            
            self.cube[5][0][2] = self.cube[4][2][0]
            self.cube[5][1][2] = self.cube[4][1][0]
            self.cube[5][2][2] = self.cube[4][0][0]
            
            self.cube[4][0][0] = tempHolder3
            self.cube[4][1][0] = tempHolder2
            self.cube[4][2][0] = tempHolder1
            
            #Rotate side 3:
            tempHolder4 = self.cube[3][0][0]
            self.cube[3][0][0] = self.cube[3][2][0]
            self.cube[3][2][0] = self.cube[3][2][2]
            self.cube[3][2][2] = self.cube[3][0][2]
            self.cube[3][0][2] = tempHolder4
            
            tempHolder5 = self.cube[3][0][1]
            self.cube[3][0][1] = self.cube[3][1][0]
            self.cube[3][1][0] = self.cube[3][2][1]
            self.cube[3][2][1] = self.cube[3][1][2]
            self.cube[3][1][2] = tempHolder5
            
            print("Finished turning right")
        
        if turn == "R-":
            self.turnOrder.append("R-")
            tempHolder1 = self.cube[0][0][2]
            tempHolder2 = self.cube[0][1][2]
            tempHolder3 = self.cube[0][2][2]
            
            self.cube[0][0][2] = self.cube[4][2][0]
            self.cube[0][1][2] = self.cube[4][1][0]
            self.cube[0][2][2] = self.cube[4][0][0]
            
            self.cube[4][0][0] = self.cube[5][2][2]
            self.cube[4][1][0] = self.cube[5][1][2]
            self.cube[4][2][0] = self.cube[5][0][2]
            
            self.cube[5][0][2] = self.cube[2][0][2]
            self.cube[5][1][2] = self.cube[2][1][2]
            self.cube[5][2][2] = self.cube[2][2][2]
            
            self.cube[2][0][2] = tempHolder1
            self.cube[2][1][2] = tempHolder2
            self.cube[2][2][2] = tempHolder3
            
            #Rotate side 3:
            tempHolder4 = self.cube[3][0][0]
            self.cube[3][0][0] = self.cube[3][0][2]
            self.cube[3][0][2] = self.cube[3][2][2]
            self.cube[3][2][2] = self.cube[3][2][0]
            self.cube[3][2][0] = tempHolder4
            
            tempHolder5 = self.cube[3][0][1]
            self.cube[3][0][1] = self.cube[3][1][2]
            self.cube[3][1][2] = self.cube[3][2][1]
            self.cube[3][2][1] = self.cube[3][1][0]
            self.cube[3][1][0] = tempHolder5
            
            print("Finished turning right (CC)")



        


def main():
    #print("Hello World")
    cube1 = rubiks()
    print(cube1)

    print("Welcome to Hersh's Rubiks Cube Simulator.")
    print("Commands: U, L, F, R, B, D. Put a '-' after the letter to signify counter-clockwise")
    print("Enter an empty input to run the commands")
    

    moveList = [] #For input and movement
    validMoves = ["U","L","F","R","B","D","U-","L-","F-","R-","B-","D-"] #validity check

    inp = " "
    while inp != "":
        inp = input().upper()
        if (inp == ""): #Stop the code
            break
        
        elif (inp not in validMoves): #Not in valid move, try again
            print("Not a valid move.")
            
        else:
            moveList.append(inp) #Add to move list
            
            
    for moves in moveList: #Move the cube
        cube1.turn(moves)
        print(cube1)
        
        
    #Output

    print("\nCompleted Cube:\n")
    print(cube1)
    cube1.pOrder()
    cube1.backToOrig()
        

    
    
if __name__ == "__main__":
    main()

