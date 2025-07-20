import pandas as pd
import pickle
Job_dict = pickle.load(open('/home/tushar/job/Job_recom.pkl', 'rb'))
data = pd.DataFrame(Job_dict)
l = 'C++'
if l in data['skills'].values:
    print('yES')
else:
    print('no')
# print(data)
# print(data.shape)