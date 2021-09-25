import random
XCONST = 1.5
YCONST = 1.3
R_S = int(round (60 * XCONST))		#RUN_SPEED
W_S = int(round (20 * XCONST))		#WALK_SPEED
AVER_PROF = 10		#AVERAGE PROFONDEUR
M_H = int(round (150 * YCONST))		#MID_HEIGH
HEIGH = int(round (300 * YCONST))
F_H = int(round (75 * YCONST))		#FOURTH_HEIGHT
J_S = int(round (40 * XCONST))		#JUMP_SPEED
RUN_BACK_HIGHT = int(round (30 * YCONST))
WEAK = 4		#profondeur unite 
JUMP_LENGHT = 12		#nombre d'images de jump... ici c 7 images 0.png ... 6.png utilise pour weak attack air

def ymax():
	return int(round (HEIGH / YCONST))

def clavier(input_,cur_key,index,prev_base,bankai) :  		# input est un entier correspondant a la sequence du clavier : ex : walk avant c'est 4
				#format : [nom ds dico,[sequence d'affichage],[profondeurs],[y(qd ca monte),vitesse(augmentation de x)
				# profondeur 0 veut dire intouchable . exemple teleport 
	h = HEIGH-prev_base
	index %=  JUMP_LENGHT	# pour les cas ou clavier est call pour autre chose index > jump_lenght et a air_dash il y aurait depasse index 
	intro = ['intro',[0,1,0,1,2,3],[1,1,1,1,1,1],[0,0,0,0,0,0],[0,0,0,0,0,0]]				#0 
	win = ['win' , [0,1,2,3,4,5,3,4,5],[1,1,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]		#1
	stance = ['stance' , [0,1,2,3,4,5,6,7],[1,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]		#2
	turn = ['turn',[0,1],[1,1],[0,0],[0,0]]							#3
	walk_avant = ['walk',[0,1,2,3,4,5],[1,1,1,1,1,1],[0,0,0,0,0,0],[W_S,W_S,W_S,W_S,W_S,W_S]]		#4
	walk_back = ['walk' , [5,4,3,2,1,0],[1,1,1,1,1,1],[0,0,0,0,0,0],[-W_S,-W_S,-W_S,-W_S,-W_S,-W_S]]		#5
	jump = ['jump' , [0,1,2,2,2,3,3,4,4,4,5,6],[1,-1,1,1,1,1,1,1,1,1,1,-1],[0,0,F_H,M_H,F_H+M_H,HEIGH,HEIGH,F_H+M_H,M_H,F_H,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]	#6	
	run_avant = ['run',[0,1,2,3],[1,1,1,1],[0,0,0,0],[R_S,R_S,R_S,R_S]]								#7
	run_back = ['stance',[3,3,1],[1,1,1],[RUN_BACK_HIGHT,RUN_BACK_HIGHT,RUN_BACK_HIGHT],[-R_S,-R_S,-R_S]]			#8
	crouch = ['crouch' , [0,1],[-1,-1],[0,0],[0,0]]			#-1 pour crouch 1 pour ni bloque ni attack ; attack est - ou +2			#9
	crouch_turn = ['crouch turn' , [0,1],[-1,-1],[0,0],[0,0]]											#10
	air_dash = ['air dash' , [0,1],[1,1],[prev_base ,prev_base],[J_S,J_S]]	# le y est celui de la prchaine image de jump  		#11
	forward_jump = ['forward jump' , [0,1,2,2,2,3,3,4,4,4,5,6],[1,-1,1,1,1,1,1,1,1,1,1,-1],[0,0,F_H,M_H,F_H+M_H,HEIGH,HEIGH,F_H+M_H,M_H,F_H,0,0],[J_S,J_S,J_S,J_S,J_S,J_S,J_S,J_S,J_S,J_S,J_S,J_S]]	#12
	backward_jump = ['jump' ,  [0,1,2,2,2,3,3,4,4,4,5,6],[1,-1,1,1,1,1,1,1,1,1,1,-1],[0,0,F_H,M_H,F_H+M_H,HEIGH,HEIGH,F_H+M_H,M_H,F_H,0,0],[-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,-J_S]]		#13
	teleport_avant = ['teleport' , [0,1,2,1] , [1,0,0,0] , [0,0,0,0] , [R_S,R_S,R_S,R_S]]								#14
	teleport_back = ['teleport' , [0,1,2,1] , [1,0,0,0] , [0,0,0,0] , [-R_S,-R_S,-R_S,-R_S]]							#15	
	up_guard = ['guard' , [0,0,0,0,0,0] , [1,1,1,1,1,1] , [0,0,0,0,0,0] ,[0,0,0,0,0,0]]	#mm nbre d'elts que walk back           		#16
	down_guard = ['guard' , [1,1] , [-1,-1] , [0,0] ,[0,0]]				#mm nbre d'elts que crouch					#17
	damage_upup = ['damage' , [0,1] , [1,1] ,[max(prev_base-RUN_BACK_HIGHT,0),max(prev_base-RUN_BACK_HIGHT , 0)] , [-2*W_S,0]]			#18
	damage_updown = ['damage' , [2,3] , [1,1] ,[prev_base,prev_base] , [-2*W_S,0]] 									#19
	damage_down = ['damage' , [4,5] , [-1,-1] ,[prev_base,prev_base] , [-2*W_S,0]]									#20
	fall1 = ['fall down 1' , [0,1,2,3,4] ,[0,0,0,0,0] , [M_H,M_H,F_H,-10,0] , [0,0,0,0,0]]					#21 
	fall2 = ['fall down 2' , [0,1,2,3,4,5,6] ,[0,0,0,0,0,0,0] , [0,0,0,0,0,-10,0] , [0,0,0,0,0,0,0]]						#22
	weak_attack = ['weak attack' ,[0,1,2,3,4] , [1,1,2*WEAK,1.5*WEAK,1] , [0,0,0,0,0] , [-1,-1,-1,-1,-1]]						#23 
	weak_attack_crouch_g = ['weak attack crouch g' ,[0,1,2,3,4,5] , [-1,-1,-2*WEAK,-1.5*WEAK,-WEAK,-1] , [0,0,0,0,0,0] , [-1,-1,-1,-1,-1,-1]]		#24
	weak_attack_crouch_p = ['weak attack crouch p' ,[0,1,2,3] , [-1,-WEAK,-1.5*WEAK,-1] , [0,0,0,0] , [-1,-1,-1,-1]]					#25

	####@@ pour l'air
	if cur_key == 6 :		#jump
		prevact = jump
	elif cur_key == 12 : 		#forward jump
		prevact = forward_jump
	elif cur_key == 13 :		#backward jump 
		prevact = backward_jump
	else :
		[bl,index,cur_key] = descendre(12 , prev_base,bankai)
		prevact = forward_jump
		if index > 0 :
			index -= 1                    #car en bas on ajoute 1
		else :
			index = JUMP_LENGHT - 2
	if index < JUMP_LENGHT - 1 :
		index += 1
	n = JUMP_LENGHT - index	# car index est ce qui devrait etre affiche si on ne breakait pas n est le nbre d'image a prendre ds weak attack air	
	#####@@@	
	weak_attack_air_g = ['weak attack air g',[0,1,2,3,4,5,5,5,5,5,5,5][:n] , [-1,-1,2*WEAK,1.5*WEAK,WEAK,-1,-1,-1,-1,-1,-1,-1][:n] , prevact[3][index:] , prevact[4][index:]]	#26
	weak_attack_air_p = ['weak attack air p',[1,2,3,3,3,3,3,3,3,3,3,3][:n] , [-1,2*WEAK,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1][:n] , prevact[3][index:] , prevact[4][index:]]		#27
	weak_at_pied_air = ['weak attack' ,[0,1,2,3,4,4,4,4,4,4,4,4][:n] , [1,1,2*WEAK,1.5*WEAK,1,1,1,1,1,1,1,1][:n] ,prevact[3][index:] , prevact[4][index:]]	#28
	strong_attack_g = ['strong attack g' , [0,1,2,3,4,5,6,7,8,9] , [1,1,1,1,2*WEAK,4*WEAK,2*WEAK,WEAK,1,1],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]	#29
	strong_attack_p = ['strong attack p' , [0,2,3,4,5,6,7] , [1,1,1,2*WEAK,3*WEAK,WEAK,1],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]					#30
	strong_attack_crouch_g = ['strong attack crouch g' ,[0,1,2,3,4,5,6] , [-1,-1,-2*WEAK,-3*WEAK,-1,-1,-1] , [0,0,0,0,0,0,0] , [-1,-1,-1,-1,-1,-1,-1]]	#31
	strong_attack_crouch_p = ['strong attack crouch p' ,[0,1,2,3,4,5,6] , [-1,-1,-2*WEAK,-3*WEAK,-1,-1,-1] , [0,0,0,0,0,0,0] , [-1,-1,-1,-1,-1,-1,-1]]	#32
	strong_attack_air_g = ['strong attack air g',[0,1,2,3,4,5,6,6,6,6,6,6][:n] , [-1,-1,3*WEAK,3*WEAK,2*WEAK,-1,-1,-1,-1,-1,-1,-1][:n] , prevact[3][index:] , prevact[4][index:]]	#33
	strong_attack_air_p = ['strong attack air p',[0,1,2,3,4,4,4,4,4,4,4,4][:n] , [-1,-1,3*WEAK,WEAK,-1,-1,-1,-1,-1,-1,-1,-1][:n] , prevact[3][index:] , prevact[4][index:]]	#34
	strongest_attack_g = ['strongest attack g' , [0,1,2,3,4,4,5,6,7,8,9,10,11] , [1,1,1,1,1,1,6*WEAK,4*WEAK,2*WEAK,WEAK,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0],[-R_S,0,0,0,R_S,R_S,2*R_S,0,0,0,0,0,0]]		#35
	strongest_attack_p = ['strongest attack p' , [0,1,2,3,4,5,6,7,8,9] , [1,1,1,1,4*WEAK,2*WEAK,WEAK,1,1,1],[0,0,0,0,0,0,0,0,0,0],[-R_S/2,0,0,0,R_S/2,R_S,0,0,0,0]]	#36
	strongest_a_crouch_g = ['strongest attack crouch g' , [0,1,2,3,4,5,6,7,8,9] , [-1,-1,-1,-1,-WEAK,-4*WEAK,-3*WEAK,-2*WEAK,-1,-1,-1],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]		#37		DOIT SE FAIRE LE JOUER ETANT DEBOUT de mem strongest_a_crouch_p (38)
	strongest_a_crouch_p = ['strongest attack crouch p' , [0,1,2,3,4,5,6,7] , [-1,-1,-1,-1,-WEAK,-3*WEAK,-2*WEAK,-WEAK,-1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]	#38
	strongest_a_air_g = ['strongest attack air g' , [0,1,2,3,4,5,6,7,8,9] , [1,1,1,1,20*WEAK,12*WEAK,8*WEAK,1,1,1],[prev_base+(h+F_H)/3,prev_base+2*(h+F_H)/3 ,F_H+HEIGH,HEIGH,M_H,F_H,0,0,0,0] ,[R_S,R_S,R_S,R_S,R_S,R_S,R_S,R_S,0,0]]	#39
	strongest_a_air_p = ['strongest attack air p' , [0,1,2,3,4,5,6,7] , [1,1,1,1,12*WEAK,8*WEAK,4*WEAK,1],[prev_base+h/3,prev_base+2*h/3 ,HEIGH+F_H/2 ,HEIGH,M_H,F_H,0,0] , [J_S,J_S,J_S,J_S,J_S,J_S,0,0]]	#40
	throw = ['throw' , [0,1,2,2,2,3,3,3] , [5*WEAK ,0,0,0,0,0,0,0] , [0,0,0,0,0,0,0,0] ,[0,0,0,0,0,R_S,R_S,R_S]]	#41
	throw_miss = ['throw miss' , [0,1,1,1,2] , [0,0,0,0,0] , [0,0,0,0,0,0] ,[0,0,0,0,0,0]]		#42
	a=prev_base #prevact[3][index]
	throw_air= ['throw air' , [0,0,1,2,2,3,3,0,0,0,0,0,0][:n+6] , [5*WEAK ,0,0,0,0,0,0,0,0,0,0,0,0][:n+6] , [a,a,a,a,a,a]+prevact[3][index:] , [0,0,0,0,0,0]+prevact[4][index:]]	#43
	throw_a_miss=['throw air miss' , [0,1,2,0,0,0,0,0,0,0,0,0][:n] , [0,0,0,0,0,0,0,0,0,0,0,0][:n] , prevact[3][index:] , prevact[4][index:]]		#44
	special_a_g=['special move a g' , [0,1,2,1,2,3,4,5,6,7,8,9,10] , [1,1,1,1,1,1,1,10*WEAK,6*WEAK,3*WEAK,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,2*R_S,2*R_S,2*R_S,2*R_S,2*R_S,R_S,0,0,0,0,0,0]]		#45
	special_a_p=['special move a p' , [0,1,2,1,2,3,4,5,6,7] , [1,1,1,1,1,1,1,8*WEAK,4*WEAK,1],[0,0,0,0,0,0,0,0,0,0],[0,2*R_S,2*R_S,2*R_S,2*R_S,2*R_S,R_S,0,0,0]]		#46
	special_b = ['special move b' , [0,1,2,0,1,2] , [1,1,1,1,1,1] , [0,0,0,0,0,0] , [0,0,0,0,0,0]]	 #47
	special_c_g = ['special move c g' , [0,1,2,3,4,5,6,5,6,7,8,9,10,11,10,11,10,11] , [1,1,1,1,1, 3*WEAK, 3*WEAK, 3*WEAK,3*WEAK, 6*WEAK, 4*WEAK, 2*WEAK, WEAK,1,1,1,1,1], [0,0,0,0,0,0,0,0,0,F_H,M_H,M_H+F_H,HEIGH,HEIGH,M_H+F_H,M_H,F_H,0], [0,0,0,0,0,2*R_S,2*R_S,2*R_S,2*R_S,R_S,R_S,R_S,R_S,W_S,W_S,W_S,W_S,0]]	#48
	special_c_p = ['special move c p' , [0,1,2,3,4,5,6,5,6,7,8,8,7,8] , [1,1,1,1,1,3*WEAK,3*WEAK,3*WEAK,3*WEAK,4*WEAK,2*WEAK,1,1,1],[0,0,0,0,0,0,0,0,0,F_H,M_H,M_H,F_H,0],[0,0,0,0,0,2*R_S,2*R_S,2*R_S,2*R_S,R_S,R_S,W_S,W_S,0]]		#49
	super_a = ['super move a', [0,1,2,3,4,5,6,7,8,14,15,16,17,18,19,20,21], [1,1,1,1,1,1,1,1,15*WEAK,10*WEAK,1,1,1,1,1,1,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]		#50
	super_b = ['super move b', [0,1,0,1,2,3,4,5,8,9,5,3,6,7,6,7], [1,1,1,1,1,1,1,10*WEAK,15*WEAK,15*WEAK,10*WEAK,1,1,1,1,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]		#51
	ken_throw = ['throw g', [0,1,2,3,4,5,6,6], [1,1,1,2*WEAK,2*WEAK,2*WEAK,1,1],[0,0,0,0,0,0,0,0],[0,0,0,1.5*R_S,1.5*R_S,1.5*R_S,0,0]]               #52


	actions = [intro , win , stance , turn , walk_avant , walk_back , jump , run_avant , run_back  , crouch , crouch_turn , air_dash  , forward_jump  , backward_jump , teleport_avant ,teleport_back ,  up_guard , down_guard , damage_upup , damage_updown 
	           , damage_down , fall1 , fall2 , weak_attack ,  weak_attack_crouch_g , weak_attack_crouch_p ,weak_attack_air_g , weak_attack_air_p, weak_at_pied_air, strong_attack_g, strong_attack_p, strong_attack_crouch_g, strong_attack_crouch_p , strong_attack_air_g ,strong_attack_air_p,strongest_attack_g,strongest_attack_p ,strongest_a_crouch_g ,strongest_a_crouch_p,strongest_a_air_g 
	           , strongest_a_air_p , throw, throw_miss, throw_air, throw_a_miss, special_a_g,special_a_p, special_b, special_c_g, special_c_p,super_a, super_b, ken_throw]
	
	return actions[input_] 

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
	special_b = [['special move b' , [0,1,2,0,1,2] ,  [0,0,0,0,0,0] , [0,0,0,0,0,0]]]	 #47
	special_c_g = [['fall down 1' , [0,0,0,0,0,0,1,2,2,3,4,0][:n] , [1,1,1,1,1,1,1,1,1,1,1,1][:n] , [F_H,M_H,M_H+F_H,HEIGH,HEIGH+RUN_BACK_HIGHT,HEIGH,M_H+F_H,M_H,0,-20,0,0][:n], [0,0,0,0,0,0,0,0,0,0,0,0][:n]],21]	#48
	special_c_p = [['fall down 1' , [0,0,0,0,1,2,2,3,4,0][:n] ,[1,1,1,1,1,1,1,1,1,1][:n] , [F_H,M_H,M_H+F_H,M_H,F_H,0,-20,0,0,0][:n],[0,0,0,0,0,0,0,0,0,0][:n]],21]		#49
	super_a = [['fall down 2',[0,1,2,3,4,5,5,6,0][:n]  , [1,1,1,1,1,1,1,1,1][:n] ,[0,0 ,0 , 0,0,0,-20,0,0][:n] , [-R_S,-R_S,-R_S,-R_S,-R_S,-R_S,0,0,0][:n]],22]		#50
	r = int(round (y2/F_H))
	super_b = [['fall down 1', [0,0,0,0,0,1,2,2,3,4,0][r:n],[1,1,1,1,1,1,1,1,1,1,1][r:n],[F_H,M_H,F_H+M_H,HEIGH,HEIGH,F_H+M_H,M_H,F_H,0,-20,0][r:n],[-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,0][r:n]],21]		#51
	ken_throw = [['fall down 2',[0,0,0,0]  , [1,1,1,1] ,[RUN_BACK_HIGHT, RUN_BACK_HIGHT ,RUN_BACK_HIGHT , 0] , [-W_S,-W_S,-W_S,-W_S]],cur_key2]

	actions = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 ,0 , 0 , 0 , 0 , 0 , 0 , 0 , 0
	           , weak_attack ,  weak_attack_crouch_g , weak_attack_crouch_p ,weak_attack_air_g , weak_attack_air_p, weak_at_pied_air, strong_attack_g, strong_attack_p, strong_attack_crouch_g, strong_attack_crouch_p , strong_attack_air_g ,strong_attack_air_p,strongest_attack_g,strongest_attack_p ,strongest_a_crouch_g ,strongest_a_crouch_p,strongest_a_air_g 
	           , strongest_a_air_p , throw, throw_miss, throw_air, throw_a_miss, special_a_g,special_a_p, special_b, special_c_g, special_c_p,super_a, super_b, ken_throw]
	
	
	
	return actions[cur_key1]
	

#########################

def breaks() :
	return [(0,[0]),(0,[0]),(2,[4]),(1,[1]),(2,[2]),(2,[2]),(3,[2]),(2,[2]),(-1,[2]),(1,[2]),(1,[1]),(3,[3]),(3,[2]),(3,[2]),(-1,[2]),(-1,[2]),(2,[2]),(1,[1]),(0,[3]),(0,[2])               #0 a 19
	        ,(0,[1]),(-1,[3]),(-1,[2]),(-1,[2]),(-1,[1]),(-1,[1]),(-1,[3]),(-1,[3]),(-1,[3]),(-1,[2]),(-1,[2]),(-1,[1]),(-1,[1]),(-1,[3]),(-1,[3]),(-1,[2,1]),(-1,[2,1]),(-1,[1]),(-1,[1]),(-1,[3])          #20 a 39
	        ,(-1,[3]),(0,[2]), (-1,[2]), (0,[3]), (-1,[3]),(-1,[2,1]),(-1,[2,1]),(-1,[2,1]),(-1,[2,1]),(-1,[2,1]),(-1,[[2,1],1]),(-1,[[2,1],1]),(-1,[2])] 		
				#(a,b) contient a=on peut break? (0 peut pas break(damages) , -1 =seulement les damages peuvent break ; 1 break crouch ,2 break stand
				# 3 break air) , b = il peut break qui? et pareil avec a
				# mais ici 0 c pour les damages car ca break tout et 4 il ne break persone
				#pour les supper il fo le maxi dc le b est un tableux [[il peut break] , maxi minimal]

##########################


#########################

def descendre(key , y,bankai) :		#key est l'action selon laquelle on descent (jump ,forwrd jump ...) ; y est la hauteur courante
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
		return [1, len(act[3])+i+1 , key]

####################################

def scale (heigh, s, k) :
	if s == 'super move b' :
		if k == 8 or k == 9 :
			return heigh/194
		else :
			return 1
	else :
		return 1

####################################

def puissance(key,puissance) :
	if key == 47 or key == 50:
		return [1,[]]
####################################

def bankai(key,bankai) :
	if key == 47 or key == 50:
		return [1,[],1,1]
####################################
####################################

def super(key,max_num) :           #2e valeur retournee est l'indice de l'image de la super a display avant
	if key == 50 or key == 51:
		return [max_num - 1 , 1]             # -1 car on use 1 maxi pour executer ca ; si on modifie ds breaks fo aussi modifier ici
	else:
		return [max_num , 0]                  # n'ont pas besoin de maxi pour s'executer
####################################
####################################

def computer(act_type,num_maxs) :
	if act_type :
		#if num_maxs >= 1:
		#	return range(41)[23:]+[42,44,45,46,47,48,49,50,51,52]
		#else :
		#	return range(41)[23:]+[42,44,45,46,47,48,49,52]
		return [26,27,28,33,34]
	else :
		#return [4,5,6,7,8,9]+[11,12,13,14,15,15]
		return [6,12,13]
####################################

def personality() :
	return random.choice([1,0,0,0,1,1,1,0,1,0,1,1,1])


def ds():
	byaku={'intro' : [[0, 50,99]  , [0, 50,99]  , [0, 50,99]  , [0, 50,99]  , [0, 55,99]  , [0, 73,118] ],  'win' : [[0, 44,99]  , [0, 55,99]  , [0, 50,99]  , [0, 50,99]  , [0, 50,99]  , [0, 50,99] ] , 'stance' : [[0, 62,99]  , [0, 62,99]  , [0, 63,99]  , [0, 63,99]  , [0, 63,99]  , [0, 63,99]  , [0, 62,99]  , [0, 62,99] ],  'turn' : [[0, 56,98]  , [0, 56,98] ],  'crouch' : [[0, 73,76]  , [0, 81,64] ] , 'walk' : [[0, 51,95]  , [0, 49,95]  , [0, 44,96]  , [0, 46,95]  , [0, 53,94]  , [0, 50,95]  , [0, 43,96]  , [0, 45,95] ],  'run' : [[0, 60,86]  , [0, 60,88]  , [0, 62,86]  , [0, 62,88] ],  'air dash' : [[0, 70,71]  , [0, 60,88] ] , 'jump' : [[0, 73,76]  , [0, 53,99]  , [0, 70,71]  , [0, 53,99]  , [0, 73,76] ],  'forward jump' : [[0, 73,76]  , [0, 61,95]  , [0, 70,71]  , [0, 88,96]  , [0, 73,76] ],  'teleport' : [[0, 43,96]  , [0, 57,85]  , [0, 62,87] ] , 'guard' : [[0, 58,97]  , [0, 70,65] ],  'damage' : [[0, 64,96]  , [0, 89,93]  , [0, 74,95]  , [0, 85,90]  , [0, 95,66]  , [0, 97,64] ] , 'fall down 1' : [[0, 93,55]  , [0, 62,96]  , [0, 103,89]  , [0, 104,33]  , [0, 72,52] ],  'fall down 2' : [[0, 82,72]  , [0, 74,95]  , [0, 85,90]  , [0, 85,98]  , [0, 103,89]  , [0, 104,33]  , [0, 72,52] ] , 'weak attack g' : [[0, 58,99]  , [0, 121,97]  , [0, 121,97]  , [0, 135,95]  , [0, 93,95]  , [0, 80,95]  , [0, 80,95]  , [0, 54,97] ],  'weak attack p' : [[0, 58,99]  , [0, 109,97]  , [0, 80,95]  , [0, 54,97] ] , 'weak attack crouch' : [[0, 81,64]  , [0, 110,64]  , [0, 109,64]  , [0, 81,64] ],  'weak attack air g' : [[0, 100,89]  , [0, 119,89]  , [0, 124,89]  , [0, 118,89] ],  'weak attack air p' : [[0, 100,89]  , [0, 118,89] ] , 'strong attack g' : [[0, 77,117]  , [0, 77,123]  , [0, 137,123]  , [0, 121,106]  , [0, 113,94]  , [0, 74,94]  , [0, 69,94]  , [0, 54,97] ],  'strong attack p' : [[0, 77,117]  , [0, 118,96]  , [0, 69,94]  , [0, 54,97] ] , 'strong attack crouch g' : [[0, 69,85]  , [0, 69,85]  , [0, 122,84]  , [0, 125,94]  , [0, 114,94]  , [0, 90,93]  , [0, 90,88]  , [0, 109,64] ] , 'strong attack crouch p' : [[0, 69,85]  , [0, 117,64]  , [0, 90,88]  , [0, 109,64] ] , 'strong attack air g' : [[0, 75,110]  , [0, 75,114]  , [0, 120,118]  , [0, 122,114]  , [0, 122,114]  , [0, 109,114]  , [0, 93,113] ],  'strong attack air p' : [[0, 75,110]  , [0, 93,113] ] , 'strongest attack g' : [[0, 80,106]  , [0, 80,107]  , [0, 128,95]  , [0, 135,105]  , [0, 135,105]  , [0, 129,105]  , [0, 111,105]  , [0, 109,97]  , [0, 54,97] ] , 'strongest attack p' : [[0, 80,106]  , [0, 128,88]  , [0, 111,105]  , [0, 109,97]  , [0, 54,97] ] , 'strongest attack crouch g' : [[0, 70,64]  , [0, 73,66]  , [0, 115,85]  , [0, 115,85]  , [0, 114,85]  , [0, 114,83]  , [0, 109,64] ],  'strongest attack crouch p' : [[0, 70,64]  , [0, 72,66]  , [0, 114,83]  , [0, 109,64] ] ,  'strongest attack air g' : [[0, 80,100]  , [0, 80,101]  , [0, 128,99]  , [0, 142,88]  , [0, 142,88]  , [0, 139,88]  , [0, 120,88] ] , 'strongest attack air p' : [[0, 80,100]  , [0, 127,82]  , [0, 120,88] ] , 'throw' : [[0, 59,96]  , [0, 91,96]  , [0, 71,99]  , [0, 85,98] ],  'throw miss' : [[0, 59,96]  , [0, 91,96]  , [0, 83,93]  , [0, 80,93] ] , 'throw air' : [[0, 89,93]  , [0, 91,96]  , [0, 71,99]  , [0, 85,98] ],  'throw air miss' : [[0, 89,93]  , [0, 106,79] ] , 'special move a' : [[0, 65,99]  , [0, 65,98]  , [0, 64,98]  , [0, 66,98]  , [0, 83,128]  , [0, 69,135]  , [0, 50,135]  , [0, 53,123]  , [0, 62,120]  , [0, 62,121]  , [0, 62,121]  , [0, 61,121]  , [0, 61,121]  , [0, 61,121]  , [0, 63,120]  , [0, 63,120]  , [0, 63,121]  , [0, 65,121]  , [0, 65,120]  , [0, 63,120]  , [0, 64,113]  , [0, 64,112]  , [0, 62,112]  , [0, 63,105]  , [0, 65,104]  , [0, 63,104]  , [0, 65,98]  , [0, 64,98]  , [0, 62,98]  , [0, 64,98]  , [0, 61,98]  , [0, 63,98]  , [0, 63,98]  , [0, 52,8] , [0, 62,98]  , [0, 61,98]  , [0, 64,99] ],  'special move a p' : [[0, 65,99]  , [0, 65,98]  , [0, 64,98]  , [0, 66,98]  , [0, 83,128]  , [0, 69,135]  , [0, 50,135]  , [0, 53,123]  , [0, 62,98]  , [0, 61,98]  , [0, 58,98]  , [0, 64,99]  , [0, 52,8] ] , 'special move b g' : [[0, 65,99]  , [0, 65,98]  , [0, 64,98]  , [0, 66,98]  , [0, 70,98]  , [0, 70,98]  , [0, 75,97]  , [0, 68,97]  , [0, 64,98]  , [0, 79,98]  , [0, 115,103]  , [0, 114,113]  , [0, 114,113]  , [0, 107,112]  , [0, 93,96]  , [0, 95,96]  , [0, 79,96] ] , 'special move b p' : [[0, 68,97]  , [0, 64,98]  , [0, 79,98]  , [0, 78,98]  , [0, 90,112]  , [0, 93,96]  , [0, 95,96]  , [0, 79,96] ] , 'miss' : [[0, 68,97]  , [0, 64,98]  , [0, 79,98]  , [0, 78,98]  , [0, 123,96]  , [0, 117,96]  , [0, 107,96]  , [0, 79,96] ] , 'special move c' : [[0, 47,96]  , [0, 60,96]  , [0, 58,96]  , [0, 86,96]  , [0, 91,96]  , [0, 91,96]  , [0, 58,96]  , [0, 60,96]  , [0, 47,96]  , [0, 36,82]  , [0, 59,86]  , [0, 47,85]  , [0, 47,89]  , [0, 42,86]  , [0, 15,15]  , [0, 4,2]  , [0, 14,27]  , [0, 13,29]  , [0, 12,29]  , [0, 12,29]  , [0, 14,29] ] , 'special move d' : [[0, 47,96]  , [0, 60,96]  , [0, 58,96]  , [0, 86,96]  , [0, 91,96]  , [0, 91,96]  , [0, 58,96]  , [0, 60,96]  , [0, 47,96]  , [0, 128,140]  , [0, 1,1]  , [0, 32,69]  , [0, 32,69]  , [0, 40,67]  , [0, 37,66]  , [0, 45,62]  , [0, 42,65] ] , 'super move a' : [[0, 65,99]  , [0, 65,98]  , [0, 64,98]  , [0, 66,98]  , [0, 50,98]  , [0, 64,99]  , [0, 13,135]  , [0, 28,26]  , [0, 52,8] ] , 'super move b' : [[0, 65,99]  , [0, 65,99]  , [0, 84,98]  , [0, 84,98]  , [0, 84,98]  , [0, 65,99]  , [0, 65,99]  , [0, 64,99]  , [0, 6,62]  , [0, 10,143] ] , 'super move c' : [[0, 65,99]  , [0, 65,98]  , [0, 64,98]  , [0, 66,98]  , [0, 50,98]  , [0, 256,192]  , [0, 80,135]  , [0, 80,135]  , [0, 81,135]  , [0, 124,135] , [0, 95,186]  , [0, 35,68]  , [0, 95,186]  , [0, 260,192]  , [0, 258,192]  , [0, 256,192]  , [0, 62,99]  , [0, 62,99]  , [0, 84,99]  , [0, 137,129]  , [0, 239,175]  , [0, 191,173]  , [0, 229,178] , [0, 141,85]  , [0, 142,90]  , [0, 220,135]  , [0, 99,93]  , [0, 86,86] ] }
	return byaku