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


### Importing read/write file and utilty methods ##
import io_module_a as io
import utility as uti

##############################################################################



#Each flenames for red blue and unknown saples for 2, 4 and 8 Dimension are stored in list
red_data =  ["datasets/red_2d.txt","datasets/red_4d.txt","datasets/red_8d.txt"]
blue_data =  ["datasets/blue_2d.txt","datasets/blue_4d.txt","datasets/blue_8d.txt"]
unknown_data =  ["datasets/unknown_2d.txt","datasets/unknown_4d.txt","datasets/unknown_8d.txt"]

#Initialising red blue and unknown dataset
red_dataset = None
blue_dataset = None
unknown_dataset = None


###Reading 3 files for red, green, and unknown data samples for 2,4 and 8 dimension

while True:
	try:
		select_dimension = int(input("Select the Dimension for the Red and blue dataset (2,4,8):"))
		if select_dimension == 2:
			red_dataset = io.read_multi_dim_data(red_data[0])
			blue_dataset = io.read_multi_dim_data(blue_data[0])
			unknown_dataset = io.read_multi_dim_data(unknown_data[0])
			break


		elif select_dimension == 4:
			red_dataset = io.read_multi_dim_data(red_data[1])
			blue_dataset = io.read_multi_dim_data(blue_data[1])
			unknown_dataset = io.read_multi_dim_data(unknown_data[1])
			break

		elif select_dimension == 8:
			red_dataset = io.read_multi_dim_data(red_data[2])
			blue_dataset = io.read_multi_dim_data(blue_data[2])
			unknown_dataset = io.read_multi_dim_data(unknown_data[2])
			break

		else:
			raise ValueError

	except ValueError:
		print("Please enter a valid number")

#all data samples in tuple
data_sample = (red_dataset,blue_dataset,unknown_dataset)


###############################################################################


#calculate distances of all unknown samples from red sample and blue sample
#Finding nearest among red and blue 
#storing the final values for shortence distance and nearest sample 
shortest_distance_final = []
nearest_sample_final = []
unknown_sample_final = []
for unknown_sample in unknown_dataset:    #looping for all unknown samples(20 unknown samples)
    shortest_distance_red,nearest_sample_red = uti.find_nearest_neighbour(unknown_sample, red_dataset)
    shortest_distance_blue,nearest_sample_blue = uti.find_nearest_neighbour(unknown_sample, blue_dataset)
    if shortest_distance_red > shortest_distance_blue: #finding shortest among red and blue class
        shortest_distance_final.append(shortest_distance_blue)  
        nearest_sample_final.append(nearest_sample_blue)
        unknown_sample_final.append((unknown_sample,"blue")) #labelling class of unknown sample, for red/blue
    else:
        shortest_distance_final.append(shortest_distance_red)
        nearest_sample_final.append(nearest_sample_blue)
        unknown_sample_final.append((unknown_sample,"red")) #labelling class of unknown sample, for red/blue
      
        
#output all unknown samples and their class label to console
for samples in unknown_sample_final:
     print("The unknown sample "+str(samples[0])+" falls in "+str(samples[1])+ " class")



#output all unknown samples and their class label to file
#generated file stored in current working folder

io.write_multi_dim_data(select_dimension, unknown_sample_final)

#######################################-----------END OF MAIN------------##########################################
