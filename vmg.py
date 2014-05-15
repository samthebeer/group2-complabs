from visual import *
import numpy as np
import re
Stage=0
Stage=1
data=open('gulpin')
condition_initial = False
condition_final= False

for line in data:
    if Stage==1:
        if 'cartesian region 1' in line:
            condition_initial = True
        if condition_initial == True:
            if 'Mg ' in line:
                posi=re.findall("\d+.\d+", line)
                posi=[float(i) for i in posi]
                posi=np.array(posi[:3])
                sphere(pos=posi, radius=0.25)
        if 'Constraints' in line:
            condition_initial = False

