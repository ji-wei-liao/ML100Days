import numpy as np
name_list = ['小明','小華','小菁','小美','小張','John','Mark','Tom']
sex_list = ['boy','boy','girl','girl','boy','boy','boy','boy']
weight_list = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]
rank_list = [8,1,5,4,7,6,2,3]
myopia_list = [True,True,False,False,True,True,False,False]


student_type={'names':('name','sex','weight','rank','myopia'),'formats':('U10','U6','f8','i4','?')}
students=np.zeros(8,dtype=student_type)
students['name']=name_list
students['sex']=sex_list
students['weight']=weight_list
students['rank']=rank_list
students['myopia']=myopia_list



print("total mean",np.mean(students['weight']))


boy_idx=np.where(students['sex']=='boy')[0]

print(np.mean(students['weight'][boy_idx]))


girl_idx=np.where(students['sex']=="girl")[0]

print(np.mean(students['weight'][girl_idx]))