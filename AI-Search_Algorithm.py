import customtkinter
import time

class Map:
    map_dict={}
    index=1
    start=[]
    goal=[]

    def init(self):
        self.list=[]
    
    def Graphical(self, list:list):
        def heuristic_fun(xcor, ycor, goal_cor):
            x=max(xcor, goal_cor[0])-min(xcor, goal_cor[0])
            y=max(ycor, goal_cor[1])-min(ycor, goal_cor[1])
            nxt=y+x
            return nxt
        
        self.lst=list
        x=0
        y=0
        gx=0
        gy=0
        for self.item in self.lst:
            for i in self.item:
                if i == 4:
                    Map.goal=[gx, gy]
                gy+=1
                if gy == len(self.item):
                    gy=0
                
            gx+=1
            if gx == len(list):
                gx=0

        
        for self.item in self.lst:
            for i in self.item:
                self.object=customtkinter.CTkFrame(window, width=50, height=50, fg_color="white", border_color="grey", border_width=1)
                self.object.grid(row=x, column=y)
                if i == 1:
                    self.object.configure(fg_color="white")
                elif i == 3:
                    self.object.configure(fg_color="blue")
                    Map.start=[x, y]
                elif i == 4:
                    self.object.configure(fg_color="red")
                    Map.goal=[x, y]
                else:
                    self.object.configure(fg_color="black")
                    erx=heuristic_fun(x, y, Map.goal)
                    label=customtkinter.CTkLabel(self.object, text=erx, width=45, height=45)
                    label.grid(row=1, column=1)
                
                Map.map_dict[f"{x};{y}"]=self.object
                Map.index+=1
                y+=1
                if y == len(self.item):
                    y=0
                
            x+=1
            if x == len(list):
                x=0

