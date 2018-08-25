import os

m_path = os.getcwd()+'\\'
START_INDEX = 1

num_name_list = []
for i in os.listdir(m_path):
    if os.path.isdir(i):
        num_name_list.append(int(i))

    
print(num_name_list)

def renameDir(l):
    for i in range(START_INDEX,len(l)+START_INDEX):
        os.rename(m_path+str(min(l)),m_path+str(i))
        l.remove(min(l))
        
renameDir(num_name_list)
    