from graphics import  Point, Line
class Cell:
    def __init__(self, win=None):
        self.has_left_wall=True
        self.has_right_wall=True
        self.has_top_wall=True
        self.has_bottom_wall=True
        self._x1=None
        self._x2=None
        self._y1=None
        self._y2=None
        self._win=win
        self.visited=False
    def draw(self,x1,y1,x2,y2):
        if self._win is None:
            return
        self._x1=x1
        self._x2=x2
        self._y1=y1
        self._y2=y2


        line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        if self.has_left_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line,"white")

        line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        if self.has_right_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line,"white")
        
        line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        if self.has_top_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line,"white")

        line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        if self.has_bottom_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line,"white")
    
    def draw_move(self, to_cell, undo=False):
        start_x=(abs(self._x2 - self._x1)) // 2 + self._x1
        start_y=(abs(self._y2 - self._y1)) // 2 + self._y1
        end_x=(abs(to_cell._x2 - to_cell._x1)) // 2 + to_cell._x1
        end_y=(abs(to_cell._y2 - to_cell._y1)) // 2 + to_cell._y1

        fiil_color = "red"
        if undo:
            fiil_color="grey"

        line=Line(Point(start_x, start_y), Point(end_x, end_y))
        self._win.draw_line(line,fiil_color)
