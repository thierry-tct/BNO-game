import random
XCONST = 1.4
YCONST = 1.2
R_S = int(round (60 * XCONST))		#RUN_SPEED
W_S = int(round (20 * XCONST))		#WALK_SPEED
AVER_PROF = 10		#AVERAGE PROFONDEUR
M_H = int(round (150 * YCONST))		#MID_HEIGH
HEIGH = int(round (300 * YCONST))
F_H = int(round (75 * YCONST))		#FOURTH_HEIGHT
J_S = int(round (40 * XCONST))		#JUMP_SPEED
RUN_BACK_HIGHT = int(round (30 * YCONST))
WEAK = 4		#profondeur unite 
JUMP_LENGHT = 10		#nombre d'images de jump... ici c 7 images 0.png ... 6.png utilise pour weak attack air

def ymax():
	return int(round (HEIGH / YCONST))

def clavier(input_,cur_key,index,prev_base,bankai) :  		# input est un entier correspondant a la sequence du clavier : ex : walk avant c'est 4
				#format : [nom ds dico,[sequence d'affichage],[profondeurs],[y(qd ca monte),vitesse(augmentation de x)
				# profondeur 0 veut dire intouchable . exemple teleport 
	h = HEIGH-prev_base
	if bankai:
		index %=  JUMP_LENGHT-4	    # pour les cas ou clavier est call pour autre chose index > jump_lenght et a air_dash il y aurait depasse index 
		intro = ['intro',[0,1,2],[1,1,1],[0,0,0],[0,0,0]]				#0 
		win = ['win' , [0,0,1,1,2,2],[1,1,1,1,1,1],[0,0,0,0,0,0],[0,0,0,0,0,0]]		#1
		stance = ['bankai/stance' , [0,0],[1,1],[0,0],[0,0]]		#2
		turn = 0							#3
		walk_avant = ['bankai/stance',[0,0],[1,1],[0,0],[2*W_S,2*W_S]]		#4
		walk_back = ['bankai/stance',[0,0],[1,1],[0,0],[-2*W_S,-2*W_S]]		#5
		jump = ['bankai/jump' , [0,0,0,0,0,0],[1,1,1,1,1,1],[F_H,F_H/2+M_H,HEIGH,HEIGH,F_H/2+M_H,F_H],[0,0,0,0,0,0]]	#6	
		run_avant = ['bankai/air dash',[0,0,0],[1,1,1],[0,0,0],[int(round(1.5*R_S)),int(round(1.5*R_S)),int(round(1.5*R_S))]]								#7
		run_back = ['bankai/stance',[0,0,0],[1,1,1],[RUN_BACK_HIGHT,RUN_BACK_HIGHT,RUN_BACK_HIGHT],[-int(round(1.5*R_S)),-int(round(1.5*R_S)),-int(round(1.5*R_S))]]			#8
		crouch = ['bankai/attack crouch g' , [0,0],[-1,-1],[0,0],[0,0]]			#-1 pour crouch 1 pour ni bloque ni attack ; attack est - ou +2			#9
		crouch_turn = 0											#10
		air_dash = ['bankai/air dash' , [0,0],[1,1],[prev_base ,prev_base],[2*J_S,2*J_S]]	# le y est celui de la prchaine image de jump  		#11
		forward_jump = ['bankai/forward jump' , [0,0,1,1,2,2],[1,1,1,1,1,1],[F_H,F_H/2+M_H,HEIGH,HEIGH,F_H/2+M_H,F_H],[int(round(1.5*J_S)),int(round(1.5*J_S)),int(round(1.5*J_S)),int(round(1.5*J_S)),int(round(1.5*J_S)),int(round(1.5*J_S))]]	#12
		backward_jump = ['bankai/jump' ,  [0,0,0,0,0,0],[1,1,1,1,1,1],[F_H,F_H/2+M_H,HEIGH,HEIGH,F_H/2+M_H,F_H],[-int(round(1.5*J_S)),-int(round(1.5*J_S)),-int(round(1.5*J_S)),-int(round(1.5*J_S)),-int(round(1.5*J_S)),-int(round(1.5*J_S))]]		#13
		teleport_avant = ['bankai/teleport' , [0,0] , [2,2] , [0,0] , [2*R_S,2*R_S]]								#14
		teleport_back = ['bankai/teleport' , [0,0] , [2,2] , [0,0] , [-2*R_S,-2*R_S]]							#15	
		up_guard = ['bankai/teleport' , [0,0] , [1,1] , [0,0] ,[0,0]]	#mm nbre d'elts que walk back           		#16
		down_guard = ['bankai/attack crouch g' , [0,0] , [-1,-1] , [0,0] ,[0,0]]				#mm nbre d'elts que crouch					#17
		damage_upup = ['bankai/stance' , [0,0] , [1,1] ,[max(prev_base-RUN_BACK_HIGHT,0),max(prev_base-RUN_BACK_HIGHT , 0)] , [-2*W_S,0]]			#18
		damage_updown = ['bankai/stance' , [0,0] , [1,1] ,[prev_base,prev_base] , [-2*W_S,0]] 									#19
		damage_down = ['bankai/attack crouch g' , [0,0] , [-1,-1] ,[prev_base,prev_base] , [-2*W_S,0]]									#20
		fall1 = ['bankai/attack crouch g' , [0,0,0,0,0] ,[0,0,0,0,0] , [M_H,M_H,F_H,-10,0] , [0,0,0,0,0]]					#21 
		fall2 = ['bankai/special move a g' , [0,0,0,0,0,0,8,8] ,[0,0,0,0,0,0,0,0] , [0,0,0,0,0,0,0,0] , [0,0,0,0,0,0,0,0]]						#22
		weak_attack = 0						#23 
		weak_attack_crouch = 0		#24
		weak_attack_crouch_p = 0  #25
	
		####@@ pour l'air
		if cur_key == 6 :		#jump
			prevact = jump
		elif cur_key == 12 : 		#forward jump
			prevact = forward_jump
		elif cur_key == 13 :		#backward jump 
			prevact = backward_jump
		else :
			[bl,index,cur_key] = descendre(12 , prev_base ,bankai)
			prevact = forward_jump
			if index > 0 :
				index -= 1                    #car en bas on ajoute 1
			else :
				index = JUMP_LENGHT -4 - 2
		if index < JUMP_LENGHT -4 - 1 :
			index += 1
		n = JUMP_LENGHT -4 - index	# car index est ce qui devrait etre affiche si on ne breakait pas n est le nbre d'image a prendre ds weak attack air	
		#####@@@	
		weak_attack_air = 0	#26
		weak_attack_air_p= 0 		#27
		weak_at_pied_air=0	#28
		strong_attack_g = ['bankai/attack g' , [0,1,2,3,4,5,6,7] , [1,2*WEAK,4*WEAK,2*WEAK,1,1,1,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]	#29
		strong_attack_p = ['bankai/attack p' , [0,1,2] , [1,4*WEAK,1],[0,0,0],[0,0,0]]					#30
		strong_attack_crouch_g = ['bankai/attack crouch g' ,[0,1,2,3,4] , [-1,-3*WEAK,-2*WEAK,-1,-1] , [0,0,0,0,0] , [-1,-1,-1,-1,-1]]	#31
		strong_attack_crouch_p = ['bankai/attack crouch p' ,[0,1,2] , [-1,-3*WEAK,-1] , [0,0,0] , [-1,-1,-1,-1]]	#32
		strong_attack_air_g = ['bankai/attack air g',[0,1,2,3,4,5,6,7,7,7][:n] , [-1,3*WEAK,3*WEAK,2*WEAK,2*WEAK,-1,-1,-1,-1,-1][:n] , prevact[3][index:] , prevact[4][index:]]	#33
		strong_attack_air_p = ['bankai/attack air p',[0,1,1,1,1,1,1,1,1,1][:n] , [-1,3*WEAK,2*WEAK,-1,-1,-1,-1,-1,-1,-1][:n] , prevact[3][index:] , prevact[4][index:]]	#34
		strongest_attack_g = 0		#35
		strongest_attack_p = 0	#36
		strongest_a_crouch_g = 0		#37		DOIT SE FAIRE LE JOUER ETANT DEBOUT de mem strongest_a_crouch_p (38)
		strongest_a_crouch_p = 0	#38
		strongest_a_air_g = 0	#39
		strongest_a_air_p =  0	#40
		throw = ['bankai/attack p' , [2,2,2,2] , [5*WEAK ,0,0,0] , [0,0,0,0] ,[0,0,0,0]]	#41
		throw_miss = ['bankai/teleport' , [0,0,0,0,0] , [2,2,2,2,2] , [0,0,0,0,0,0] ,[0,0,0,0,0,0]]		#42
		a=prev_base #prevact[3][index]
		throw_air= ['bankai/attack p' , [2,2,2,2,2,2,2,2,2,2,2,2,2][:n+6] , [5*WEAK ,0,0,0,0,0,0,0,0,0,0,0,0][:n+6] , [a,a,a,a,a,a]+prevact[3][index:] , [0,0,0,0,0,0]+prevact[4][index:]]	#43
		throw_a_miss=['bankai/teleport' , [0,0,0,0,0,0,0,0,0,0,0,0][:n] , [2,2,2,2,2,1,1,1,1,1,1,1][:n] , prevact[3][index:] , prevact[4][index:]]		#44
		special_a_g=['bankai/special move a g' , [0,1,2,3,4,5,6,7,8] , [1,1,1,1,6*WEAK,3*WEAK,2*WEAK,1,1],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,-W_S,0,0]]		#45
		special_a_p=['bankai/special move a p' , [0,1,2,3,4,5,6,7] , [1,1,1,1,2*WEAK,4*WEAK,2*WEAK,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,-W_S,0,0]]		#46
		special_d = 0	 #47
		special_b_g = 0 	#48
		special_b_p = 0		#49
		super_a = 0		#50
		super_b = 0		#51
		special_e_g = 0              #52
		special_c_g = 0    #53
		special_c_p = 0     #54
		transform_back = ['bankai/transform back' , [0,0,0,0,0,0,0,0][:n]+[0,1,2,3,4,5,6,7] , [0,0,0,0,0,0,0,0][:n]+[0,0,0,0,0,0,0,0] , prevact[3][index:]+[0,0,0,0,0,0,0,0] , prevact[4][index:]+[0,0,0,0,0,0,0,0]]     #55
	else :
		index %=  JUMP_LENGHT	# pour les cas ou clavier est call pour autre chose index > jump_lenght et a air_dash il y aurait depasse index 
		intro = ['intro',[0,1,2],[1,1,1],[0,0,0],[0,0,0]]				#0 
		win = ['win' , [0,0,1,1,2,2],[1,1,1,1,1,1],[0,0,0,0,0,0],[0,0,0,0,0,0]]		#1
		stance = ['stance' , [0,1,2,3,4,5,6,7,8],[1,1,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]		#2
		turn = ['turn',[0,1],[1,1],[0,0],[0,0]]							#3
		walk_avant = ['walk',[0,1,2,3,4,5,6,7],[1,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0],[W_S,W_S,W_S,W_S,W_S,W_S,W_S,W_S]]		#4
		walk_back = ['walk' , [7,6,5,4,3,2,1,0],[1,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0],[-W_S,-W_S,-W_S,-W_S,-W_S,-W_S,-W_S,-W_S]]		#5
		jump = ['jump' , [0,1,1,1,2,2,3,3,3,4],[1,1,1,1,1,1,1,1,1,1],[0,F_H,M_H,F_H+M_H,HEIGH,HEIGH,F_H+M_H,M_H,F_H,0],[0,0,0,0,0,0,0,0,0,0]]	#6	
		run_avant = ['run',[0,1,2,3,4,5],[1,1,1,1,1,1],[0,0,0,0,0,0],[R_S,R_S,R_S,R_S,R_S,R_S]]								#7
		run_back = ['stance',[3,3,1],[1,1,1],[RUN_BACK_HIGHT,RUN_BACK_HIGHT,RUN_BACK_HIGHT],[-R_S,-R_S,-R_S]]			#8
		crouch = ['crouch' , [0,1],[-1,-1],[0,0],[0,0]]			#-1 pour crouch 1 pour ni bloque ni attack ; attack est - ou +2			#9
		crouch_turn = ['crouch turn' , [0,1],[-1,-1],[0,0],[0,0]]											#10
		air_dash = ['air dash' , [0,1],[1,1],[prev_base ,prev_base],[J_S,J_S]]	# le y est celui de la prchaine image de jump  		#11
		forward_jump = ['forward jump' , [0,1,1,1,2,2,3,3,3,4],[1,1,1,1,1,1,1,1,1,1],[0,F_H,M_H,F_H+M_H,HEIGH,HEIGH,F_H+M_H,M_H,F_H,0],[J_S,J_S,J_S,J_S,J_S,J_S,J_S,J_S,J_S,J_S]]	#12
		backward_jump = ['jump' ,  [0,1,1,1,2,2,3,3,3,4],[1,1,1,1,1,1,1,1,1,1],[0,F_H,M_H,F_H+M_H,HEIGH,HEIGH,F_H+M_H,M_H,F_H,0],[-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,-J_S]]		#13
		teleport_avant = ['teleport' , [0,1,2,1] , [1,0,0,0] , [0,0,0,0] , [R_S,R_S,R_S,R_S]]								#14
		teleport_back = ['teleport' , [0,1,2,1] , [1,0,0,0] , [0,0,0,0] , [-R_S,-R_S,-R_S,-R_S]]							#15	
		up_guard = ['guard' , [0,0,0,0,0,0,0,0] , [1,1,1,1,1,1,1,1] , [0,0,0,0,0,0,0,0] ,[0,0,0,0,0,0,0,0]]	#mm nbre d'elts que walk back           		#16
		down_guard = ['guard' , [1,1] , [-1,-1] , [0,0] ,[0,0]]				#mm nbre d'elts que crouch					#17
		damage_upup = ['damage' , [1,2] , [1,1] ,[max(prev_base-RUN_BACK_HIGHT,0),max(prev_base-RUN_BACK_HIGHT , 0)] , [-2*W_S,0]]			#18
		damage_updown = ['damage' , [3,4] , [1,1] ,[prev_base,prev_base] , [-2*W_S,0]] 									#19
		damage_down = ['damage' , [5,6] , [-1,-1] ,[prev_base,prev_base] , [-2*W_S,0]]									#20
		fall1 = ['fall down 1' , [0,1,2,3,4] ,[0,0,0,0,0] , [M_H,M_H,F_H,-10,0] , [0,0,0,0,0]]					#21 
		fall2 = ['fall down 2' , [0,1,2,3,4,5,6,7] ,[0,0,0,0,0,0,0,0] , [0,0,0,0,0,0,-10,0] , [0,0,0,0,0,0,0,0]]						#22
		weak_attack = ['weak attack' ,[0,1,2] , [1,2*WEAK,1] , [0,0,0] , [-1,-1,-1]]						#23 
		weak_attack_crouch = ['weak attack crouch' ,[0,1,2,3] , [-1,-2*WEAK,-1.5*WEAK,-1] , [0,0,0,0] , [-1,-1,-1,-1]]		#24
		weak_attack_crouch_p = 0  #25
	
		####@@ pour l'air
		if cur_key == 6 :		#jump
			prevact = jump
		elif cur_key == 12 : 		#forward jump
			prevact = forward_jump
		elif cur_key == 13 :		#backward jump 
			prevact = backward_jump
		else :
			[bl,index,cur_key] = descendre(12 , prev_base ,bankai)
			prevact = forward_jump
			if index > 0 :
				index -= 1                    #car en bas on ajoute 1
			else :
				index = JUMP_LENGHT - 2
		if index < JUMP_LENGHT - 1 :
			index += 1
		n = JUMP_LENGHT - index	# car index est ce qui devrait etre affiche si on ne breakait pas n est le nbre d'image a prendre ds weak attack air	
		#####@@@	
		weak_attack_air = ['weak attack air',[0,1,2,3,3,3,3,3,3,3][:n] , [-1,2*WEAK,1.5*WEAK,-1,-1,-1,-1,-1,-1,-1][:n] , prevact[3][index:] , prevact[4][index:]]	#26
		weak_attack_air_p= 0 		#27
		weak_at_pied_air=0	#28
		strong_attack_g = ['strong attack g' , [0,1,2,3,4,5,6,7,8] , [1,2*WEAK,4*WEAK,2*WEAK,1,1,1,1,1],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]	#29
		strong_attack_p = ['strong attack p' , [0,1,2,3] , [1,4*WEAK,1,1],[0,0,0,0],[0,0,0,0]]					#30
		strong_attack_crouch_g = ['strong attack crouch g' ,[0,1,2,3,4] , [-1,-3*WEAK,-2*WEAK,-1,-1] , [0,0,0,0,0] , [-1,-1,-1,-1,-1]]	#31
		strong_attack_crouch_p = ['strong attack crouch p' ,[0,1,2] , [-1,-3*WEAK,-1] , [0,0,0] , [-1,-1,-1,-1]]	#32
		strong_attack_air_g = ['strong attack air g',[0,1,2,3,4,5,6,6,6,6][:n] , [-1,3*WEAK,3*WEAK,2*WEAK,-1,-1,-1,-1,-1,-1][:n] , prevact[3][index:] , prevact[4][index:]]	#33
		strong_attack_air_p = ['strong attack air p',[0,1,2,2,2,2,2,2,2,2][:n] , [-1,3*WEAK,-1,-1,-1,-1,-1,-1,-1,-1][:n] , prevact[3][index:] , prevact[4][index:]]	#34
		strongest_attack_g = ['strongest attack g' , [0,1,2,2,3,4,5,6,7,8,9] , [1,1,1,1,4*WEAK,4*WEAK,4*WEAK,WEAK,1,1,1],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0]]		#35
		strongest_attack_p = ['strongest attack p' , [0,1,2,3,4,5] , [1,1,1,2*WEAK,4*WEAK,1],[0,0,0,0,0,0],[0,0,0,0,0,0]]	#36
		strongest_a_crouch_g = ['strongest attack crouch g' , [0,1,2,3,4,5,6,7,8] , [-1,-1,-1,-WEAK,-4*WEAK,-3*WEAK,-1,-1,-1,-1],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0] ,'extra']		#37		DOIT SE FAIRE LE JOUER ETANT DEBOUT de mem strongest_a_crouch_p (38)
		strongest_a_crouch_p = ['strongest attack crouch p' , [0,1,2,3,4,5,6,7] , [-1,-1,-1,-WEAK,-3*WEAK,-2*WEAK,-1,-1,-1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0] ,'extra']	#38
		strongest_a_air_g = ['strongest attack air g' , [0,1,2,3,4,5,6,7,7,7][:n] , [1,5*WEAK,3*WEAK,2*WEAK,WEAK,1,1,1,1,1][:n], prevact[3][index:] , prevact[4][index:]]	#39
		strongest_a_air_p = ['strongest attack air p' , [0,1,1,1,1,1,1,1,1,1][:n] , [1,3*WEAK,2*WEAK,1*WEAK,1,1,1,1,1,1][:n],prevact[3][index:] , prevact[4][index:]]	#40
		throw = ['throw' , [0,1,2,2,3,3,4,4] , [5*WEAK ,0,0,0,0,0,0,0] , [0,0,0,0,0,0,0,0] ,[0,0,0,0,0,0,0,0]]	#41
		throw_miss = ['throw miss' , [0,1,1,1,2] , [0,0,0,0,0] , [0,0,0,0,0,0] ,[0,0,0,0,0,0]]		#42
		a=prev_base #prevact[3][index]
		throw_air= ['throw air' , [0,1,2,3,3,4,4,0,0,0,0,0,0][:n+6] , [5*WEAK ,0,0,0,0,0,0,0,0,0,0,0,0][:n+6] , [a,a,a,a,a,a]+prevact[3][index:] , [0,0,0,0,0,0]+prevact[4][index:]]	#43
		throw_a_miss=['throw air miss' , [0,1,2,0,0,0,0,0,0,0,0,0][:n] , [0,0,0,0,0,0,0,0,0,0,0,0][:n] , prevact[3][index:] , prevact[4][index:]]		#44
		special_a_g=['special move a g' , [0,1,2,3,4,5,6,7] , [1,1,1,6*WEAK,3*WEAK,WEAK,1,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,-W_S,0,0]]		#45
		special_a_p=['special move a p' , [0,1,2,3,4,5,6,7] , [1,1,1,4*WEAK,2*WEAK,WEAK,1,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,-W_S,0,0]]		#46
		special_d = ['special move d' , [0,1,2,3,2,3,4,5] , [1,1,1,1,1,1,1,1] , [0,0,0,0,0,0,0,0] , [0,0,0,0,0,0,0,0]]	 #47
		special_b_g = ['special move c g' , [0,1,1,1,2,3,4,5,6,7,8,9] , [1,1,1,1,1, 3*WEAK, 5*WEAK, 7*WEAK,4*WEAK,1,1,1], [0,0,0,0,0,0,0,0,0,0,0,0], [0,2*R_S,2*R_S,2*R_S,2*R_S,2*R_S,R_S,R_S,R_S,R_S,W_S,0]]	#48
		special_b_p = ['special move c p' , [0,1,2,3,4,5,6,7] , [1,1,1,3*WEAK,6*WEAK,1,1,1],[0,0,0,0,0,0,0,0],[0,2*R_S,2*R_S,2*R_S,R_S,R_S,W_S,0]]		#49
		super_a = ['super move a g', [0,1,2,3,4,5,6,7,8,9,10], [1,1,1,1,4*WEAK,4*WEAK,2*WEAK,1,1,1,1], [0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0]]		#50
		super_b = ['super move b', [0,1,2,3,4,5,6,7,8,9,10,11,12,13,10,11,12,13,14], [1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]		#51
		special_e_g = ['special move e g', [0,1,2,3,4,5,6,7,8], [1,1,1,2*WEAK,2*WEAK,2*WEAK,1,1,1],[0,0,0,0,0,0,0,0,0],[0,0,R_S,R_S,R_S,0,0,0,0]]               #52
		special_c_g = ['special move c g',[0,1,2,3,4,5,6,7,8,9,10,11,12],[1,1,1,3*WEAK,2*WEAK,2*WEAK,WEAK,1,1,2*WEAK,2*WEAK,2*WEAK,1] , [0,0,0,F_H,M_H,F_H+M_H,HEIGH,HEIGH,F_H+M_H,M_H,F_H,0,0] , [0,0,0,W_S,W_S,W_S,W_S,W_S,W_S,W_S,W_S,0,0] ]     #53
		special_c_p = ['special move c p',[0,1,2,3,4,5,6,7,8],[1,1,1,3*WEAK,1,1,1,3*WEAK,1] , [0,0,0,F_H,M_H,F_H+M_H,M_H,F_H,0] , [0,0,0,W_S,W_S,W_S,W_S,W_S,0] ]     #54
		transform_back = 0      #55

	actions = [intro , win , stance , turn , walk_avant , walk_back , jump , run_avant , run_back  , crouch , crouch_turn , air_dash  , forward_jump  , backward_jump , teleport_avant ,teleport_back ,  up_guard , down_guard , damage_upup , damage_updown 
	           , damage_down , fall1 , fall2 , weak_attack ,  weak_attack_crouch , weak_attack_crouch_p ,weak_attack_air , weak_attack_air_p, weak_at_pied_air, strong_attack_g, strong_attack_p, strong_attack_crouch_g, strong_attack_crouch_p , strong_attack_air_g ,strong_attack_air_p
	           ,strongest_attack_g,strongest_attack_p ,strongest_a_crouch_g ,strongest_a_crouch_p,strongest_a_air_g 
	           , strongest_a_air_p , throw, throw_miss, throw_air, throw_a_miss, special_a_g,special_a_p, special_d, special_b_g, special_b_p,super_a, super_b, special_e_g,special_c_g,special_c_p,transform_back]
	
	return actions[input_] 

#########################
def stay_down():
	return ['fall down 2' , [0,1,2,3,4,5,6] ,[0,0,0,0,0,0,0] , [0,0,0,0,0,0,-10] , [0,0,0,0,0,0,0]]
##########################
def throw(is_air,bankai,prev_base1):
	if is_air:
		if bankai :
			return ['bankai/attack p' , [2,2,2] , [0,0,0] , [0,0,0] ,[0,0,0]]
		else:
			return ['throw' , [0,1,0] , [0,1,0] , [0,1,0] ,[0,1,0]]
	else:
		if bankai :
			return ['bankai/attack p' , [2,2,2,2,2] , [0,0,0,0,0] , [prev_base1,prev_base1,M_H,F_H,0] , [0,-J_S,-R_S,-R_S,-J_S]]
		else:
			return ['throw air' , [0,0,3,3,3] , [0,0,0,0,0] , [prev_base1,prev_base1,M_H,F_H,0] , [0,-J_S,-R_S,-R_S,-J_S]] 
#########################

def trajectoire(cur_key1,cur_key2,y2,live_val2,index) :        #decide comment dit se deplacer l'image de celui qui se fait damage par le joueur courant
	if live_val2:                   #on affiche pas la derniere image de fall(a genoux)si fin
		n = -1
	else: 
		n=-2
	if cur_key2 == 18 :                       ## on suppose que le 1 a attaque le 2
		type_damage_index = 1
	elif cur_key2 == 19 :
		type_damage_index = 3
	elif cur_key2 == 20 :
		type_damage_index = 5
	else :
		type_damage_index = 5

	weak_attack = [['damage' , [type_damage_index,type_damage_index] , [1,1] ,[0,0] , [-W_S,0]] , cur_key2]						#23 
	weak_attack_crouch_g = [['damage' , [type_damage_index,type_damage_index] , [1,1] ,[RUN_BACK_HIGHT,0] , [-2*W_S,0]] , cur_key2]		#24
	weak_attack_crouch_p = [['damage' , [type_damage_index,type_damage_index] , [1,1] ,[0,0] , [0,0]] , cur_key2]					#25
	weak_attack_air_g = [['fall down 2',[0,0]  , [1,1] ,[y2 + 2 * RUN_BACK_HIGHT,0] , [-W_S,0]],cur_key2]	#26
	weak_attack_air_p = [['fall down 2',[0,0]  , [1,1] ,[y2 + 2 * RUN_BACK_HIGHT,0] , [-W_S,0]],cur_key2]		#27
	weak_at_pied_air = [['fall down 2',[0,0]  , [1,1] ,[y2 + 2 * RUN_BACK_HIGHT,0] , [-W_S,0]],cur_key2]	#28
	strong_attack_g = [['fall down 2',[0,0,0,0]  , [1,1,1,1] ,[F_H, M_H ,F_H , 0] , [-2*W_S,-2*W_S,-2*W_S,-2*W_S]],cur_key2]	#29
	strong_attack_p = [['fall down 2',[0,0,0,0]  , [1,1,1,1] ,[F_H, M_H ,F_H , 0] , [-2*W_S,-W_S,-2*W_S,-W_S]],cur_key2]					#30
	strong_attack_crouch_g = [['fall down 2',[0,1,2,3,4,5,6,0][:n]  , [1,1,1,1,1,1,1,1][:n] ,[RUN_BACK_HIGHT, RUN_BACK_HIGHT ,RUN_BACK_HIGHT , 0,0,-20,0,0][:n] , [-2*W_S,-W_S,-W_S,0,0,0,0,0][:n]],22]	#31
	strong_attack_crouch_p = [['fall down 2',[0,1,2,3,4,5,6,0][:n]  , [1,1,1,1,1,1,1,1][:n] ,[RUN_BACK_HIGHT, RUN_BACK_HIGHT ,0 , 0,0,-20,0,0][:n] , [-W_S,-W_S,0,0,0,0,0,0][:n]],22]	#32
	strong_attack_air_g = [['fall down 2',[0,0]  , [1,1] ,[y2 + 2 * RUN_BACK_HIGHT,0] , [-3 * W_S,0]],cur_key2]	#33
	strong_attack_air_p = [['fall down 2',[0,0]  , [1,1] ,[y2 +  RUN_BACK_HIGHT,0] , [-2 * W_S,0]],cur_key2]	#34
	strongest_attack_g = [['fall down 1',[0,0,0,1,2,3,4,0][:n]  , [1,1,1,1,1,1,1,1][:n] ,[F_H, M_H , M_H + 2* RUN_BACK_HIGHT ,M_H,F_H,-20,0,0][:n] , [-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,0][:n]],21]		#35
	strongest_attack_p = [['fall down 1',[0,0,0,1,2,3,4,0][:n]  , [1,1,1,1,1,1,1,1][:n] ,[F_H, M_H , M_H + RUN_BACK_HIGHT ,M_H,F_H,-20,0,0][:n] , [-J_S,-J_S,-W_S,-W_S,-W_S,-J_S,-J_S,0][:n]],21]	#36
	strongest_a_crouch_g =[['fall down 1',[0,0,0,0,1,2,3,4,0][:n]  , [1,1,1,1,1,1,1,1,1][:n] ,[F_H, M_H ,F_H + M_H , HEIGH ,M_H,F_H,-20,0,0][:n] , [0,0,0,0,0,0,0,0,0][:n]],21]		#37		DOIT SE FAIRE LE JOUER ETANT DEBOUT de mem strongest_a_crouch_p (38)
	strongest_a_crouch_p = [['fall down 1',[0,0,0,1,2,3,4,0][:n]  , [1,1,1,1,1,1,1,1][:n] ,[F_H, M_H , M_H + F_H ,M_H,F_H,-20,0,0][:n] , [0,0,0,0,0,0,0,0][:n]],21]	#38
	r = min(1,int(round(M_H/(y2+1))))
	strongest_a_air_g = [['fall down 1',[0,0,0,0,0,0,0,1,2,3,4,0][r:n]  , [1,1,1,1,1,1,1,1,1,1,1,1][r:n] ,[M_H,0,0,F_H,M_H,M_H+F_H,M_H+F_H,M_H,F_H,-20,0,0][r:n] , [0,0,0,0,0,0,0,0,0,0,0,0][r:n]],21]
	strongest_a_air_p = [['fall down 1',[0,0,0,0,0,0,0,1,2,3,4,0][r:n]  , [1,1,1,1,1,1,1,1,1,1,1,1][r:n] ,[M_H,0,0,F_H,M_H,M_H+F_H,M_H+F_H,M_H,F_H,-20,0,0][r:n] , [0,0,0,0,0,0,0,0,0,0,0,0][r:n]],21]	#40
	throw = [['fall down 2' , [0,0,0,0,0,0,0,0 ,0,0,1,2,3,4,5,5,5,6,6] ,  [0,0,0,0,0,0,0,0 ,0,0,0,0,0,0,0,0,0,0,0] , [0,0,0,0,0,0,0,0 ,0,0,0,0,0,0,-20,-20,-20,0,0] ,[0,R_S,0,0,0,0,0,0 ,-R_S,-R_S,-R_S,-R_S,-R_S,-R_S,-R_S,0,0,0,0]],22]	#41
	throw_miss = [['throw miss' , [0,1,1,1,2] , [0,0,0,0,0,0] ,[0,0,0,0,0,0]]]		#42
	throw_air= [['fall down 1' , [0,0,0,0,0,0,1,2,3,3,3,4,0][:n] , [0,0,0,0,0,0,0,0,0,0,0,0,0][:n] , [y2,y2,y2,y2,y2,y2,M_H,F_H,0,-20,-20,0,0][:n] , [0,0,0,0,0,J_S,R_S,R_S,R_S,0,0,0,0][:n]],21]	#43
	throw_a_miss=[['throw air miss' , [0,1,2,0,0,0,0,0,0,0][:n] ,  0 , 0]]	#44
	special_a_g=[['fall down 1',[0,0,0,1,2,3,4,0][:n]  , [1,1,1,1,1,1,1,1][:n] ,[F_H, M_H , M_H + 2* RUN_BACK_HIGHT ,M_H,F_H,-20,0,0][:n] , [-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,0][:n]],21]		#45
	special_a_p=[['fall down 1',[0,0,0,1,2,3,4,0][:n]  , [1,1,1,1,1,1,1,1][:n] ,[F_H, M_H , M_H + RUN_BACK_HIGHT ,M_H,F_H,-20,0,0][:n] , [-J_S,-J_S,-W_S,-W_S,-W_S,-J_S,-J_S,0][:n]],21]		#46
	special_d = [['fall down 1',[0,0,0,1,2,3,4,0][:n]  , [1,1,1,1,1,1,1,1][:n] ,[F_H, M_H , M_H + 2* RUN_BACK_HIGHT ,M_H,F_H,-20,0,0][:n] , [-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,0][:n]],21]	 #47
	special_b_g = [['fall down 1' , [0,0,0,0,0,0,1,2,2,3,4,0][:n] , [1,1,1,1,1,1,1,1,1,1,1,1][:n] , [F_H,M_H,M_H+F_H,HEIGH,HEIGH+RUN_BACK_HIGHT,HEIGH,M_H+F_H,M_H,0,-20,0,0][:n], [0,0,0,0,0,0,0,0,0,0,0,0][:n]],21]	#48
	special_b_p = [['fall down 1' , [0,0,0,0,1,2,2,3,4,0][:n] ,[1,1,1,1,1,1,1,1,1,1][:n] , [F_H,M_H,M_H+F_H,M_H,F_H,0,-20,0,0,0][:n],[0,0,0,0,0,0,0,0,0,0][:n]],21]		#49
	super_a = [['fall down 2',[0,1,2,3,4,5,5,6,0][:n]  , [1,1,1,1,1,1,1,1,1][:n] ,[0,0 ,0 , 0,0,0,-20,0,0][:n] , [-R_S,-R_S,-R_S,-R_S,-R_S,-R_S,0,0,0][:n]],22]		#50
	r = int(round (y2/F_H))
	super_b = [['fall down 1', [0,0,0,0,0,1,2,2,3,4,0][r:n],[1,1,1,1,1,1,1,1,1,1,1][r:n],[F_H,M_H,F_H+M_H,HEIGH,HEIGH,F_H+M_H,M_H,F_H,0,-20,0][r:n],[-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,0][r:n]],21]		#51
	special_e_g = [['fall down 2',[0,0,0,0]  , [1,1,1,1] ,[RUN_BACK_HIGHT, RUN_BACK_HIGHT ,RUN_BACK_HIGHT , 0] , [-W_S,-W_S,-W_S,-W_S]],cur_key2]                                                    #52
	special_c_g = [['fall down 1',[0,0,0,1,2,3,4,0][:n]  , [1,1,1,1,1,0,0,1][:n] ,[F_H, M_H , M_H + 2* RUN_BACK_HIGHT ,M_H,F_H,-20,0,0][:n] , [-J_S,-W_S,-W_S,-W_S,-W_S,0,0,0][:n]],21]                #53
	special_c_p = [['fall down 1',[0,0,0,1,2,3,4,0][:n]  , [1,1,1,1,1,0,0,1][:n] ,[F_H, M_H , M_H + 2* RUN_BACK_HIGHT ,M_H,F_H,-20,0,0][:n] , [-J_S,-W_S,-W_S,-W_S,-W_S,0,0,0][:n]],21]                  #54
	
	actions = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 ,0 , 0 , 0 , 0 , 0 , 0 , 0 , 0
	           , weak_attack ,  weak_attack_crouch_g , weak_attack_crouch_p ,weak_attack_air_g , weak_attack_air_p, weak_at_pied_air, strong_attack_g, strong_attack_p, strong_attack_crouch_g, strong_attack_crouch_p , strong_attack_air_g ,strong_attack_air_p,strongest_attack_g,strongest_attack_p ,strongest_a_crouch_g ,strongest_a_crouch_p,strongest_a_air_g 
	           , strongest_a_air_p , throw, throw_miss, throw_air, throw_a_miss, special_a_g,special_a_p, special_d, special_b_g, special_b_p,super_a, super_b, special_e_g,special_c_g,special_c_p]
	
	
	
	return actions[cur_key1]
	

