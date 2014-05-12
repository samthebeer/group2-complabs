#! /usr/bin/python
import numpy as np


#defining cores and shells here, the %s's represent the x,y,z coords as cartesians or fractionals depending on flags

fname = 'gulpin'
#code below commented out for development at later date
#c_type = str(sys.argv[1]) #argument here defines whether fractional or absolute co-ords are used

#The co_ordinates are going to have maximum and minimum values in terms of the cell defined
#these max values are defined as number of atoms, not the absolute values and will therefore be integers
scale=2.11769


shape=np.loadtxt('dim')

cell_lst= np.loadtxt('new_cell')

cell_lst=cell_lst.reshape(shape)
x,y,z=tuple(shape)
x=int(x)
y=int(y)
z=int(z)
#section for writing input file to gulp
#first four lines:
gridscale =  x*scale
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