class Player:
    def __init__(self, map):
        self.x=map.start[0]
        self.y=map.start[1]
        self.movement=0
        self.stop=True
        self.junction=[]
        self.previous=[self.x, self.y]
        self.player=customtkinter.CTkFrame(window, width=50, height=50, fg_color="brown", border_color="grey", border_width=1)
        self.player.grid(row=self.x, column=self.y)
        self.covered=[f"{self.x};{self.y}"]
        self.lst=[]
        self.frontier=[]
        self.lst=map.lst
        self.goal=map.goal
        self.step=0
        self.Astr=[]
        self.Astrstart=False
        self.tupe=False
        
    def Depth_first_Search(self):
        if self.stop:
            tup=[]
            if self.lst[self.x-1][self.y]==0 and f"{self.x-1};{self.y}" not in self.covered:
                self.movement=2
                if [self.x-1,self.y] != self.previous:
                    tup.append([self.x, self.y])
                    self.previous=[self.x, self.y]
                    
            if self.lst[self.x][self.y+1]==0 and f"{self.x};{self.y+1}" not in self.covered:
                self.movement=3
                if [self.x, self.y+1] != self.previous:
                    tup.append([self.x, self.y])
                    self.previous=[self.x, self.y]
                    
            if self.lst[self.x+1][self.y]==0 and f"{self.x+1};{self.y}" not in self.covered:
                self.movement=1
                if [self.x+1, self.y] !=self.previous:
                    tup.append([self.x, self.y])
                    self.previous=[self.x, self.y]
                    
            if self.lst[self.x][self.y-1]==0 and f"{self.x};{self.y-1}" not in self.covered:
                self.movement=4
                if [self.x, self.y-1] != self.previous:
                    tup.append([self.x, self.y])
                    self.previous=[self.x, self.y]                

            if len(tup) > 1:
                self.junction.append(self.previous)
            
            if self.lst[self.x-1][self.y]==4 and f"{self.x-1};{self.y}" not in self.covered:
                self.movement=2
                self.stop=False
                self.frontier.append([self.x-1, self.y])
            if self.lst[self.x][self.y+1]==4 and f"{self.x};{self.y+1}" not in self.covered:
                self.movement=3
                self.stop=False
                self.frontier.append([self.x, self.y+1])
            if self.lst[self.x+1][self.y]==4 and f"{self.x+1};{self.y}" not in self.covered:
                self.movement=1
                self.stop=False
                self.frontier.append([self.x+1, self.y])
            if self.lst[self.x][self.y-1]==4 and f"{self.x};{self.y-1}" not in self.covered:
                self.movement=4
                self.stop=False
                self.frontier.append([self.x, self.y-1])
            ########
            if self.movement == 1:
                self.x+=1
                self.covered.append(f"{self.x};{self.y}")  
                self.player.grid_configure(row=self.x,column=self.y)        
            elif self.movement==2:
                self.x-=1
                self.covered.append(f"{self.x};{self.y}")
                self.player.grid_configure(row=self.x,column=self.y)
            elif self.movement==3:
                self.y+=1
                self.covered.append(f"{self.x};{self.y}")
                self.player.grid_configure(row=self.x,column=self.y)
            elif self.movement==4:
                self.y-=1
                self.covered.append(f"{self.x};{self.y}")
                self.player.grid_configure(row=self.x,column=self.y)
            elif self.movement ==0:
                self.x=self.junction[-1][0]
                self.y=self.junction[-1][1]
                self.player.grid_configure(row=self.x,column=self.y)
                self.junction.remove(self.junction[-1])
            Map.map_dict[self.covered[-1]].configure(fg_color="green")
            self.movement=0
            pass
        else:btn.configure(text="Complete")
    
    def Breadth_first_search(self):
        if self.stop:
        ############################
            tup=[]
            if self.lst[self.x-1][self.y]==0 and f"{self.x-1};{self.y}" not in self.covered:
                self.movement=2
                if [self.x-1,self.y] != self.previous:
                    tup.append([self.x, self.y])
                    self.previous=[self.x, self.y]
                    if [self.x-1, self.y] not in self.frontier:
                        self.frontier.append([self.x-1, self.y])
                    
            if self.lst[self.x][self.y+1]==0 and f"{self.x};{self.y+1}" not in self.covered:
                self.movement=3
                if [self.x, self.y+1] != self.previous:
                    tup.append([self.x, self.y])
                    self.previous=[self.x, self.y]
                    if [self.x, self.y+1] not in self.frontier:
                        self.frontier.append([self.x, self.y+1])
                    
            if self.lst[self.x+1][self.y]==0 and f"{self.x+1};{self.y}" not in self.covered:
                self.movement=1
                if [self.x+1, self.y] !=self.previous:
                    tup.append([self.x, self.y])
                    self.previous=[self.x, self.y]
                    if [self.x+1, self.y] not in self.frontier:
                        self.frontier.append([self.x+1, self.y])
                    

            if self.lst[self.x][self.y-1]==0 and f"{self.x};{self.y-1}" not in self.covered:
                self.movement=4
                if [self.x, self.y-1] != self.previous:
                    tup.append([self.x, self.y])
                    self.previous=[self.x, self.y]
                    if [self.x, self.y-1] not in self.frontier:
                        self.frontier.append([self.x, self.y-1])
                    

            if len(tup) > 1:
                self.junction.append(self.previous)
            
            if self.lst[self.x-1][self.y]==4 and f"{self.x-1};{self.y}" not in self.covered:
                self.movement=2
                self.stop=False
                self.frontier.append([self.x-1, self.y])
            if self.lst[self.x][self.y+1]==4 and f"{self.x};{self.y+1}" not in self.covered:
                self.movement=3
                self.stop=False
                self.frontier.append([self.x, self.y+1])
            if self.lst[self.x+1][self.y]==4 and f"{self.x+1};{self.y}" not in self.covered:
                self.movement=1
                self.stop=False
                self.frontier.append([self.x+1, self.y])
            if self.lst[self.x][self.y-1]==4 and f"{self.x};{self.y-1}" not in self.covered:
                self.movement=4
                self.stop=False
                self.frontier.append([self.x, self.y-1])
        ############################
            self.player.grid_configure(row=self.frontier[0][0],column=self.frontier[0][1])
            Map.map_dict[self.covered[-1]].configure(fg_color="green")
            self.covered.append(f"{self.frontier[0][0]};{self.frontier[0][1]}")
            self.x, self.y=self.frontier[0][0], self.frontier[0][1]
            self.frontier.remove(self.frontier[0])
            
        else:btn.configure(text="Complete")      

    def Greedy_first_search(self):
        def heuristic_fun(xcor, ycor, goal_cor:list):
            x=max(xcor, goal_cor[0])-min(xcor, goal_cor[0])
            y=max(ycor, goal_cor[1])-min(ycor, goal_cor[1])
            nxt=y+x
            return nxt
        
        if self.stop:
            tup=[]
            mv=[]
            if self.lst[self.x-1][self.y]==0 and f"{self.x-1};{self.y}" not in self.covered:
                self.movement=2
                if [self.x-1,self.y] != self.previous:
                    tup.append([self.x-1, self.y])
                    mv.append(self.movement)
                    self.previous=[self.x, self.y]
                    
            if self.lst[self.x][self.y+1]==0 and f"{self.x};{self.y+1}" not in self.covered:
                self.movement=3
                if [self.x, self.y+1] != self.previous:
                    tup.append([self.x, self.y+1])
                    self.previous=[self.x, self.y]
                    mv.append(self.movement)
                    
            if self.lst[self.x+1][self.y]==0 and f"{self.x+1};{self.y}" not in self.covered:
                self.movement=1
                if [self.x+1, self.y] !=self.previous:
                    tup.append([self.x+1, self.y])
                    self.previous=[self.x, self.y]
                    mv.append(self.movement)
                    
            if self.lst[self.x][self.y-1]==0 and f"{self.x};{self.y-1}" not in self.covered:
                self.movement=4
                if [self.x, self.y-1] != self.previous:
                    tup.append([self.x, self.y-1])
                    self.previous=[self.x, self.y] 
                    mv.append(self.movement)               

            if len(tup) > 1:
                self.junction.append(self.previous)
                x=[]
                for i  in tup:
                    x.append(heuristic_fun(i[0], i[1], self.goal))
                self.movement=mv[x.index(min(x))]
            
            if self.lst[self.x-1][self.y]==4 and f"{self.x-1};{self.y}" not in self.covered:
                self.movement=2
                self.stop=False
                self.frontier.append([self.x-1, self.y])
            if self.lst[self.x][self.y+1]==4 and f"{self.x};{self.y+1}" not in self.covered:
                self.movement=3
                self.stop=False
                self.frontier.append([self.x, self.y+1])
            if self.lst[self.x+1][self.y]==4 and f"{self.x+1};{self.y}" not in self.covered:
                self.movement=1
                self.stop=False
                self.frontier.append([self.x+1, self.y])
            if self.lst[self.x][self.y-1]==4 and f"{self.x};{self.y-1}" not in self.covered:
                self.movement=4
                self.stop=False
                self.frontier.append([self.x, self.y-1])
            ########
            if self.movement == 1:
                self.x+=1
                self.covered.append(f"{self.x};{self.y}")  
                self.player.grid_configure(row=self.x,column=self.y)        
            elif self.movement==2:
                self.x-=1
                self.covered.append(f"{self.x};{self.y}")
                self.player.grid_configure(row=self.x,column=self.y)
            elif self.movement==3:
                self.y+=1
                self.covered.append(f"{self.x};{self.y}")
                self.player.grid_configure(row=self.x,column=self.y)
            elif self.movement==4:
                self.y-=1
                self.covered.append(f"{self.x};{self.y}")
                self.player.grid_configure(row=self.x,column=self.y)
            elif self.movement ==0:
                self.x=self.junction[-1][0]
                self.y=self.junction[-1][1]
                self.player.grid_configure(row=self.x,column=self.y)
                self.junction.remove(self.junction[-1])
            Map.map_dict[self.covered[-1]].configure(fg_color="green")
            self.movement=0
            pass
        else:btn.configure(text="Complete")
        pass
    
    def Astar_search(self):
        def heuristic_fun(xcor, ycor, goal_cor:list):
            x=max(xcor, goal_cor[0])-min(xcor, goal_cor[0])
            y=max(ycor, goal_cor[1])-min(ycor, goal_cor[1])
            nxt=y+x
            return nxt
        
        def ground_fun(xcor, ycor, goal_cor:list, step):
            h=heuristic_fun(xcor, ycor, goal_cor)
            search=h+step
            return search
        
        if self.stop:
            tup=[]
            if self.lst[self.x-1][self.y]==0 and f"{self.x-1};{self.y}" not in self.covered:
                self.movement=1
                tup.append([self.x-1, self.y, self.movement])
                    
            if self.lst[self.x][self.y+1]==0 and f"{self.x};{self.y+1}" not in self.covered:
                self.movement=2
                tup.append([self.x, self.y+1, self.movement])
                pass
                    
            if self.lst[self.x+1][self.y]==0 and f"{self.x+1};{self.y}" not in self.covered:
                self.movement=3
                tup.append([self.x+1, self.y, self.movement])
                pass
                    
            if self.lst[self.x][self.y-1]==0 and f"{self.x};{self.y-1}" not in self.covered:
                self.movement=4
                tup.append([self.x, self.y-1, self.movement])
                pass

            if len(tup) > 1:
                self.junction.append([self.x, self.y, self.step])
                hrst=ground_fun(tup[0][0], tup[0][1], self.goal, self.step+1)
                hrst1=ground_fun(tup[1][0], tup[1][1], self.goal, self.step+1)
                if hrst > hrst1:
                    self.movement=tup[1][2]
                    self.Astr.append([tup[0][0], tup[0][1], hrst])
                    self.Astrstart=True
                else:
                    self.movement=tup[0][2]
                    self.Astr.append([tup[1][0], tup[1][1], hrst1])
                    self.Astrstart=True

            if self.lst[self.x][self.y-1]==4:
                self.movement=4
                self.stop=False
                tup.append([self.x, self.y-1])
            elif self.lst[self.x+1][self.y]==4:
                self.movement=3
                self.stop=False
                tup.append([self.x+1, self.y])
            elif self.lst[self.x][self.y+1]==4:
                self.movement=2
                self.stop=False
                tup.append([self.x, self.y+1])
            elif self.lst[self.x-1][self.y]==4:
                self.movement=1
                self.stop=False
                tup.append([self.x-1, self.y])
            else:pass
            hrst=ground_fun(self.x, self.y, self.goal, self.step)
            hrst1=0
            if len(tup)>0:
                hrst1=ground_fun(tup[-1][0], tup[-1][1], self.goal, self.step+1)
                self.tupe=True

            if self.Astrstart:
                if self.tupe:
                    if hrst1 !=0:
                        if hrst1 > hrst:
                            if len(self.Astr) > 0:
                                if hrst1 > self.Astr[-1][2] and f"{self.Astr[-1][0]};{self.Astr[-1][1]}" not in self.covered:
                                    self.Astr.append([tup[-1][0], tup[-1][1], hrst1])
                                    self.x=self.Astr[-2][0]
                                    self.y=self.Astr[-2][1]
                                    self.player.grid_configure(row=self.x, column=self.y)
                                    self.covered.append(f"{self.x};{self.y}")  
                                    self.Astr.remove(self.Astr[-2])
                                    self.movement=5

            if self.movement == 1:
                self.x=self.x-1
                self.y=self.y
                self.player.grid_configure(row=self.x, column=self.y)
                self.covered.append(f"{self.x};{self.y}") 
                self.step+=1
            elif self.movement == 2:
                self.x=self.x
                self.y=self.y+1
                self.player.grid_configure(row=self.x, column=self.y)
                self.covered.append(f"{self.x};{self.y}") 
                self.step+=1
            elif self.movement == 3:
                self.x=self.x+1
                self.y=self.y
                self.player.grid_configure(row=self.x, column=self.y)
                self.covered.append(f"{self.x};{self.y}") 
                self.step+=1
            elif self.movement == 4:
                self.x=self.x
                self.y=self.y-1
                self.player.grid_configure(row=self.x, column=self.y)
                self.covered.append(f"{self.x};{self.y}")
                self.step+=1 
            elif self.movement == 0:
                if len(self.junction) ==0:
                    self.junction.append([self.Astr[-1][0], self.Astr[-1][1], self.Astr[-1][2]])
                    self.covered.append(f"{self.junction[-1][0]};{self.junction[-1][1]}")
                self.x=self.junction[-1][0]
                self.y=self.junction[-1][1]
                self.step=self.junction[-1][2]
                self.player.grid_configure(row=self.x, column=self.y)
                if self.Astr[-1][0] == self.junction[-1][0] and self.Astr[-1][1] == self.junction[-1][1]:
                    self.Astr.remove(self.Astr[-1])
                self.junction.remove(self.junction[-1])
            else:pass

            self.movement=0
            Map.map_dict[self.covered[-1]].configure(fg_color="green")
        else:btn.configure(text="Complete")

customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("dark")  
window=customtkinter.CTk()
lst=[
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 3, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1], 
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 4, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    
]
lst2=[
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 3, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 4, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    
]
lst3 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 3, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 4, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],   
]
lst4=[
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 3, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

initialmap=Map()
initialmap.Graphical(lst4)
player=Player(initialmap) 
def call():
    player.Astar_search()
    window.after(300, call)
btn=customtkinter.CTkButton(window, text="test", command=call)
btn.grid(row=20, column=1, columnspan=10)

window.mainloop()
