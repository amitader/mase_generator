import time
import random
from cell import Cell
class Maze:
    def __init__(self,x1,y1,num_rows,num_cols,cell_size_x,cell_size_y,win=None, seed=None):
        self._cells=[]
        self.x1=x1
        self.y1=y1
        self.num_rows=num_rows
        self.num_cols=num_cols
        self.cell_size_x=cell_size_x
        self.cell_size_y=cell_size_y
        self.win=win
        if seed is not None:
            seed=random.seed(0)
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
        

    def _create_cells(self):
        for i in range(self.num_cols):
            culumn=[]
            for j in range(self.num_rows):
                culumn.append(Cell(self.win))
            self._cells.append(culumn)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i,j)
    
    def _draw_cell(self, i, j):
        if self.win is None:
            return
        start_x=i * self.cell_size_x + self.x1
        start_y=j * self.cell_size_y + self.y1
        end_x=start_x + self.cell_size_x
        end_y=start_y + self.cell_size_y
        self._cells[i][j].draw(start_x, start_y, end_x, end_y)
        self._animate()

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall=False
        self._draw_cell(0,0)
        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall=False
        self._draw_cell(self.num_cols-1,self.num_rows-1)

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited=True
        while True:
            visit_next=[]
            if i>0 and not self._cells[i-1][j].visited:
                visit_next.append((i-1,j))

            if j>0 and not self._cells[i][j-1].visited:
                visit_next.append((i,j-1))

            if i < (self.num_cols-1) and not self._cells[i+1][j].visited:
                visit_next.append((i+1,j))

            if j < (self.num_rows-1) and not self._cells[i][j+1].visited:
                visit_next.append((i,j+1))

            if len(visit_next) == 0:
                self._draw_cell(i, j)
                return
            direction_index=random.randrange(len(visit_next))
            next_index=visit_next[direction_index]
            if next_index[0]==i+1:
                self._cells[i][j].has_right_wall=False
                self._cells[i+1][j].has_left_wall=False
            if next_index[0]==i-1:
                self._cells[i][j].has_left_wall=False
                self._cells[i-1][j].has_right_wall=False
            if next_index[1]==j+1:
                self._cells[i][j].has_bottom_wall=False
                self._cells[i][j+1].has_top_wall=False
            if next_index[1]==j-1:
                self._cells[i][j].has_top_wall=False
                self._cells[i][j-1].has_bottom_wall=False
            self._break_walls_r(next_index[0], next_index[1]) 
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
    
    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self,i,j):
        self._animate()
        self._cells[i][j].visited=True
        if (
            i > 0
            and not self._cells[i][j].has_left_wall
            and not self._cells[i - 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        if (
            i < self.num_cols - 1
            and not self._cells[i][j].has_right_wall
            and not self._cells[i + 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        if (
            j > 0
            and not self._cells[i][j].has_top_wall
            and not self._cells[i][j - 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        if (
            j < self.num_rows - 1
            and not self._cells[i][j].has_bottom_wall
            and not self._cells[i][j + 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        return False