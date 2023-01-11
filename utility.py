#########################################################################################
#																						#
# 								PROGRAMMING IN DATA SCIENCE		                        #
#								ASSIGNMENT- 1a			     						    #
#								STUDENT ID: U3227622		     					    #
#								STUDENT NAME: Ambika Huluse Kapanaiah				    #
#								DATE OF SUBMISSION:                                     #
#								POST GRADUATE                                           #
#																						#
##########################################################################################


###function to calculate distance between 2 samples.
#Based on eucledean distance formula distance is calculated
def calculate_distance(p1, p2):
 distance = 0
 for i in range(len(p1)):    #takes care of dimension of the sample(2d or 4d)
     distance += (p2[i] - p1[i]) * (p2[i] - p1[i])  #Eucledean distance formula
 return distance**0.5     # taking square root of all the summed distance  



###############################################################################


###module definition for finding nearest distance.
#Function will take one unknown smaples at a time when called.
#outputs shortest_distance_final of respective unknown sample with data_sample
#outputs nearest_sample_final as respective red/blue sample which is shortest to unknown_sample

def find_nearest_neighbour(unknown_sample, data_sample):
    shortest_distance = 100000000
    nearest_sample_final = []
    shortest_distance_final = []
    for sample in data_sample:                     # iterating for each samples from red/blue
        dist = calculate_distance(unknown_sample, sample) #calling distance calculation method to find shortest distance 
        if shortest_distance > dist:                     #finding shortest among calculated distances with each data_sample
            shortest_distance = dist
            nearest_sample = sample
    shortest_distance_final.append(shortest_distance)   #saving sortest distance finalized for each unkown sample
    nearest_sample_final.append(nearest_sample)     #saving corresponding sample for the sortest distance finalized for each unkown sample
    return shortest_distance_final,nearest_sample_final 


###########################################---------END of utility-----------###################################