#########################

def breaks() :
	return [(0,[0]),(0,[0]),(2,[4]),(1,[1]),(2,[2]),(2,[2]),(3,[2]),(2,[2]),(-1,[2]),(1,[2]),(1,[1]),(3,[3]),(3,[2]),(3,[2]),(-1,[2]),(-1,[2]),(2,[2]),(1,[1]),(0,[3]),(0,[2])               #0 a 19
	        ,(0,[1]),(-1,[3]),(-1,[2]),(-1,[2]),(-1,[1]),(-1,[10]),(-1,[3]),(-1,[10]),(-1,[10]),(-1,[2]),(-1,[2]),(-1,[1]),(-1,[1]),(-1,[3]),(-1,[3]),(-1,[2,1]),(-1,[2,1]),(-1,[1]),(-1,[1]),(-1,[3])          #20 a 39
	        ,(-1,[3]),(0,[2]), (-1,[2]), (0,[3]), (-1,[3]),(-1,[2,1]),(-1,[2,1]),(-1,[2,1]),(-1,[2,1]),(-1,[2,1]),(-1,[[2,1],1]),(-1,[[2,1],1]),(-1,[2]),(-1,[1,2]),(-1,[1,2]),(-1,[10])] 		
				#(a,b) contient a=on peut break? (0 peut pas break(damages) , -1 =seulement les damages peuvent break ; 1 break crouch ,2 break stand
				# 3 break air) , b = il peut break qui? et pareil avec a
				# mais ici 0 c pour les damages car ca break tout et 4 il ne break persone
				#pour les supper il fo le maxi dc le b est un tableux [il peut break , maxi minimal]
				#b = [10] pour que ca ne puisse pas s'executer 
