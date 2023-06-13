import os
import time
import glob


path = "/home/sanaz/IDP/directories/direct1/*"

list_files = glob.glob(path)
#print(list_files)
fp = open('/home/sanaz/IDP/projects/file.txt', 'w')
for file in list_files:
    ti_c = os.path.getctime (file)
    ti_m = os.path.getmtime (file)
    c_ti = time.ctime ( ti_c )
    m_ti = time.ctime ( ti_m )
    fp.write(file)
    fp.write(c_ti)
    fp.write(m_ti)
fp.close()
