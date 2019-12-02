from math import log as ln
import numpy as np
from matplotlib import pyplot as plt
import random
dimention=2
percent_training_data=0.75
# maximum_number_of_weight_update=100
learning_rate=0.1

def read_training_dataset(filename):
    file_object=open(filename,'r')
    file_data=file_object.readlines()
    data_vectors=[]#list of list
    for line in file_data:
        data_vectors.append([float(x) for x in line.split()])
    return data_vectors

def main():
     training_data=[[] for i in range(3)]
     testing_data=[]
     # xmin=ymin=100;xmax=ymax=-100
     upper_limit=-100
     lower_limit=100
     for i in range(1,4):#because it is two class perceptron
         filename='Class'+str(i)+'.txt'
         data_vectors=read_training_dataset(filename)
         # print ('mini ===============================',data_vectors)
         # print
         lower_limit=min(lower_limit, np.amin(data_vectors));
         upper_limit=max(upper_limit, np.amax(data_vectors));

         for item in data_vectors[:int(len(data_vectors)*percent_training_data)]:
             # print item
             training_data[i-1].append([item[0],item[1],i-1])
             # training_data_Y[i-1].append(item[1])
         for item in data_vectors[int(len(data_vectors)*percent_training_data):]:
             # print item
             testing_data.append([item[0],item[1],i-1])

     print ('### Drawing graph ###\n')
     # print X,Y
     #naming the x axis
     plt.xlabel('x - axis')
     # naming the y axis
     plt.ylabel('y - axis')
     plt.scatter((np.array(training_data[0]).T)[0],(np.array(training_data[0]).T)[1],s=1 ,color='pink',label='class 1')
     plt.scatter((np.array(training_data[1]).T)[0],(np.array(training_data[1]).T)[1],s=1, color='lightgreen',label='class 2')
     plt.scatter((np.array(training_data[2]).T)[0],(np.array(training_data[2]).T)[1],s=1, color='lightblue',label='class 3')
     testing_data = [x for x in testing_data if x != []]
     random.shuffle(testing_data)
     window_size_by_2=2.8
     wrongly_classfied=0
     for i in range(len(testing_data)):
         window_left=testing_data[i][0]-window_size_by_2
         window_right=testing_data[i][0]+window_size_by_2
         window_top=testing_data[i][1]+window_size_by_2
         window_bottom=testing_data[i][1]-window_size_by_2

         predicted_class=-1
         count_mini=0
         for c in range(3):
             count=0
             for data in training_data[c]:
                 if data[0]>=window_left and data[0]<=window_right and data[1]>=window_bottom and data[1]<=window_top:
                     count+=1
             if count>count_mini:
                 count_mini=count
                 predicted_class=c

         if predicted_class==0:
             plt.plot(testing_data[i][0], testing_data[i][1],marker='o', markersize=1, color="red")
         if predicted_class==1:
             plt.plot(testing_data[i][0], testing_data[i][1],marker='o', markersize=1, color="green")
         if predicted_class==2:
             plt.plot(testing_data[i][0], testing_data[i][1],marker='o', markersize=1, color="blue")
         wrongly_classfied+=abs(predicted_class-testing_data[i][2])

     plt.legend()
     plt.savefig('result.png')
     # plt.savefig('result.pdf')
     plt.show()
     print("Model accuracy is ",float((len(testing_data)-wrongly_classfied)/len(testing_data))*100,"%\n")
if __name__ == '__main__':
    main()
    # print("frist")