def breaks_bankai() :
	return [(0,[0]),(0,[0]),(2,[4]),(1,[10]),(2,[2]),(2,[2]),(3,[2]),(2,[2]),(-1,[2]),(1,[2]),(1,[10]),(3,[3]),(3,[2]),(3,[2]),(-1,[2]),(-1,[2]),(2,[2]),(1,[1]),(0,[3]),(0,[2])               #0 a 19
	        ,(0,[1]),(-1,[3]),(-1,[2]),(-1,[20]),(-1,[10]),(-1,[10]),(-1,[30]),(-1,[10]),(-1,[10]),(-1,[2]),(-1,[2]),(-1,[1]),(-1,[1]),(-1,[3]),(-1,[3]),(-1,[10]),(-1,[10]),(-1,[10]),(-1,[10]),(-1,[30])          #20 a 39
	        ,(-1,[30]),(0,[2]), (-1,[2]), (0,[3]), (-1,[3]),(-1,[2,1]),(-1,[2,1]),(-1,[10]),(-1,[10]),(-1,[10]),(-1,[[10],1]),(-1,[[10],1]),(-1,[20]),(-1,[10]),(-1,[10]),(-1,[0])] 
##########################


#########################

def descendre(key , y , bankai) :		#key est l'action selon laquelle on descent (jump ,forwrd jump ...) ; y est la hauteur courante
	if y <= 0 :		#pour que ca aille a stance
		return [0,0,2]		# 2 pour stance
	else :
		if y > HEIGH :
			y = HEIGH
		act = clavier(key,key,0,0,bankai)
		i = -1
		n = act[3][i]
		while y > n :
			i -= 1
			n = act[3][i]
		if i== -1:
			i = -2                   # c pour le bankai il ne fini pas le saut a y == 0
		return [1, len(act[3])+i+1 , key]

