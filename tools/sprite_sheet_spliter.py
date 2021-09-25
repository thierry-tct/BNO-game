import pygame, os
pygame.init()
path = 'C:/Users/THIERRY/Desktop\BNO\images\kenpachi'
#path = raw_input('enter file folder path')
ncouleur = input('enter the number of  colors ( sauf normal ( original))')
couleurs = []			# colors name . exemple 'normal'
other_sheet = []		# colors images
for i in range(ncouleur) :
	print 'input the name of color ',i+1
	couleurs += [raw_input()]
	aux = pygame.image.load(os.path.join('data',path + '/' + couleurs[-1] + '.png'))
	other_sheet += [aux]
name = raw_input('enter file name normal')
sheet = pygame.image.load(os.path.join('data',path + '/' + name + '.png'))

############### pour creer le fichier de structure de donnee 
f = open(path + '/images.txt' , 'w')
g = open(path + '/type_position.txt' , 'w')
f.write('{')
g.write('{')
###############

hauteur = sheet.get_height()
largeur = sheet.get_width()
image_array = []		#a la fin est de la forme [[(ligne 1):y_haut,y_bas,[(image 1):x_gauche,x_droite,y_haut,y_bas]...]...]
row = 0
bool = 1
while row < hauteur :
	col=0
	color = sheet.get_at((col,row))
	while  color.a == 0 :		#get the alpha value , if 0 (tranparence), continu
		col +=1
		if col >= largeur :
			break
		color = sheet.get_at((col,row))
	if col < largeur :
		if bool :
			image_array +=	[[]]
			image_array[-1] += [row]	 #met ligne de y_haut
			bool = 0
	else :
		if bool==0 :
			image_array[-1] += [row]	  #met ligne de y_bas
		bool = 1
	row += 1
if bool == 0 :
	image_array[-1] += [row-1]		#cas ou l'image touche le bas
print 'number of lines : ',len(image_array)
# a ce stage on a ttes les lignes now on traite les colones

for line in range(len(image_array)) :
	row = 0
	bool = 1
	while row < largeur :
		col=image_array[line][0]
		color = sheet.get_at((row,col))
		while  color.a == 0 :		#get the alpha value , if 0 (tranparence) continu
			col +=1
			if col > image_array[line][1] :
				break
			color = sheet.get_at((row,col))
		if col <= image_array[line][1] :
			if bool :
				image_array[line] +=	[[]]
				image_array[line][-1] += [row]	 #met ligne de x_gauche
				bool = 0
		else :
			if bool==0 :
				image_array[line][-1] += [row]	  #met ligne de x_droite
				image_array[line][-1] += [image_array[line][0]]
				image_array[line][-1] += [image_array[line][1]]
			bool = 1
		row += 1
	if bool == 0 :
		image_array[line][-1] += [row-1]		#cas ou l'image touche la droite
		image_array[line][-1] += [image_array[line][0]]
		image_array[line][-1] += [image_array[line][1]]

