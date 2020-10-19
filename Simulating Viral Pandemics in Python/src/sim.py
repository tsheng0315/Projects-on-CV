import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use('dark_background')
from matplotlib.animation import FuncAnimation as animation
from matplotlib import rc


sus_col = 'grey' # susceptable
inf_col = 'red' # infection 
rem_col = 'lime' # recovered
ded_col = 'k' # deceased-black

infection_radius = 0.6
recovery_rate = 0.0006
death_rate = .001
stage_dimension = 100 # MxM square stage

maskBool=False
maskMod=.16

SDbool=False
SDmod= .1

class Sim():
    def __init__(self,init):
        #init = [N,inf,recover,dead]
        
        self.N = init[0]
        suc = self.N-init[1]-init[2]-init[3]
        self.cols = np.repeat([sus_col,inf_col,rem_col,ded_col],
                              [suc,init[1],init[2],init[3]])
                              # colors and repeated times
        self.low, self.high = -stage_dimension/2,stage_dimension/2
        self.pos = np.random.uniform(self.low,self.high,size=(2,self.N))
        # self.pos.shape--> (2,500), (x1, x2, x3...), (y1, y2, y3)
        # Draw samples from a uniform distribution.
        # size(): output size
        
        self.stream = self.data_stream()
        self.fig, self.ax = plt.subplots()

        self.ani = animation(self.fig
                            ,self.update
                            ,interval=80
                            ,init_func=self.setup
                            ,blit=True)
        
    def setup(self):
        p,c= next(self.stream)
        
        self.scat = self.ax.scatter(x=p[0,:],
                                    y=p[1,:],
                                    c=c.T)
        return self.scat,

    
    def arg_within_radius(self,inf,susceptible,r):
        #inf 2x2--> location of 2 points, succeptible nx2 matrices --> location of n points
        dist = np.sqrt(((inf-susceptible)**2).sum(axis=1)) 
        # distance between infection points and susceptible points
        return np.argwhere(dist<r).ravel()
        # Find the indices of array elements satisfy requirement + vectorise(2D to 1D) 
    
    def data_stream(self):
        while True:
            removed = 0
            # move points
            jitter = 0.5 * np.random.normal(0,1,size=(2,self.N))
            self.pos[0:2,:]+=jitter ## ?

            # infect and recover---------
            # get infected people
            inf = np.argwhere(self.cols == inf_col).ravel()
            # index of inf_col in 1D (ndarray)
            '''
            print(self.pos)
            print(" /n Second")
            print(self.pos[:,[0, 1,2, 3]])
            print(np.array([0, 1,2, 3]).shape)
            '''
            # infectious people location
            inf_people = self.pos[:,inf].T
            # turn inf_people into the format of index pairs
            # self.pos.shape--> (2,500)
            # self.pos[:,inf]--> (2,2)
            
            # susceptible people location
            for i in inf_people:
                suc = np.argwhere(self.cols == sus_col).ravel()
                # suc.shape-->498
                suc_people = self.pos[:,suc].T
                
                # new infected people(people within infection radius)
                infect = self.arg_within_radius(i, suc_people,infection_radius)
                infect_index = suc[infect]
                # infected index in total population
                self.cols[infect_index] = inf_col # infectious people mark as 'red'

            # adjust out of bound points
            x1=np.where(self.pos[0:2,:]<self.low)
            x2=np.where(self.pos[0:2,:]>self.high)
            self.pos[0:2,:][x1], self.pos[0:2,:][x2] = self.low, self.high
            
            # recovered people from susceptible people
            # yield [self.pos,self.cols],
            r = np.random.uniform(0,1, size = inf.size)
            # r-->(1,2)
            recover = np.argwhere(r<recovery_rate).T
            # transpose, turn into the shape of (x1,y1)
            recovered_idx = inf[recover]
            self.cols[recovered_idx] = rem_col
            
            # dead people from susceptible people
            d = np.random.uniform(0,1, size = (inf.size))
            dead = np.argwhere(d<death_rate).T
            dead_idx = inf[dead]
            self.cols[dead_idx] = ded_col
          
            '''for dd in dead:
              removed+=1
            '''
            ## confused???
            ded=np.argwhere(self.cols == ded_col).ravel()
            
            ded_people = self.pos[:,dead].T

            for dd in ded_people:
                removed+=1

            # print number of deaths
            # print(removed)
            #print(len(ded))
            yield self.pos,self.cols
            
    def update(self,i):
        data, c= next(self.stream)
        self.scat.set_offsets(data[0:2,:].T)
        self.scat.set_sizes(np.zeros(self.N)+10)
        self.scat.set_color(c.T)
        return self.scat,


init = [500, # pop. size
        2, # infected
        0, #recovered
        0] #dead


S=Sim(init)

rc('animation', html='jshtml')
S.ani
