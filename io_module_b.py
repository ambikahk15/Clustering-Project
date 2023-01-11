#########################################################################################
#																						#
# 								PROGRAMMING IN DATA SCIENCE		                        #
#								ASSIGNMENT-1 a			     						    #
#								STUDENT ID: U3227622		     					    #
#								STUDENT NAME: Ambika Huluse Kapanaiah				    #
#								DATE OF SUBMISSION:                                     #
#								POST GRADUATE                                           #
#																						#
##########################################################################################

###This is io_module_b.py imported as io in assignment-1b.py

##iporting tkinter package for CANVAS drawing
import tkinter



###############################################################################

#Module definition for reading the txt files: 2d, 4d data samples
#takes user input as 2d, 4d or 8d
def read_multi_dim_data(file_name):
    datasets = [] #empty dataset created to append data
    f = None
    try:
        f = open(file_name, 'r') #open file in reading mode
        while True:
            line = f.readline()
            if len(line) == 0: #if we reach end of file break the loop
                 break
            line = line.replace('\n', '') #remove end of line \n character
            dataset = line.split(' ') 
            dataset = [float(x) for x in dataset]
            datasets.append(dataset)  #storing line by line to datasets list
    except Exception as ex:
        print(ex.args)
    finally:
        if f:
            f.close()   #closing the file
    return tuple(datasets) #returning tuple of datasets
   
###############################################################################


#Function to display data on canvas for all data samples with best final centroids.
#Function takes final centroids and final clusterlists and original data sample as input
#based on cluster size the cluster lines are drawn
# circles are drawn using original data sample read from text files.
def drawing(data_sample, Final_centeroids, cluster_final_list,select_dimension,cluster_size):
    #Create canvas
    top = tkinter.Tk()
    canvas = tkinter.Canvas(top, bg="white", height=1000, width=1300) #defining canvas size
    #Display data
    s = 80 #scale factor for samples
    r = 4 #radius for circles creation
    tx = 400 #x translation 
    ty = 200 #y translation
    
    
    xi = 0
    yi = 1
    fill_colour = ["green","red","cyan","grey"] #colou list for different cluster lines
    if select_dimension == 4: #x and y selection done for 4dimension data sample
        xi = 2
        yi = 3
        
    
    for sample in data_sample: ##Iterating to create circle points on canvas for all data samples
        x = sample[xi]
        y = sample[yi]
        x = x*s + tx #some values are negative so +400 is to make them positive
        y = y*s + ty
        canvas.create_oval(x-r, y-r, x+r, y+r, outline = "blue", fill="blue") #circle outline, filled with blue
        
        
    for k in range(len(Final_centeroids)):  ##drawing lines from each centroind to respective cluster group
         (x1, y1) = (Final_centeroids[k][xi], Final_centeroids[k][yi])
         x1 = x1*s + tx
         y1 = y1*s + ty
         for i in range(len(cluster_final_list[k])): #iterates for all the cluster groups one group at a time
            (x2, y2) = (cluster_final_list[k][i][xi], cluster_final_list[k][i][yi])
            x2 = x2*s + tx
            y2 = y2*s + ty
            canvas.create_line(x1, y1, x2, y2, fill = fill_colour[k]) #drawing line and filling with respective colours define above

    canvas.pack()
    top.mainloop()
        

##########################################------END OF io_module------##########################################