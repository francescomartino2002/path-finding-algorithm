import time
import os

DIM = 20
D = 10 #lenght of a cell 
D2 = 14 # diagonal length of a cell (sqrt(2))

start = (17,17)
goal = (2,2)
open = set()
close = set()

#g -> cost to get from starting node to current node
#h -> heuristic cost to get from current node to end node
#f -> g + h
class Cell:
    def __init__(self, parent, position, g):
        self.parent = parent
        self.position = position
        self.parent_g = g

    def __hash__(self):
        return hash(self.position)

    def __eq__(self, other):
        #self -> node already in the list, other -> node i want to check before adding it to list
        return self.position == other.position and self.f_cost < other.f_cost
       

    def get_costs(self):
        #h_cost
        dx = abs(self.position[0] - goal[0])
        dy = abs(self.position[1] - goal[1])
        self.h_cost = D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)
        #g_cost
        if self.position[0] == self.parent[0] or self.position[1] == self.parent[1]:
            distance = 10
        elif self.position == start:
            distance = 0
        else: distance = 14
        self.g_cost = self.parent_g + distance
        #f
        self.f_cost = self.g_cost + self.h_cost
    

    def successors(self,matrix):
        global found
        for i in range(-1,2):
            for j in range(-1,2):
                if (i != 0 or j != 0) and (self.position[0] + i != self.parent[0] or self.position[1] + j != self.parent[1]) and check_valid_position(self.position[0] + i, self.position[1] + j, matrix):
                    new_node = Cell(self.position, (self.position[0] + i, self.position[1] + j),self.g_cost)
                    new_node.get_costs()
                else: continue
                if new_node in open:
                    continue
                if new_node in close
                    continue
                for z in open.copy():
                    if z.position == new_node.position:
                        open.remove(z)
                        break
                open.add(new_node)
                matrix[new_node.position[0]][new_node.position[1]] = 2
                new_node.check_goal()
                if found:
                    return
    


    def check_goal(self):
        if self.position[0] == goal[0] and self.position[1] == goal[1]:
            close.add(self)
            global found
            found = True

        
def check_valid_position(x,y, matrix):
    if x < 0 or x >= DIM or y < 0 or y >= DIM or matrix[x][y] == 1:
        return False
    else: return True

'''
def print_matrix(matrix):
    for i in range(DIM):
        print(matrix[i])  
'''     
        

found = False

def main(matrix):
    global found
    start_node = Cell(start, start, 0)
    start_node.get_costs()
    open.add(start_node)
    
    current = start_node
    while not found:
        #pick node with lowest f_cost, in case 2 nodes have same f_cost pick the one with lowest h_cost
        current  = min(open, key=lambda Cell: (Cell.f_cost, Cell.h_cost))

        open.remove(current)
        current.successors(matrix)
        '''
        for z in close.copy():
            if z.position == current.position:
                close.remove(z)
                break
        '''
        close.add(current)


    #getting the path
    path = []
    position = goal
    complete = False
    while not complete:
        for i in close:
            if i.position == position:
                path.append(i.position)
                position = i.parent
            if i.position == start and position == start:
                complete = True
                break
    for i in path:
        matrix[i[0]][i[1]] = 3
        #time.sleep(0.1)
    #print_matrix(matrix)


if __name__ == '__main__':
    matrix = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1,1,1,1],
              [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],]

    main(matrix)

   
