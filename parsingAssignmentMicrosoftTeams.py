'''
Heirarchical files in Microsoft Teams:
Submitted files/
	- Student-1 Name/
		- Assignment-1/
			- Version 1/
				- file-1.*
				- file-2.*
				.
				.
			- Version 2/
				- file-1.*
				- file-2.*
				.
				.
		- Assignment-2/
			- Version-1/
				.
				.
	- Student-2 Name/
		.
		.

Result of this code (more satisfying):
Assignment-1/
	- Student-1 Name/
		- file-1.* (from Version 1/)
		- file-1.* (from Version 2/)
		- file-2.* .....
	- Student-2 Name/
		.
		.

by Sudiro (sudiro@mail.ugm.ac.id or sudiroeen@gmail.com)
'''

import numpy as np 
import os
import shutil

parent1 = 'Submitted files/'
names = os.listdir(parent1)

for nf in names:
	dirname = parent1 + nf + '/'
	if os.path.isdir(dirname):
		for npr in os.listdir(dirname):
			insidePR = parent1 + nf + '/' + npr + '/'
			os.makedir(insidePR)
			desdir = insidePR + nf
			os.mkdir(desdir)
			for version in os.listdir(insidePR):
				nversfolder = insidePR + version + '/'
				if os.path.isdir(nversfolder):
					files = os.listdir(nversfolder)
					for f in files:
						nfile = nversfolder + f
						shutil.copy(nfile, desdir + '/' + f)

