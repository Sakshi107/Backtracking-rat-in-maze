N = 4
# prints solution matrix solution
def printsolmatrix( sol ):   
    for i in sol: 
        for j in i: 
            print(str(j) + " ", end ="") 
        print("")  
# IsPossible checks if r, c is valid i.e within the matrix 
def IsPossible( maze, r, c ): 
      
    if r >= 0 and r < N and c >= 0 and c < N and maze[r][c] == 1: 
        return True
    else:
        return False
  
def solvematrix( maze ): 
      
    # Creating a 4 * 4 2-D matrix all 0 since 1 will indicate the path
    sol = [ [ 0 for j in range(4) ] for i in range(4) ] 
      
    if solvematrixUtil(maze, 0, 0, sol) == False: 
        print("Solution doesn't exist"); 
        return False
    print("Solution matrix containing the path is:")     
    printsolmatrix(sol) 
    return True
      
# A recursive function to solve Maze problem 
def solvematrixUtil(maze, r, c, sol): 
      
    # if destination is reached return True 
    if r == N - 1 and c == N - 1: 
        sol[r][c] = 1
        return True
          
    # Check if maze[r][c] is valid 
    if IsPossible(maze, r, c) == True: 
        # mark r, c as part of solution path 
        sol[r][c] = 1
          
        # Move forward in r direction 
        if solvematrixUtil(maze, r + 1, c, sol) == True: 
            return True
              
        # If moving in r direction doesn't give solution  
        # then Move down in c direction 
        if solvematrixUtil(maze, r, c + 1, sol) == True: 
            return True

        # If none of the above movements work then  
        # We use backtracking, unmark r, c as part of solution path 
        sol[r][c] = 0
        return False
if __name__ == "__main__": 
    # Initialising the maze  4*4
    maze = [ [1, 0, 1, 0], 
             [1, 1, 1, 1], 
             [0, 0, 1, 0], 
             [1, 0, 1, 1] ] 
               
    solvematrix(maze) 
