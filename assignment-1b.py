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

###Importing io_module_b.py(having input output interactions)
#Importing clustering.py to use modules defined inside
import io_module_b as io
import clustering as cluster

###Hardcoding the path for 4 datasets given
data_2c_2d = "datasets/data_2c_2d.txt"
data_4c_2d = "datasets/data_4c_2d.txt"
data_2c_4d = "datasets/data_2c_4d.txt"
data_4c_4d = "datasets/data_4c_4d.txt"


###Reading the data files based on dimension input from the user
#if user enter 2 as input both data_2c_2d and data_4c_2d are read
#if user enter 4 as input both data_2c_4d and data_4c_4d are read
while True:
	try:
		select_dimension = int(input("Select the Dimension for the dataset (2,4):"))
		if select_dimension == 2:
			data_2c_2d = io.read_multi_dim_data(data_2c_2d)
			data_4c_2d = io.read_multi_dim_data(data_4c_2d)
			break
		elif select_dimension == 4:
			data_2c_4d = io.read_multi_dim_data(data_2c_4d)
			data_4c_4d = io.read_multi_dim_data(data_4c_4d)
			break
		else:
			raise ValueError

	except ValueError:
		print("Please enter a valid number") #2 and 4 could be entered as input

###Taking input for cluster size from the user 
##The final input data is decided here based on cluster size and selected dimention 
#2 dimension: among data_2c_2d and data_4c_2d, data_2c_2d is selected if cluster size is 2 or else data_4c_2d
#4 dimension: among data_2c_4d and data_4c_4d, data_2c_4d is selected if cluster size is 2 or else data_4c_4d
cluster_size = int(input("Input the cluster size:2,4 : "))
try:
    if cluster_size == 2:
        if select_dimension == 2:
            data_sample =  data_2c_2d
        else:
            data_sample =  data_2c_4d
    elif cluster_size == 4:
        if select_dimension == 2:
            data_sample =  data_4c_2d
        else:
            data_sample =  data_4c_4d
    else:
     	raise ValueError
        
except ValueError:
		print("Please enter a valid clustersize") #2 and 4 could be entered as input

print("!!!!!Now going to create cluster for "+str(select_dimension)+"Dimension Data with "+str(cluster_size)+"clusters.")

print("#############################################################################")

###Create a random cluster center based on number of dimension and size of cluster
#These are initial centroids to begin with
#based on selected dimension either 2 or 4 random centroids are generated.
#centroids are stored in cluster_center_random variable
cluster_center_random = []
cluster_center_random = cluster.generate_K_cluster_centres(select_dimension, cluster_size)

###creating empty lists to group the data samples
clusterlist1 = []
clusterlist2 = []
clusterlist3 = []
clusterlist4 = []

###Based on cluster size creating clusterlists of data sample by calling create_lists functions
#if it is 2 cluster 2 clusterlists are created else 4 clusterlists are created
#1st iteration sending random clusters generated above to group data samples into clusterlists
if cluster_size == 2:
    clusterlist1, clusterlist2 = cluster.create_lists(cluster_size, cluster_center_random, data_sample)
    clusterlist_All = [clusterlist1, clusterlist2]
elif cluster_size == 4: 
    clusterlist1, clusterlist2,clusterlist3, clusterlist4 = cluster.create_lists(cluster_size, cluster_center_random, data_sample)
    clusterlist_All = [clusterlist1, clusterlist2,clusterlist3, clusterlist4]

###Calculating average of each clusterlists to find new centroids.
##calculate_average function returns new centroids  for all cluster lists formed above.
#We will get all centroids (all_center) based on calculating average of samples in each clusterlist
# 2 centroids if clustersize is 2 otherwise 4 centroids
all_center = []
for clusters in clusterlist_All:
    new_center =  cluster.calculate_average(clusters, cluster_size,select_dimension)
    all_center.append(new_center)

#Calling calculate_distance function to get the sum of distance of old and new centroids
#inputs are old centroids which are generated randomly and new centroids calculated using average function
sum_of_distance = 0
for index in range(len(clusterlist_All)):   
      distance = cluster.calculate_distance(cluster_center_random[index], all_center[index])
      sum_of_distance += distance 
 
###############################################################################

#Setting threshold to 0.1 so the sum of distance between old and new centroids shouldnot be greater than 0.1
#This threshold will decide whether we need to stop recalculating centroids and recalculating clusters.
threshold = 0.1

#recalculated_iterations is the number of iterations done to get the proper centroids and proper clusterlists
recalculated_iterations = 0

###The following while loop iterates and recalculates both centroids and clustelists
#until and unless we find proper centroids and proper clusterlists
#Contains Function calls for create list, calculating average and finding sum of distances
while sum_of_distance > threshold:
    recalculated_iterations += 1
    #calculate distance between old and new center     
    old_center = all_center
       
    if cluster_size == 2:
        clusterlist1, clusterlist2 = cluster.create_lists(cluster_size, all_center, data_sample)
        clusterlist_All = [clusterlist1, clusterlist2]
    elif cluster_size == 4: 
        clusterlist1, clusterlist2,clusterlist3, clusterlist4 = cluster.create_lists(cluster_size, all_center, data_sample)
        clusterlist_All = [clusterlist1, clusterlist2,clusterlist3, clusterlist4]
    all_center = []
    for clusters in clusterlist_All:
        centeroids =  cluster.calculate_average(clusters, cluster_size,select_dimension)
        all_center.append(centeroids)
    sum_of_distance = 0
    for index in range(len(clusterlist_All)):   
        distance = cluster.calculate_distance(old_center[index], all_center[index])
        sum_of_distance += distance 
        #print(sum_of_distance)
    
###############################################################################

###Once the proper centroids and clusterlists are formed we are coming out if while loop
##Storing the final clusterlists and centroids as follows.
#cluster_final_list will have 2 clusterlists if clustersize selected above is 2 otherwise 4 clusterlists.
#Final_centeroids will have 2 centroids if clustersize selected above is 2 otherwise 4 centroids.
cluster_final_list = clusterlist_All
Final_centeroids = old_center


###############################################################################

###Finally calling tKinter drawing which is in io_module_b.py
#The function draws clusters with centroids on to the canvas.
#Draws 4 clusters with 4 centroids if clustersize selected above is 4 else draws 2 clusters with 2 centroids.
io.drawing(data_sample, Final_centeroids, cluster_final_list,select_dimension,cluster_size)


####################################------END OF THE CODE---#####################################################