####################################

def scale (heigh, s, k) :
	if s == 'super move a g' :
		if k == 11 :
			return heigh/194
		else :
			return 1
	if s == 'bankai/special move a g' :
		if k == 9 :
			return heigh/194
		else :
			return 1
	if s == 'bankai/special move a p' :
		if k == 8 :
			return heigh/194
		else :
			return 1
	else :
		return 1

####################################

def puissance(key,puissance,x,y,bankai) :
	if bankai :
		if key == 29 :
			attack_g = ['bankai/attack g', [8,8,8,8,8,8,8,8,8,8], [5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK], [F_H,F_H,F_H,F_H,F_H,F_H,F_H,F_H,F_H,F_H], [0,R_S,int(1.8*R_S),int(1.8*R_S),int(1.8*R_S),int(1.8*R_S),int(1.8*R_S),int(1.8*R_S),int(1.5*R_S),int(1.5*R_S)]]
			return [1 , {'data':attack_g , 'index':-1 , 'start':3 , 'end':12 , 'type': 1 , 'key': 29}]
		elif key == 30 :
			attack_p = ['bankai/attack p', [3,3,3,3,3,3,3,3,3,3], [5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK], [F_H,F_H,F_H,F_H,F_H,F_H,F_H,F_H,F_H,F_H], [0,int(R_S/2),R_S,R_S,R_S,R_S,R_S,R_S,R_S,R_S]]
			return [1 , {'data':attack_p , 'index':-1 , 'start':3 , 'end':12 , 'type': 1, 'key': 30}]
		elif key == 33 :
			attack_air_g = ['bankai/attack air g', [8,8,8], [5*WEAK,5*WEAK,5*WEAK], [M_H,F_H,0], [R_S,int(1.5*R_S),int(1.5*R_S)]]
			return [1 , {'data':attack_air_g , 'index':-1 , 'start':2 , 'end':4 , 'type': 1 , 'key': 33}]
		elif key == 34 :
			attack_air_p = ['bankai/attack air p', [2,2,2], [5*WEAK,5*WEAK,5*WEAK], [M_H,F_H,0], [R_S,R_S,R_S]]
			return [1 , {'data':attack_air_p , 'index':-1 , 'start':2 , 'end':4 , 'type': 1 , 'key': 34}]
		elif key == 45 :
			special_a_g = ['bankai/special move a g', [9,9,9,9,9,9,9,9,9,9], [5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK], [0,0,0,0,0,0,0,0,0,0], [0,R_S,R_S,int(1.5*R_S),int(1.5*R_S),int(1.5*R_S),int(1.5*R_S),int(1.5*R_S),int(1.5*R_S),int(1.5*R_S)]]
			return [1 , {'data':special_a_g , 'index':-1 , 'start':6 , 'end':15 , 'type': 2 , 'key': 45}]
		elif key == 46 :
			special_a_p = ['bankai/special move a p', [8,8,8,8,8,8,8,8,8,8], [5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK], [0,0,0,0,0,0,0,0,0,0], [0,int(R_S/2),R_S,R_S,R_S,R_S,R_S,R_S,R_S,R_S]]
			return [1 , {'data':special_a_p , 'index':-1 , 'start':6 , 'end':15, 'type': 2 , 'key': 46}]
		else :
			return [1,{}]
	else :		
		if key == 45 :
			special_a_g = ['special move a g', [8,9,10,10,10,10,10,10,10,10], [5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK], [0,0,0,0,0,0,0,0,0,0], [0,R_S,R_S,int(1.5*R_S),int(1.5*R_S),int(1.5*R_S),int(1.5*R_S),int(1.5*R_S),int(1.5*R_S),int(1.5*R_S)]]
			return [1 , {'data':special_a_g , 'index':-1 , 'start':3 , 'end':12 , 'type': 1 , 'key': 45}]
		elif key == 46 :
			special_a_p = ['special move a p', [8,9,10,10,10,10,10,10,10,10], [5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK], [0,0,0,0,0,0,0,0,0,0], [0,int(R_S/2),R_S,R_S,R_S,R_S,R_S,R_S,R_S,R_S]]
			return [1 , {'data':special_a_p , 'index':-1 , 'start':3 , 'end':12 , 'type': 1, 'key': 46}]
		elif key == 47 :
			special_d = ['special move d', [6,7,8,9,10,10,10,10,10,10], [5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK,5*WEAK], [0,0,0,0,0,0,0,0,0,0], [0,int(R_S/2),R_S,2*R_S,2*R_S,2*R_S,2*R_S,2*R_S,2*R_S,2*R_S]]
			return [1 , {'data':special_d , 'index':-1 , 'start':3 , 'end':12 , 'type': 2, 'key': 47}]
		elif key == 50 :
			super_a_g = ['super move a g', [11,11,11,11,11,11,11,11,11,11], [8*WEAK,8*WEAK,8*WEAK,8*WEAK,8*WEAK,8*WEAK,8*WEAK,8*WEAK,8*WEAK,8*WEAK], [0,0,0,0,0,0,0,0,0,0], [0,0,2*R_S,2*R_S,2*R_S,2*R_S,2*R_S,2*R_S,2*R_S,2*R_S]]
			return [1 , {'data':super_a_g , 'index':-1 , 'start':5 , 'end':14 , 'type': 2, 'key': 50}]
		elif key == 52 :
			special_e_g = ['special move e g', [9,10], [3*WEAK,3*WEAK], [M_H,F_H], [100,2*R_S]]
			return [1 , {'data':special_e_g , 'index':-1 , 'start':4 , 'end':5 , 'type': 1, 'key': 52}]
		else :
			return [1,{}]
