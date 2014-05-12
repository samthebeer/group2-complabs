import numpy as np
import os
import sys
import re

term=os.system
pathn=os.getcwd()

term('./gulp <gulp_input> gulp.out')

data=open('test.out')
for line in data:
	if 'Final energy' in line:
	   E1= re.findall("\d+.\d+", line)[0]

runs = 100

for x in xrange(runs):
	print (x*100.0)/runs , x
	term('python mcmc.py')
	term('python gulpgen.py')
	term('./gulp <gulpin> gulp.out')
	data=open('gulp.out')
	for line in data:
		if 'Final energy' in line:
			E2= re.findall("\d+.\d+", line)[0]
	if E2 < E1:
		E1 = E2
		os.rename('new_cell','grid')

	
	
