#########################################################################################
#																						#
# 								PROGRAMMING IN DATA SCIENCE		                        #
#								ASSIGNMENT- 1b			     						    #
#								STUDENT ID: U3227622		     					    #
#								STUDENT NAME: Ambika Huluse Kapanaiah				    #
#								DATE OF SUBMISSION: 19/09/2021                          #
#								POST GRADUATE                                           #
#																						#
##########################################################################################

####clustering.py for assignment 1b imported in the main module as cluster


###function to calculate distance between 2 data samples.
#Based on eucledean distance formula distance is calculated
def calculate_distance(point1, point2):
 euc_distance = 0
 for i in range(len(point1)):    #takes care of dimension of the sample(2d or 4d)
     euc_distance += (point2[i] - point1[i]) * (point2[i] - point1[i])  #Eucledean distance formula
 return euc_distance**0.5   # taking square root of all the summed distance 

###############################################################################
 
###Function to generate K cluster centres at random
##Only used once initially to get random centroids to begin with clustering.
#Output cluster_centre_list will have centroids calculated randomly
def generate_K_cluster_centres(num_of_dimension, num_of_clusters):
    cluster_centre_list = []
    for cluster in range(num_of_clusters): #Takes care of cluser size(2 clusters or 4)
        cluster_centre = []
        for dimension in range(num_of_dimension): #Based on dimension(2D or 4D)
            cluster_centre.append(cluster + dimension) #adding both cluster range and dimension range
        cluster_centre_list.append(cluster_centre) #cluster centers saved for each dimension
    return cluster_centre_list

###############################################################################

###Function to find the shortest distance between samples
##Calling calculate_distance for each sample and centroids using for loop
##Outputs the best centroid data based on shortest distance calculated
def find_short_dist(cluster_center_new, sample): #sample is data sample sent one at a time from calling function
    best_centroid = []
    shortest_distance = 10000000000
    for centre in cluster_center_new:         #iterates 2 times for 2 clusters else 4 times
        distance = calculate_distance(sample,centre)
        if shortest_distance > distance:   #if shortest distance found with the current iteration and centroid
            shortest_distance = distance
            best_centroid = centre       #storing that as best centroid for the sample
    return best_centroid                 #Appending all best centroids happens in othe function after returning.

###############################################################################

####Function to create clusterlists based on clustesize and shortests distance between data points and centroids.
##Outputs 2 clusterlists if clustersize selected is 2 or else 4 clusterlists are returned.
def create_lists(cluster_size, cluster_center_new, data_sample):
    #creating empty clusterlists to append samples based on best centroid
    clusterlist1 = []
    clusterlist2 = []
    clusterlist3 = []
    clusterlist4 = []       
    for sample in data_sample:      #Iterating for all data saples from input file
        best_centroid = find_short_dist(cluster_center_new, sample) #best_centroid received find_short_dist function
        if cluster_size == 2:
            if best_centroid == cluster_center_new[0]: #based on clustersize and best centroids 
              clusterlist1.append(sample)              #samples are stored in respective clusterlists
            else: 
              clusterlist2.append(sample)
        if cluster_size == 4:
            if best_centroid == cluster_center_new[0]:  ##cluster_center_new has the centroids for all clusters
              clusterlist1.append(sample)
            elif best_centroid == cluster_center_new[1]: ##if best centroid we found belongs to 1st (0,1,2,3) center inside list
              clusterlist2.append(sample)                 ##storing the corresponding datasample into the clusterlist2
            elif best_centroid == cluster_center_new[2]:
              clusterlist3.append(sample)
            else: 
                clusterlist4.append(sample)
    if cluster_size == 2:
        return clusterlist1, clusterlist2    #returning 2 clusterlists if clustersize is 2
    elif cluster_size == 4:
        return clusterlist1, clusterlist2,clusterlist3, clusterlist4  #returning 4 clusterlists if clustersize is 4


###############################################################################

###Function to calculate average to find new centroids for cluster lists of data sample.
##based on selected dimension(2 or 4) the average of all samples in the clusterlist is computed.
##new centroids are returned one at a time for each clusterlist

def calculate_average(clusterlist, cluster_size, select_dimension):
    new_centre = []
    for index in range(select_dimension): #based on dimension columnwise averages calculated
        sum = 0
        for sample in clusterlist:
            sum += sample[index]
        if len(clusterlist)==0:  #empty clusterlists are handled  
            new_centre.append(0)
        else:
            new_centre.append(sum / len(clusterlist))
    return new_centre   #returning one center at a time




######################################------END of clustering.py-----#######################################################