####################################

def bankai(key,bankai,x,y) :
	if key == 51:
		return [1,{'type' : 2,'count':100},1,int(round(1.5))]
	else :
		return [1,{},1,1]
####################################
####################################

def super(key,max_num) :
	if key == 50  :
		return [max_num - 1 , 1]             # -1 car on use 1 maxi pour executer ca ; si on modifie ds breaks fo aussi modifier ici
	elif key == 51:
		return [max_num - 3 , 2]
	else:
		return [max_num , 0]                   # n'ont pas besoin de maxi pour s'executer
####################################
####################################

def computer(act_type,num_maxs,bankai) :
	if act_type :
		if bankai:
			return [29,30,31,32,33,34,45,46]
		else:
			if num_maxs >= 3:
				return [23,24,26] + range(41)[29:] + [42,44,45,46,47,48,49,50,51,52,53,54]
			if num_maxs >= 1:
				return [23,24,26] + range(41)[29:] + [42,44,45,46,47,48,49,50,52,53,54]
			else :
				return [23,24,26] + range(41)[29:]+[42,44,45,46,47,48,49,52,53,54]
	else :
		return [4,5,6,7,8,9]+[11,12,13,14,15,15]
####################################

def personality() :
	return random.choice([1,0,0,0,1,1,1,0,1,0,1,1,1])

