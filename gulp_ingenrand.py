#! /usr/bin/python
import numpy as np
import random
random.seed()


#defining cores and shells here, the %s's represent the x,y,z coords as cartesians or fractionals depending on flags

fname = 'gulp_input'

mg_core='Mg   core    %s    %s   %s' # %s = x,y,z

ox_core='O    core    %s    %s   %s' # %s = x,y,z
ox_shell= 'O     shel %s %s %s' # %s = x,y,z

ca_core='Ca core %s %s %s' # %s = x,y,z

#code below commented out for development at later date

#The co_ordinates are going to have maximum and minimum values in terms of the cell defined
#these max values are defined as number of atoms, not the absolute values and will therefore be integers
scale=2.11769

#general structure for this code
#two options, iterate through the x,y and z axis placing atoms individually
#or create line of atoms, from line generate 1 layer
#from 1 layer generate cube

#dimensions of cube
m=8
x=m
y=m
z=m		

gridscale = m*scale
#this function is for putting in the placeholder '1' for when oxygen is present in the lattice, 2 for magnesium and 3 for calcium
def isox(a,b,c,m):
	if (a+b+c)%2 == 0:
		return 1
	elif c < m/2:
		r=random.random()
			if (r<0.7):
				return 2
			else:
				return 3

	else:
		r=random.random()
			if (r<0.7):
				return 3
			else:
				return 2


#cell_lst=np.array([[[0]*m]*m]*m)
cell_lst = [[[0 for k in xrange(x)] for j in xrange(y)] for i in xrange(z)]
scale = 2.11769
#this section of the code fills in all of the oxygen, magnesium and calcium placeholders in the lattice
for a in xrange(0,x):
	for b in xrange(0,y):
		for c in xrange(0,z):
			cell_lst[a][b][c] = isox(a,b,c,m)

#the following section is to write the cell to a human readable array.
#in another script a mcmc will be applied to this
np.savetxt('dim',[x,y,z],fmt='%d')
with file('grid', 'w') as f:
	f.write('#shape: (%s, %s, %s)\n' % (int(x),int(y),int(z)))	
	for layer in xrange(z):
		np.savetxt(f,cell_lst[:][:][layer],fmt='%d')
		f.write('#new layer\n')



#section for writing input file to gulp
#first four lines:
fst= 'opti conp\ncell\n%f %f %f 90.0 90.0 90.0\ncartesian region 1' %(gridscale, gridscale, gridscale)

#last lines
charges='species\nMg	core	2.000000\nCa	   core    2.000000\nO      core    0.869020\nO      shel   -2.869020'
bucks='buck\nMg core O shel 1280.00 0.300000 4.500000 0.000 12.00\nbuck\nCa core O shel 1420.00 0.300000 6.300000 0.000 10.00\nbuck\nO  shel O shel 22764.3 0.149000 20.37000 0.000 8.000'
springs='spring\nO      51.708000\ndump every GULPMgOCaO.res'

lst = charges +'\n' + bucks + '\n'+springs

#this function returns a string containing the co-ordinates and type of atom

def whichatom(item,a,b,c,scale):
	mg_core='Mg    core    %f    %f    %f' # %s = x,y,z
	ox_core='O     core    %f    %f    %f' # %s = x,y,z
	ox_shel='O     shel    %f    %f    %f' # %s = x,y,z
	ca_core='Ca    core    %f    %f    %f' # %s = x,y,z
	if item == 1:
		oxc = ox_core % (a*scale,b*scale,c*scale)
		oxs = ox_shel % (a*scale,b*scale,c*scale)
		return oxc + '\n' + oxs	
	elif item == 2:
		return mg_core % (a*scale,b*scale,c*scale)
	elif item == 3:
		return ca_core % (a*scale,b*scale,c*scale)
	


#this section is for iterating through the array to output the co-ordinates and other info of the cell
atom_lst=''

for a in xrange(0,x):
	for b in xrange(0,y):
		for c in xrange(0,z):
			atom_lst += whichatom(cell_lst[a][b][c],a,b,c,scale) + '\n'

#coalates all strings to write to file
info= fst + '\n' + atom_lst + lst

with open(fname, 'w+') as inf:
   print >> inf, info
inf.close
