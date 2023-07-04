


class Diffusion:

    """
    This is a class for simulating diffusion in a two-dimensional space.
    
    Attributes:
        - rows (int): The number of rows in the space.
        - cols (int): The number of columns in the space.
        - bc_settings (list): A list of boundary condition settings for each of the 4 borders.
        - left_bc (list): A list containing boundary condition values of type float for the left border.
        - rightbc (list): A list containing boundary condition values of type float for the right border.
        - top_bc (list): A list containing boundary condition values of type float for the top border.
        - bottom_bc (list): A list containing boundary condition values of type float for the bottom border.
        - space (list): A 2D array of type list, representing the state of the material.
    
    """

    
    def __init__(self, rows = 10, cols = 10, bc_settings = [1,1,1,1], left_bc = None, right_bc = None, top_bc = None, bottom_bc = None):
        """
        The constructor for Diffusion class. 
        """
        
        self.rows = int(rows) if rows else 10
        self.cols = int(cols) if cols  else 10
        self.bc_settings = [int(i) for  i in bc_settings] if bc_settings else [1,1,1,1]
        self.left_bc = [float(i) for i in left_bc] if left_bc else [0.0]*self.rows
        self.right_bc = [float(i) for i in right_bc] if right_bc else [0.0]*self.rows
        self.top_bc = [float(i) for i in top_bc] if top_bc else [0.0]*self.cols
        self.bottom_bc = [float(i) for i in bottom_bc] if bottom_bc else [0.0]*self.cols
        self.space = [[0.0 for i in range(0, cols)] for j in range(0,rows)]
    
    
    def set_cell(self, row_range, col_range, value):
        """
        Modifies the state of cells in the material by modifying the space attribute

        Parameters:
            row_range (list): The selected rows, list containing values of type int
            col_range (list): The selected columns, list containing values of type int
            value (float): The value to set the selected cells to.
          
        """
        
        # to set selected cells to value specified
        for i in range(row_range[0], row_range[1]+1):
            for j in range(col_range[0],col_range[1]+1):
                self.space[i][j] = float(value)
                
    
    def print_space(self):
        """
        To view the current state of the material
        """
        
        for i in range(self.rows):
            for j in range(self.cols): 
                print(f'{self.space[i][j]:1.4f}', end=' ')
            print()       
                    
    
    def next_step(self, time_steps):
        """
        Simulates diffusion through the material depending on the number of time_steps. 
        Modifies space attribute to represent the current state of the material after diffusion

        Parameters:
            time_steps (int): number of time steps to run simulation through
        
          
        """
        
              
        # calculate diffusion for each time step as specified 
        for n in range(0,time_steps):
            #creating temporary array to store the changes
            change_array = [[0.0 for i in range(0, self.cols)] for j in range(0,self.rows)]
    

        
            # calculating the change of state for each cell in the material
            for i in range(0,self.rows):
                for j in range(0,self.cols):
                    
                    # calculate change of state at left and right boundaries
                    if j == 0 and j != self.cols-1: # left
                        right_cell = self.space[i][j+1]        
 
                        if self.bc_settings[0] == 1:                        # Direchlet
                            left_cell = self.left_bc[i]
                        else:                                               # Neumann
                            left_cell = self.space[i][j+1]-2*self.left_bc[i]
                            
                    elif j == self.cols-1 and j != 0: # right
                        left_cell = self.space[i][j-1]

                        if self.bc_settings[1] == 1:                        # Direchlet
                            right_cell = self.right_bc[i]
                        else:                                               # Neumann
                            right_cell = self.space[i][j-1]+2*self.right_bc[i]
                     
                    elif j == 0 and j == self.cols-1: # for case of vertical 1D array (1 column)
                        # won't work with Neumann boundary conditions based on formula
                        left_cell = self.left_bc[i]
                        right_cell = self.right_bc[i]    
                        
                    else: # for all cells not at left and right boundaries
                        left_cell = self.space[i][j-1]
                        right_cell = self.space[i][j+1]        
                           
                        
                    # check change of state at top and bottom boundaries  
                    if i == 0 and i != self.rows-1: # top 
                        bottom_cell = self.space[i+1][j]

                        if self.bc_settings[2] == 1:                        # Direchlet
                            top_cell = self.top_bc[j]
                        else:                                               # Neumann
                            top_cell = self.space[i+1][j]-2*self.top_bc[j]
                    
                    elif i == self.rows-1 and i !=0: # bottom 
                        top_cell = self.space[i-1][j]
                        if self.bc_settings[3] == 1:                        # Direchlet
                            bottom_cell = self.bottom_bc[j]
                        else:                                               # Neumann
                            bottom_cell = self.space[i-1][j]+2*self.bottom_bc[j]
                    
                    elif i == 0 and i == self.rows-1: # for case of horizontal 1D array (1 row)
                        # won't work with Neumann boundary conditions based on formula
                        top_cell = self.top_bc[j]
                        bottom_cell = self.bottom_bc[j] 
                        
                    else: #for all cells not at top and bottom boundaries
                        top_cell = self.space[i-1][j]
                        bottom_cell = self.space[i+1][j]
                    
                    
                    # changes in x and y direction     
                    # left and right cell refer to j-1 and j+1
                    # top and bottom cell refer to i-1 and i+1
                    x_change = right_cell - 2*self.space[i][j] + left_cell 
                    y_change = bottom_cell - 2*self.space[i][j] + top_cell

                    change_array[i][j] = x_change + y_change
                    
            # adding changes of all cells to corresponding cell in space. 
            # space attribute is updated with new values after diffusion
            for  i in range(0,self.rows):
                for j in range(0,self.cols):
                    self.space[i][j] =  self.space[i][j] + 0.0001*(change_array[i][j])
            



            