def ds():
	ichi = { 'intro' : [[0, 60,93]  , [0, 69,129]  , [0, 90,141] ],  'win' : [[0, 90,141]  , [0, 69,129]  , [0, 60,93] ],  'taunt' : [[0, 90,141]  , [0, 69,129]  , [0, 60,93]  , [0, 69,129]  , [0, 90,141] ]  , 'stance' : [[0, 82,109]  , [0, 82,109]  , [0, 82,108]  , [0, 82,107]  , [0, 83,107]  , [0, 83,107]  , [0, 82,107]  , [0, 83,108]  , [0, 82,109] ],  'turn' : [[0, 62,106]  , [0, 62,106] ]  ,  'walk' : [[0, 79,106]  , [0, 77,104]  , [0, 73,105]  , [0, 75,106]  , [0, 77,105]  , [0, 77,106]  , [0, 81,107]  , [0, 72,107] ],  'crouch' : [[0, 82,92]  , [0, 80,68] ],  'crouch turn' : [[0, 58,77]  , [0, 58,77] ] , 'run' : [[0, 82,90]  , [0, 80,88]  , [0, 80,80]  , [0, 84,82]  , [0, 82,82]  , [0, 83,82] ],  'air dash' : [[0, 60,87]  , [0, 84,82] ]  ,'jump' : [[0, 82,92]  , [0, 55,123]  , [0, 60,87]  , [0, 55,123]  , [0, 82,92] ],  'forward jump' : [[0, 82,92]  , [0, 79,114]  , [0, 60,87]  , [0, 65,106]  , [0, 82,92] ] ,'teleport' : [[0,82,108],[0,84,108],[0,84,107]] , 'guard' : [[0,89,88],[0,81,64]] ,'damage' : [[0, 65,111]  , [0, 65,111]  , [0, 76,98]  , [0, 69,112]  , [0, 68,100]  , [0, 54,98]  , [0, 76,88] ] , 'fall down 1' : [[0, 122,92]  , [0, 105,85]  , [0, 126,45]  , [0, 135,25]  , [0, 70,67] ] , 'fall down 2' : [[0, 119,44]  , [0, 69,112]  , [0, 68,100]  , [0, 103,82]  , [0, 126,45]  , [0, 126,45]  , [0, 135,25]  , [0, 70,67] ] , 'weak attack' : [[0, 84,83]  , [0, 96,79]  , [0, 84,83] ],  'weak attack crouch' : [[0, 58,91]  , [0, 90,85]  , [0, 90,85]  , [0, 58,91] ],  'weak attack air' : [[0, 78,100]  , [0, 94,110]  , [0, 94,110]  , [0, 78,100] ] , 'strong attack g' : [[0, 84,83]  , [0, 100,83]  , [0, 143,79]  , [0, 144,95]  , [0, 97,96]  , [0, 83,96]  , [0, 83,95]  , [0, 83,93]  , [0, 77,92] ] , 'strong attack p' : [[0, 84,83]  , [0, 143,79]  , [0, 83,93]  , [0, 77,92] ]  , 'strong attack crouch g' : [[0, 92,58]  , [0, 158,56]  , [0, 158,56]  , [0, 158,56]  , [0, 92,58] ],  'strong attack crouch p' : [[0, 92,58]  , [0, 158,56]  , [0, 92,58] ] , 'strong attack air g' : [[0, 86,66]  , [0, 163,76]  , [0, 141,75]  , [0, 146,119]  , [0, 102,119]  , [0, 102,115]  , [0, 102,100] ] , 'strong attack air p' : [[0, 86,66]  , [0, 139,69]  , [0, 102,100] ] , 'strongest attack g' : [[0, 79,102]  , [0, 80,102]  , [0, 79,102]  , [0, 130,164]  , [0, 112,164]  , [0, 137,157]  , [0, 137,85]  , [0, 137,67]  , [0, 131,67]  , [0, 120,75] ] , 'strongest attack p' : [[0, 79,102]  , [0, 80,102]  , [0, 79,102]  , [0, 97,140]  , [0, 131,67]  , [0, 120,75] ] , 'strongest attack crouch g' : [[0, 108,59]  , [0, 89,58]  , [0, 64,74]  , [0, 128,95]  , [0, 128,153]  , [0, 118,153]  , [0, 60,153]  , [0, 60,153]  , [0, 128,95] ] , 'strongest attack crouch p' : [[0, 108,59]  , [0, 89,58]  , [0, 64,74]  , [0, 128,95]  , [0, 60,153]  , [0, 60,153]  , [0, 60,153]  , [0, 128,95] ] , 'strongest attack air g' : [[0, 84,92]  , [0, 139,168]  , [0, 135,168]  , [0, 119,168]  , [0, 119,139]  , [0, 117,77]  , [0, 110,76]  , [0, 98,76] ] , 'strongest attack air p' : [[0, 84,92]  , [0, 98,76] ] , 'throw' : [[0, 116,80]  , [0, 88,83]  , [0, 66,87]  , [0, 93,87]  , [0, 83,67] ],  'throw miss' : [[0, 116,80]  , [0, 88,83]  , [0, 81,80] ] , 'throw air' : [[0, 95,68]  , [0, 68,72]  , [0, 60,88]  , [0, 93,86]  , [0, 83,69] ],  'throw air miss' : [[0, 95,68]  , [0, 68,72]  , [0, 72,85] ] , 'special move a g' : [[0, 62,108]  , [0, 68,117]  , [0, 83,117]  , [0, 117,88]  , [0, 104,92]  , [0, 88,92]  , [0, 67,92]  , [0, 105,80]  , [0, 30,60]  , [0, 47,107]  , [0, 63,123] ] , 'special move a p' : [[0, 62,108]  , [0, 68,117]  , [0, 83,83]  , [0, 105,80]  , [0, 67,92]  , [0, 67,91]  , [0, 67,92]  , [0, 105,80] , [0, 30,60]  , [0, 47,107]  , [0, 63,123]] , 'special move b g' : [[0, 84,83]  , [0, 91,64]  , [0, 91,64]  , [0, 89,64]  , [0, 151,63]  , [0, 159,86]  , [0, 107,86]  , [0, 107,83]  , [0, 107,75]  , [0, 107,75] ] , 'special move b p' : [[0, 84,83]  , [0, 91,64]  , [0, 72,64]  , [0, 87,64]  , [0, 151,63]  , [0, 107,75]  , [0, 107,75]  , [0, 107,75] ] , 'special move c g' : [[0, 108,59]  , [0, 89,58]  , [0, 64,74]  , [0, 128,95]  , [0, 124,154]  , [0, 115,154]  , [0, 57,154]  , [0, 57,154] , [0, 84,92]  , [0, 139,168]  , [0, 135,168]  , [0, 119,168]  , [0, 119,139] ] , 'special move c p' : [[0, 108,59]  , [0, 89,58]  , [0, 64,74]  , [0, 128,95]  , [0, 57,154]  , [0, 57,154]  , [0, 57,154]  , [0, 84,92]  , [0, 98,76] ] , 'special move d' : [[0, 89,86]  , [0, 61,108]  , [0, 65,83]  , [0, 65,95]  , [0, 61,108]  , [0, 89,86]  , [0, 45,181]  , [0, 60,183]  , [0, 120,190]  , [0, 172,192]  , [0, 180,192] ] , 'special move e g' : [[0, 108,59]  , [0, 89,58]  , [0, 64,74]  , [0, 128,95]  , [0, 128,153]  , [0, 118,153]  , [0, 60,153]  , [0, 60,153]  , [0, 128,95]  , [0, 54,81]  , [0, 65,79] ] , 'special move e p' : [[0, 108,59]  , [0, 89,58]  , [0, 64,74]  , [0, 128,95]  , [0, 60,153]  , [0, 60,153]  , [0, 60,153]  , [0, 128,95] ] , 'super move a g' : [[0, 60,172]  , [0, 63,166]  , [0, 61,158]  , [0, 72,142]  , [0, 114,142]  , [0, 145,137]  , [0, 145,101]  , [0, 142,62]  , [0, 135,62]  , [0, 92,58]  , [0, 82,92] , [0, 63,123]] , 'super move a p' : [[0, 60,172]  , [0, 63,166]  , [0, 61,158]  , [0, 72,142]  , [0, 114,121]  , [0, 136,61]  , [0, 136,60]  , [0, 135,62]  , [0, 92,58]  , [0, 82,92]  , [0, 63,123] ]  ,'super move b' : [[0, 78,111]  , [0, 78,112]  , [0, 74,108]  , [0, 110,78]  , [0, 108,77]  , [0, 108,79]  , [0, 108,78]  , [0, 108,78]  ,  [0, 71,94]  , [0, 95,80]  , [0, 144,86]  , [0, 151,79]  , [0, 144,79]  , [0, 152,79]  , [0, 76,91] ] , 'bankai/stance' : [[0, 90,92] ],  'bankai/air dash' : [[0, 112,74] ],  'bankai/jump' : [[0, 78,97] ],  'bankai/forward jump' : [[0, 112,85]  , [0, 78,97]  , [0, 86,85] ],  'bankai/teleport' : [[0, 87,94] ] , 'bankai/attack g' : [[0, 81,78]  , [0, 97,78]  , [0, 145,79]  , [0, 146,95]  , [0, 103,96]  , [0, 79,96]  , [0, 79,95]  , [0, 79,94]  , [0, 189,52] ] , 'bankai/attack p' : [[0, 81,78]  , [0, 140,79]  , [0, 79,94] , [0, 189,52] ] , 'bankai/attack crouch g' : [[0, 95,58]  , [0, 166,56]  , [0, 166,56]  , [0, 158,56]  , [0, 95,58] ],  'bankai/attack crouch p' : [[0, 95,58]  , [0, 158,56]  , [0, 95,58] ] , 'bankai/attack air g' : [[0, 85,84]  , [0, 139,168]  , [0, 135,168]  , [0, 119,168]  , [0, 119,139]  , [0, 117,77]  , [0, 110,76]  , [0, 98,76]   , [0, 147,122] ] , 'bankai/attack air p' : [[0, 85,84]  , [0, 98,76] , [0, 147,122] ],  'bankai/special move a g' : [[0, 60,124]  , [0, 56,168]  , [0, 62,155]  , [0, 78,138]  , [0, 123,142]  , [0, 147,137]  , [0, 148,101]  , [0, 146,60]  , [0, 134,59]  , [0, 63,123] ] , 'bankai/special move a p' : [[0, 60,124]  , [0, 56,168]  , [0, 62,155]  , [0, 78,138]  , [0, 122,118]  , [0, 132,60]  , [0, 132,59]  , [0, 134,59] ,[0, 63,123]] , 'bankai/transform back' : [[0, 78,111]  , [0, 78,112]  , [0, 74,108]  , [0, 110,78]  , [0, 108,77]  , [0, 108,79]  , [0, 108,78]  , [0, 108,78] ] }
	return ichi