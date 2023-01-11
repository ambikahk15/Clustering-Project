#########################################################################################
#																						#
# 								PROGRAMMING IN DATA SCIENCE		                        #
#								ASSIGNMENT- 1a			     						    #
#								STUDENT ID: U3227622		     					    #
#								STUDENT NAME: Ambika Huluse Kapanaiah				    #
#								DATE OF SUBMISSION: 19/09/2021                          #
#								POST GRADUATE                                           #
#																						#
##########################################################################################


#io_module_a.py which is imported as io in assignment-1a.py


#Module definition for reading the txt files: 2d, 4d and 8d/ red, blue and unknown sample
#based on user input 2,4,8 red,lue and unknown 2d,4d and 8d files are read conditionally
def read_multi_dim_data(file_name):
    datasets = [] #empty dataset created to append data
    f = None
    try:
        f = open(file_name, 'r') #open file in read mode
        while True:
            line = f.readline()
            if len(line) == 0: #end of file
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
    return datasets
   


###############################################################################

#Module definition for writing the output unknownsamples and the belonging class(red/blue) to a file
#function creates a filename based on dimension selected (output_2d.txt,output_4d.txt or output_8d.txt)
#it iterates through each unknown sample with class label attached to it and writes into output file.
def write_multi_dim_data(dimension,unknown_sample_final):

    filename = "output_"+str(dimension)+"d.txt"   #creating output file name
    try:
        f = open(filename, "w")         #creating and opening file for writing
        for sample in unknown_sample_final: #reading all the samples one by one from unknown_sample_final
            f.write(str(sample))
            f.write("\n")                  # writing of next sample happens to next line 
    except Exception as ex:
        print(ex.args)
    finally:
        if f:
            f.close()               #closing and saving the file
    
         

##########################################------END OF io_module------##########################################