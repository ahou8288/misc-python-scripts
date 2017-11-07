# Select mode!
# 1 = cifar10,
# 2 = cifar100,
# 3=both
mode=3

print("Importing nessecary libraries")
import numpy as np
from scipy.spatial import distance
import os
import pickle
print("Finished importing")

### CONSTANTS
number_svd_vectors=10 #Specifies the amount of data stored after dimensional reduction
progress_display_rate=1000 # Just used to show progress

# Size of the data sets
cifar10_training_set_size=10000
cifar10_test_set_size=10000
cifar10_num_labels=10

cifar100_training_set_size=10000
cifar100_test_set_size=10000
cifar100_num_coarse=20
cifar100_num_fine=100

# confusion_matrix=[[0 for i in range(10)] for i in range(10)]

### Get the data
def unpickle(file):
	import pickle as cPickle
	fo = open(file, 'rb')
	dict = cPickle.load(fo,encoding='latin1')
	fo.close()
	return dict

if (mode!=2):
	# cifar10
	# Join all 5 training batches together into one extra large batch
	cifar10_training_set=unpickle("data_batch_1")
	cifar10_test_set=unpickle("test_batch")
if (mode!=1):
	#cifar100
	cifar100_training_set=unpickle('train')
	cifar100_test_set=unpickle('test')

def single_image_svd(data):
	#Dimensional reduction using singular value decomposition
	U, sigma, V = np.linalg.svd(data) #SVD

	#some data is not returned, this is to reduce the size of the data and make the program run faster
	return [U[:, :number_svd_vectors],sigma[:number_svd_vectors],V[:number_svd_vectors, :]] #store all 3 vectors to a depth of number_svd_vectors

def print_progress(i,data_size):
	if i%progress_display_rate==0 and i>0:
		print('%d%% complete.' % (i*100/data_size))

def two_dimension(data): #splits 1d array up and puts it in a 2D array
	return [data[32*i:32+32*i] for i in range(32)]

def similarity(svd1,svd2):
	scores=[0,0,0]
	array_depths=[32,number_svd_vectors,number_svd_vectors]

	importance_factors=[475,1,310] #these are weighting numbers (chosen by trial and error) which resulted in the highest accuracy.
	#this accounts for not all of the things SVD returns being of equal scale/importance.
	
	for i in range(3):
		for j in range(array_depths[i]):
			scores[i]+=distance.cityblock(svd1[0][j],svd2[0][j]) #(manhattan distance)
	return np.array(scores).dot(np.array(importance_factors))

### Get svd data for the training batches
def batch_image_svd(batch_size,batch_data):
	output_data=[]
	for i in range(batch_size):
		print_progress(i+1,batch_size)
		output_data.append(single_image_svd(two_dimension(batch_data['data'][i])))
	return output_data

print("Getting svd data for training batches:")
if (mode!=2):
	print("CIFAR-10;")
	cifar10_training_svd=batch_image_svd(cifar10_training_set_size,cifar10_training_set)
if (mode!=1):
	print("CIFAR-100;")
	#cifar100
	cifar100_training_svd=batch_image_svd(cifar100_training_set_size,cifar100_training_set)
	print("Training batch SVD complete")

### Finding the average for each class
#for a give class it has each image has some vectors.
#if we take the average vector of all the images in a class we assume that it represents the class.

###Find the average for each class
def group_batch_by_class(class_size,batch_size,batch_labels,batch_svd):
	class_svd_data=[[] for k in range(class_size)] #create a place to put each item
	for i in range(batch_size): #go through every item in the batch
		class_svd_data[batch_labels[i]].append(batch_svd[i]) #group the current item under it's label
	return class_svd_data

print("Grouping svd data.")
if (mode!=2):
	cifar10_class_svd=group_batch_by_class(cifar10_num_labels,cifar10_training_set_size,cifar10_training_set['labels'],cifar10_training_svd)
if (mode!=1):
	cifar100_coarse_svd=group_batch_by_class(cifar100_num_coarse,cifar100_training_set_size,cifar100_training_set['coarse_labels'],cifar100_training_svd)
	cifar100_fine_svd=group_batch_by_class(cifar100_num_fine,cifar100_training_set_size,cifar100_training_set['fine_labels'],cifar100_training_svd)

print("Getting class vector representations from training data")
def find_class_average(class_svd_data):
	i=0
	class_svd_average=[]
	for temp_class in class_svd_data: #find the average of similarly labelled items (should try median instead)
		#setting initial values of variables
		t_v=temp_class[0][0]
		t_sigma=temp_class[0][1]
		t_u=temp_class[0][2]
		#including all the other items in the sum
		for svd_item in temp_class[1:]:
			i+=1
			print_progress(i,10000)
			t_v+=svd_item[0]
			t_sigma+=svd_item[1]
			t_u+=svd_item[2]
		#normalising
		t_v=t_v/len(temp_class)
		t_sigma=t_sigma/len(temp_class)
		t_u=t_u/len(temp_class)
		class_svd_average.append([t_v,t_sigma,t_u])
	return class_svd_average

if (mode!=2):
	cifar10_class_average=find_class_average(cifar10_class_svd)
if (mode!=1):
	cifar100_coarse_average=find_class_average(cifar100_coarse_svd)
	cifar100_fine_average=find_class_average(cifar100_fine_svd)

print("Getting svd data for test batches:")
if (mode!=2):
	print("CIFAR-10;")
	cifar10_test_svd=batch_image_svd(cifar10_test_set_size,cifar10_test_set)
if (mode!=1):
	print("CIFAR-100;")
	#cifar100
	cifar100_test_svd=batch_image_svd(cifar100_test_set_size,cifar100_test_set)
	print("Training batch SVD complete")

print("Classifying images") #Fianlly!
def classify_batch(test_size,test_data,class_svd_average,label_data):
	num_correct=0
	for j in range(test_size): #loop through all images to test
		print_progress(j+1,test_size)

		### create an empty arrap of similarites
		image_similarities=[]
		for i in class_svd_average:# compare each image the the vector which represents each class
			image_similarities.append(similarity(i,test_data[j]))

		if (np.argmin(image_similarities)==label_data[j]): # see if the image was classified correctly
			# Successful classification
			num_correct+=1
		# confusion_matrix[np.argmin(image_similarities)][label_data[j]]+=1
	return num_correct

if (mode!=2):
	print("Cifar10 classification:")
	cifar10_correct=classify_batch(cifar10_test_set_size,cifar10_test_svd,cifar10_class_average,cifar10_test_set['labels'])
	print("Cifar10 classifier accuracy:\t\t",cifar10_correct/cifar10_test_set_size*100)
if (mode!=1):
	print("Cifar100 coarse classification:")
	cifar100_coarse_correct=classify_batch(cifar100_test_set_size,cifar100_test_svd,cifar100_coarse_average,cifar100_test_set['coarse_labels'])
	print("Cifar100 coarse classifier accuracy:",cifar100_coarse_correct/cifar100_test_set_size*100)

	print("Cifar100 fine classification:")
	cifar100_fine_correct=classify_batch(cifar100_test_set_size,cifar100_test_svd,cifar100_fine_average,cifar100_test_set['fine_labels'])
	print("Cifar100 fine classifier accuracy:\t",cifar100_fine_correct/cifar100_test_set_size*100)

# [print(i) for i in confusion_matrix]