# now on a ttes les images maintenat on les crop
previous = ['',0]		#previous : [output_folder,last output file name]
for i in range(len(image_array)) :
	double_ligne = 0
	print 'input output folder name for the line ',i+1 
	output_folder = raw_input()
	while(output_folder == '') :		# pour traiter le cas ou de type de sprite sur meme ligne
		n = input('enter the indice where start the second folder ( indice start at 0 )')
		output_folder = raw_input("input the folder for the firsts")
		double_ligne = 1

	####################
	f.write(" '")
	f.write(output_folder)
	f.write(" ' : [")
	g.write(" '")
	g.write(output_folder)
	g.write(" ' : [")
	####################
	
	output_folder = '/' + output_folder + '/'
	num = 3               			# used pour compter quand y'a plusieurs dossier par ligne le num du dossier prochain
	
	j = 2
	spr_nam = j-2				# nom de sprites (0.png , 1.png , ....
	while j < len(image_array[i]) :		# pour chaque sprite

		col = image_array[i][j][0]	# x_gauche
		bool = 1
		while bool :
			row = image_array[i][j][2]	
			color = sheet.get_at((col,row))
			while color.a == 0 :
				if row >= image_array[i][j][3] :
					break 	
				row += 1
				color = sheet.get_at((col,row))
			if color.a != 0	:
				bool = 0
				image_array[i][j][0] = col
			col +=1
		
		col = image_array[i][j][1]	# x_droite
		bool = 1
		while bool :
			row = image_array[i][j][2]	
			color = sheet.get_at((col,row))
			while color.a == 0 :
				if row >= image_array[i][j][3] :
					break 	
				row += 1
				color = sheet.get_at((col,row))
			if color.a != 0	:
				bool = 0
				image_array[i][j][1] = col
			col -=1

		col = image_array[i][j][2]	# y_haut
		bool = 1
		while bool :
			row = image_array[i][j][0]	
			color = sheet.get_at((row,col))
			while color.a == 0 :
				if row >= image_array[i][j][1] :
					break 	
				row += 1
				color = sheet.get_at((row,col))
			if color.a != 0	:
				bool = 0
				image_array[i][j][2] = col
			col +=1
		
		col = image_array[i][j][3]	# y_bas
		bool = 1
		while bool :
			row = image_array[i][j][0]	
			color = sheet.get_at((row,col))
			while color.a == 0 :
				if row >= image_array[i][j][1] :
					break 	
				row += 1
				color = sheet.get_at((row,col))
			if color.a != 0	:
				bool = 0
				image_array[i][j][3] = col
			col -=1

# now save the sprites

		
	# cas plusieurs dossiers sur mem ligne
		if double_ligne :
			if (j-2)==n :
				###################
				f.write("]")
				g.write("]")
				###################
				double_ligne = 0
				previous[0] = output_folder
				previous[1] = spr_nam + 1
				output_folder = raw_input("input the folder for the nexts")
				while(output_folder == '') :		# pour traiter le cas ou de type de sprite sur meme ligne
					print 'enter the indice were start the', num ,'folder ( indice start at 0 )'
					n = input()
					print 'input the folder for the ',num-1,'th'
					output_folder = raw_input()
					double_ligne = 1
				num += 1
				####################
				f.write(",  '")
				f.write(output_folder)
				f.write(" ' : [")
				g.write(",  '")
				g.write(output_folder)
				g.write(" ' : [")
				####################
				output_folder = '/' + output_folder + '/'
				spr_nam = 0

	####
	# traite  le cas ou plusieurs lignes st ds le mem dossier
		if previous[0]==output_folder :
			spr_nam += previous[1]	
	###
		sprite_img = sheet.subsurface(image_array[i][j][0],image_array[i][j][2],image_array[i][j][1]-image_array[i][j][0]+1,image_array[i][j][3]-image_array[i][j][2]+1)
		if not os.path.isdir(os.path.join (path + '/normal' + output_folder )):
			os.makedirs(os.path.join (path + '/normal' + output_folder ))
		pygame.image.save(sprite_img , (os.path.join (path + '/normal' + output_folder + str(spr_nam) + '.png')))

		############## le 1er 0 de ch va etre remplace par la surface
		ch = '[0, '+ str(image_array[i][j][1]-image_array[i][j][0]+1)+ ',' + str(image_array[i][j][3]-image_array[i][j][2]+1)+'] '
		if spr_nam != 0 :
			ch = ' , '+ch
		f.write(ch)
		g.write(' 0 , 1 ')
		##############

		for k in range(ncouleur) :
			sprite_img = other_sheet[k].subsurface(image_array[i][j][0],image_array[i][j][2],image_array[i][j][1]-image_array[i][j][0]+1,image_array[i][j][3]-image_array[i][j][2]+1)
			if not os.path.isdir(os.path.join (path + '/' + couleurs[k] +  output_folder )):
				os.makedirs(os.path.join (path + '/' + couleurs[k] +  output_folder ))
			pygame.image.save(sprite_img , (os.path.join (path + '/' + couleurs[k] +  output_folder + str(spr_nam) + '.png')))
		j+=1
		spr_nam +=1
	# fin de while j<...
	#pour traiter  le cas ou plusieurs lignes st ds le mem dossier
	previous[0] = output_folder
	previous[1] = spr_nam 
	###################
	f.write("] ")
	g.write("] ")
	###################
###
###################
f.write("}")
g.write("}")
f.close()
g.close()
###################			
print 'finished'
fin=raw_input('press any key ...')
		

