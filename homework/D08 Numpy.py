import numpy as np
name_list = ['小明','小華','小菁','小美','小張','John','Mark','Tom']
sex_list = ['boy','boy','girl','girl','boy','boy','boy','boy']
weight_list = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]
rank_list = [8,1,5,4,7,6,2,3]
myopia_list = [True,True,False,False,True,True,False,False]


student_data={'names':('name','sex','weight','rank','myopia'),'formats':('U10','U6','f8','i3','?')}
student_data['name']=name_list
student_data['sex']=sex_list
student_data['weight']=weight_list
student_data['rank']=rank_list
student_data['myopia']=myopia_list



print("total mean",np.mean(student_data['weight']))

boy_idx=np.where(student_data['sex']=='boy')[0]
np.mean(student_data['weight'][boy_idx])


girl_idx=np.where(student_data['sex']=="girl")[0]

np.mean(student_data['weight'][girl_idx])