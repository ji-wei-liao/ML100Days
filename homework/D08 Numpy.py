import numpy as np
name_list = ['小明','小華','小菁','小美','小張','John','Mark','Tom']
sex_list = ['boy','boy','girl','girl','boy','boy','boy','boy']
weight_list = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]
rank_list = [8,1,5,4,7,6,2,3]
myopia_list = [True,True,False,False,True,True,False,False]

student_data=np.dtype('U17,U13,f8,int,?')
student_data=np.dtype({'names':('Name','sex','weight','rank','myopia'),'formats':('U17','U13','f8','int','?')})
student_data[0]=[name_list[0],sex_list[0],weight_list[0],rank_list[0],myopia_list[0]]
student_data[1]=[name_list[1],sex_list[1],weight_list[1],rank_list[1],myopia_list[1]]

print(student_data[0])
