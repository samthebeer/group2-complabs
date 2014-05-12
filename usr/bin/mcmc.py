import numpy as np
from random import randint

#loads shape of array
shape=np.loadtxt('dim')
#delta_E = np.loadtxt('energy')

#loads cell list as a 2d array
cell_lst= np.loadtxt('grid')

#reshapes cell list into original 3d array
cell_lst=cell_lst.reshape(shape)

#this function is for the swappiong method

def probability(E,T=1000,k_b=8.6173324E-5):
	return exp(-E/(k_b*T))

def swap(lst,cell=cell_lst):
	num = randint(0,len(swaplist)-1)
	ca = swaplist[num][0]
	mg = swaplist[num][1]
	cell_lst[ca[0]][ca[1]][ca[2]],cell_lst[mg[0]][mg[1]][mg[2]] = cell_lst[mg[0]][mg[1]][mg[2]], cell_lst[ca[0]][ca[1]][ca[2]]
	

def mcmc(cell_lst,shape):
	x,y,z=tuple(shape)

	swaplist = []
	for a in xrange(int(x)):
		for b in xrange(int(y)):
			for c in xrange(int(z)):
				#if current atom is calcium
				if cell_lst[a][b][c] == 3:
					#scan through corners
					for nx in xrange(-1,2):
						na = a + nx
						for ny in xrange(-1,2):
							nb = b + ny
							for nz in xrange(-1,2):
								nc = c + nz
								if (-1 < na < x) and (-1 < nb < y) and (-1 < nc < z):
									if cell_lst[na][nb][nc] == 2:
										swaplist.append([[a,b,c],[na,nb,nc]])
	return swaplist

swaplist = mcmc(cell_lst,shape)			

cell_lst = swap(swaplist)

with file('new_cell', 'w') as f:
	f.write('#shape: (%s, %s, %s)\n' % (int(x),int(y),int(z)))	
	for layer in xrange(z):
		np.savetxt(f,cell_lst[:][:][layer],fmt='%d')
		f.write('#new layer\n')

				
