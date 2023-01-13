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
WEAK = 8		#profondeur unite 
JUMP_LENGHT = 12		#nombre d'images de jump... ici c 7 images 0.png ... 6.png utilise pour weak attack air
#########################
def ymax():
	return int(round (HEIGH / YCONST))
########################
def songs(key1) :
    return "intro.wav"
	
#######################
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
	teleport_avant = ['teleport' , [0,1,2,1] , [1,2,2,2] , [0,0,0,0] , [R_S,R_S,R_S,R_S]]								#14
	teleport_back = ['teleport' , [0,1,2,1] , [1,2,2,2] , [0,0,0,0] , [-R_S,-R_S,-R_S,-R_S]]							#15	
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
		[bl,index,cur_key] = descendre(12 , prev_base , bankai)
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
	strongest_attack_g = ['strongest attack g' , [0,1,2,3,4,4,5,6,7,8,9,10,11] , [1,1,1,1,1,1,8*WEAK,6*WEAK,4*WEAK,3*WEAK,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0],[-R_S,0,0,0,R_S,R_S,2*R_S,0,0,0,0,0,0]]		#35
	strongest_attack_p = ['strongest attack p' , [0,1,2,3,4,5,6,7,8,9] , [1,1,1,1,6*WEAK,4*WEAK,3*WEAK,1,1,1],[0,0,0,0,0,0,0,0,0,0],[-R_S/2,0,0,0,R_S/2,R_S,0,0,0,0]]	#36
	strongest_a_crouch_g = ['strongest attack crouch g' , [0,1,2,3,4,5,6,7,8,9] , [-1,-1,-1,-1,-WEAK,-4*WEAK,-3*WEAK,-2*WEAK,-1,-1,-1],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0] , 'extra']		#37		DOIT SE FAIRE LE JOUER ETANT DEBOUT de mem strongest_a_crouch_p (38)
	strongest_a_crouch_p = ['strongest attack crouch p' , [0,1,2,3,4,5,6,7] , [-1,-1,-1,-1,-WEAK,-3*WEAK,-2*WEAK,-WEAK,-1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0] , 'extra']	#38
	strongest_a_air_g = ['strongest attack air g' , [0,1,2,3,4,5,6,7,8,9] , [1,1,1,1,20*WEAK,12*WEAK,8*WEAK,1,1,1],[prev_base+(h+F_H)/3,prev_base+2*(h+F_H)/3 ,F_H+HEIGH,HEIGH,M_H,F_H,0,0,0,0] ,[R_S,R_S,R_S,R_S,R_S,J_S,J_S,J_S,0,0]]	#39
	strongest_a_air_p = ['strongest attack air p' , [0,1,2,3,4,5,6,7] , [1,1,1,1,12*WEAK,8*WEAK,4*WEAK,1],[prev_base+h/3,prev_base+2*h/3 ,HEIGH+F_H/2 ,HEIGH,M_H,F_H,0,0] , [J_S,J_S,J_S,W_S,W_S,W_S,0,0]]	#40
	throw = ['throw' , [0,1,2,2,2,3,3,3] , [5*WEAK ,0,0,0,0,0,0,0] , [0,0,0,0,0,0,0,0] ,[0,0,0,0,0,R_S,R_S,R_S]]	#41
	throw_miss = ['throw miss' , [0,1,1,1,2] , [2,2,2,2,2] , [0,0,0,0,0,0] ,[0,0,0,0,0,0]]		#42
	a=prev_base #prevact[3][index]
	throw_air= ['throw air' , [0,0,1,2,2,3,3,0,0,0,0,0,0][:n+6] , [5*WEAK ,0,0,0,0,0,0,0,0,0,0,0,0][:n+6] , [a,a,a,a,a,a]+prevact[3][index:] , [0,0,0,0,0,0]+prevact[4][index:]]	#43
	throw_a_miss=['throw air miss' , [0,1,2,0,0,0,0,0,0,0,0,0][:n] , [2,2,2,2,2,1,1,1,1,1,1,1][:n] , prevact[3][index:] , prevact[4][index:]]		#44
	special_a_g=['special move a g' , [0,1,2,1,2,3,4,5,6,7,8,9,10] , [1,1,1,1,0,0,0,10*WEAK,6*WEAK,3*WEAK,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,2*R_S,2*R_S,2*R_S,2*R_S,2*R_S,R_S,0,0,0,0,0,0]]		#45
	special_a_p=['special move a p' , [0,1,2,1,2,3,4,5,6,7] , [1,1,1,1,0,0,0,8*WEAK,4*WEAK,1],[0,0,0,0,0,0,0,0,0,0],[0,2*R_S,2*R_S,2*R_S,2*R_S,2*R_S,R_S,0,0,0]]		#46
	special_b = ['special move b' , [0,1,2,0,1,2] , [1,1,1,1,1,1] , [0,0,0,0,0,0] , [0,0,0,0,0,0]]	 #47
	special_c_g = ['special move c g' , [0,1,2,3,4,5,6,5,6,7,8,9,10,11,10,11,10,11] , [1,1,1,1,1, 3*WEAK, 3*WEAK, 3*WEAK,3*WEAK, 6*WEAK, 4*WEAK, 2*WEAK, WEAK,1,1,1,1,1], [0,0,0,0,0,0,0,0,0,F_H,M_H,M_H+F_H,HEIGH,HEIGH,M_H+F_H,M_H,F_H,0], [0,0,0,0,0,2*R_S,2*R_S,2*R_S,2*R_S,R_S,R_S,R_S,R_S,W_S,W_S,W_S,W_S,0]]	#48
	special_c_p = ['special move c p' , [0,1,2,3,4,5,6,5,6,7,8,8,7,8] , [1,1,1,1,1,3*WEAK,3*WEAK,3*WEAK,3*WEAK,4*WEAK,2*WEAK,1,1,1],[0,0,0,0,0,0,0,0,0,F_H,M_H,M_H,F_H,0],[0,0,0,0,0,2*R_S,2*R_S,2*R_S,2*R_S,R_S,R_S,W_S,W_S,0]]		#49
	super_a = ['super move a', [0,1,2,3,4,5,6,7,8,14,15,16,17,18,19,20,21], [1,1,1,1,1,1,1,1,15*WEAK,10*WEAK,1,1,1,1,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]		#50
	super_b = ['super move b', [0,1,0,1,2,3,4,5,8,9,5,3,6,7,6,7], [1,1,1,1,1,1,1,10*WEAK,0,0,10*WEAK,1,1,1,1,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] , 'extra']		#51
	ken_throw = ['throw g', [0,1,2,3,4,5,6,6], [1,1,1,2*WEAK,2*WEAK,2*WEAK,1,1],[0,0,0,0,0,0,0,0],[0,0,0,1.5*R_S,1.5*R_S,1.5*R_S,0,0] , 'extra']               #52
	p53 = 0            #53
	p54 = 0            #54

	actions = [intro , win , stance , turn , walk_avant , walk_back , jump , run_avant , run_back  , crouch , crouch_turn , air_dash  , forward_jump  , backward_jump , teleport_avant ,teleport_back ,  up_guard , down_guard , damage_upup , damage_updown 
	           , damage_down , fall1 , fall2 , weak_attack ,  weak_attack_crouch_g , weak_attack_crouch_p ,weak_attack_air_g , weak_attack_air_p, weak_at_pied_air, strong_attack_g, strong_attack_p, strong_attack_crouch_g, strong_attack_crouch_p , strong_attack_air_g ,strong_attack_air_p,strongest_attack_g,strongest_attack_p ,strongest_a_crouch_g ,strongest_a_crouch_p,strongest_a_air_g 
	           , strongest_a_air_p , throw, throw_miss, throw_air, throw_a_miss, special_a_g,special_a_p, special_b, special_c_g, special_c_p,super_a, super_b, ken_throw]	
	return actions[input_] 

#########################
def stay_down():
	return ['fall down 2' , [0,1,2,3,4,5] ,[0,0,0,0,0,0] , [0,0,0,0,0,-20] , [0,0,0,0,0,0]]
##########################
def throw(is_air,bankai,prev_base1):
	if is_air:
		return ['throw' , [0,1,0] , [0,1,0] , [0,1,0] ,[0,1,0]]
	else:
		return ['throw air' , [0,0,3,3,3] , [0,0,0,0,0] , [prev_base1,prev_base1,M_H,F_H,0] , [0,-J_S,-R_S,-R_S,-J_S]] 
##############################

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
	strong_attack_crouch_g = [['fall down 2',[0,1,2,3,4,5,6,0][:n]  , [1,1,1,1,1,0,0,1][:n] ,[RUN_BACK_HIGHT, RUN_BACK_HIGHT ,RUN_BACK_HIGHT , 0,0,-20,0,0][:n] , [-2*W_S,-W_S,-W_S,0,0,0,0,0][:n]],22]	#31
	strong_attack_crouch_p = [['fall down 2',[0,1,2,3,4,5,6,0][:n]  , [1,1,1,1,1,0,0,1][:n] ,[RUN_BACK_HIGHT, RUN_BACK_HIGHT ,0 , 0,0,-20,0,0][:n] , [-W_S,-W_S,0,0,0,0,0,0][:n]],22]	#32
	strong_attack_air_g = [['fall down 2',[0,0]  , [1,1] ,[y2 + 2 * RUN_BACK_HIGHT,0] , [-3 * W_S,0]],cur_key2]	#33
	strong_attack_air_p = [['fall down 2',[0,0]  , [1,1] ,[y2 +  RUN_BACK_HIGHT,0] , [-2 * W_S,0]],cur_key2]	#34
	strongest_attack_g = [['fall down 1',[0,0,0,1,2,3,4,0][:n]  , [1,1,1,1,1,0,0,1][:n] ,[F_H, M_H , M_H + 2* RUN_BACK_HIGHT ,M_H,F_H,-20,0,0][:n] , [-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,0][:n]],21]		#35
	strongest_attack_p = [['fall down 1',[0,0,0,1,2,3,4,0][:n]  , [1,1,1,1,1,0,0,1][:n] ,[F_H, M_H , M_H + RUN_BACK_HIGHT ,M_H,F_H,-20,0,0][:n] , [-J_S,-J_S,-W_S,-W_S,-W_S,-J_S,-J_S,0][:n]],21]	#36
	strongest_a_crouch_g =[['fall down 1',[0,0,0,0,1,2,3,4,0][:n]  , [1,1,1,1,1,1,0,0,1][:n] ,[F_H, M_H ,F_H + M_H , HEIGH ,M_H,F_H,-20,0,0][:n] , [0,0,0,0,0,0,0,0,0][:n]],21]		#37		DOIT SE FAIRE LE JOUER ETANT DEBOUT de mem strongest_a_crouch_p (38)
	strongest_a_crouch_p = [['fall down 1',[0,0,0,1,2,3,4,0][:n]  , [1,1,1,1,1,0,0,1][:n] ,[F_H, M_H , M_H + F_H ,M_H,F_H,-20,0,0][:n] , [0,0,0,0,0,0,0,0][:n]],21]	#38
	r = min(1,int(round(M_H/(y2+1))))
	strongest_a_air_g = [['fall down 1',[0,0,0,0,0,0,0,1,2,3,4,0][r:n]  , [1,1,1,1,1,1,1,1,1,0,0,1][r:n] ,[M_H,0,0,F_H,M_H,M_H+F_H,M_H+F_H,M_H,F_H,-20,0,0][r:n] , [0,0,0,0,0,0,0,0,0,0,0,0][r:n]],21]
	strongest_a_air_p = [['fall down 1',[0,0,0,0,0,0,0,1,2,3,4,0][r:n]  , [1,1,1,1,1,1,1,1,1,0,0,1][r:n] ,[M_H,0,0,F_H,M_H,M_H+F_H,M_H+F_H,M_H,F_H,-20,0,0][r:n] , [0,0,0,0,0,0,0,0,0,0,0,0][r:n]],21]	#40
	throw = [['fall down 2' , [0,0,0,0,0,0,0,0 ,0,0,1,2,3,4,5,5,5,6,6] ,  [0,0,0,0,0,0,0,0 ,0,0,0,0,0,0,0,0,0,0,0] , [0,0,0,0,0,0,0,0 ,0,0,0,0,0,0,-20,-20,-20,0,0] ,[0,R_S,0,0,0,0,0,0 ,-R_S,-R_S,-R_S,-R_S,-R_S,-R_S,-R_S,0,0,0,0]],22]	#41
	throw_miss = [['throw miss' , [0,1,1,1,2] , [0,0,0,0,0,0] ,[0,0,0,0,0,0]]]		#42
	throw_air= [['fall down 1' , [0,0,0,0,0,0,1,2,3,3,3,4,0][:n] , [0,0,0,0,0,0,0,0,0,0,0,0,0][:n] , [y2,y2,y2,y2,y2,y2,M_H,F_H,0,-20,-20,0,0][:n] , [0,0,0,0,0,J_S,R_S,R_S,R_S,0,0,0,0][:n]],21]	#43
	throw_a_miss=[['throw air miss' , [0,1,2,0,0,0,0,0,0,0][:n] ,  0 , 0]]	#44
	special_a_g=[['fall down 1',[0,0,0,1,2,3,4,0][:n]  , [1,1,1,1,1,0,0,1][:n] ,[F_H, M_H , M_H + 2* RUN_BACK_HIGHT ,M_H,F_H,-20,0,0][:n] , [-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,0][:n]],21]		#45
	special_a_p=[['fall down 1',[0,0,0,1,2,3,4,0][:n]  , [1,1,1,1,1,0,0,1][:n] ,[F_H, M_H , M_H + RUN_BACK_HIGHT ,M_H,F_H,-20,0,0][:n] , [-J_S,-J_S,-W_S,-W_S,-W_S,-J_S,-J_S,0][:n]],21]		#46
	special_b = [['special move b' , [0,1,2,0,1,2] ,  [0,0,0,0,0,0] , [0,0,0,0,0,0]]]	 #47
	special_c_g = [['fall down 1' , [0,0,0,0,0,0,1,2,2,3,4,0][:n] , [1,1,1,1,1,1,1,1,1,0,0,1][:n] , [F_H,M_H,M_H+F_H,HEIGH,HEIGH+RUN_BACK_HIGHT,HEIGH,M_H+F_H,M_H,0,-20,0,0][:n], [0,0,0,0,0,0,0,0,0,0,0,0][:n]],21]	#48
	special_c_p = [['fall down 1' , [0,0,0,0,1,2,2,3,4,0][:n] ,[1,1,1,1,1,1,1,0,0,1][:n] , [F_H,M_H,M_H+F_H,M_H,F_H,0,-20,0,0,0][:n],[0,0,0,0,0,0,0,0,0,0][:n]],21]		#49
	super_a = [['fall down 2',[0,1,2,3,4,5,5,6,0][:n]  , [1,1,1,1,1,0,0,0,1][:n] ,[0,0 ,0 , 0,0,0,-20,0,0][:n] , [-R_S,-R_S,-R_S,-R_S,-R_S,-R_S,0,0,0][:n]],22]		#50
	r = int(round (y2/F_H))
	super_b = [['fall down 1', [0,0,0,0,0,1,2,2,3,4,0][r:n],[1,1,1,1,1,1,1,1,0,0,1][r:n],[F_H,M_H,F_H+M_H,HEIGH,HEIGH,F_H+M_H,M_H,F_H,0,-20,0][r:n],[-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,-J_S,0][r:n]],21]		#51
	ken_throw = [['fall down 2',[0,0,0,0]  , [1,1,1,1] ,[RUN_BACK_HIGHT, RUN_BACK_HIGHT ,RUN_BACK_HIGHT , 0] , [-W_S,-W_S,-W_S,-W_S]],cur_key2]

	actions = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 ,0 , 0 , 0 , 0 , 0 , 0 , 0 , 0
	           , weak_attack ,  weak_attack_crouch_g , weak_attack_crouch_p ,weak_attack_air_g , weak_attack_air_p, weak_at_pied_air, strong_attack_g, strong_attack_p, strong_attack_crouch_g, strong_attack_crouch_p , strong_attack_air_g ,strong_attack_air_p,strongest_attack_g,strongest_attack_p ,strongest_a_crouch_g ,strongest_a_crouch_p,strongest_a_air_g 
	           , strongest_a_air_p , throw, throw_miss, throw_air, throw_a_miss, special_a_g,special_a_p, special_b, special_c_g, special_c_p,super_a, super_b, ken_throw]
	
	
	
	return actions[cur_key1]
	

#########################

def breaks() :
	return [(0,[0]),(0,[0]),(2,[4]),(1,[1]),(2,[2]),(2,[2]),(3,[2]),(2,[2]),(-1,[2]),(1,[2]),(1,[1]),(3,[3]),(3,[2]),(3,[2]),(-1,[2]),(-1,[2]),(2,[2]),(1,[1]),(0,[3]),(0,[2])               #0 a 19
	        ,(0,[1]),(-1,[3]),(-1,[2]),(-1,[2]),(-1,[1]),(-1,[1]),(-1,[3]),(-1,[3]),(-1,[3]),(-1,[2]),(-1,[2]),(-1,[1]),(-1,[1]),(-1,[3]),(-1,[3]),(-1,[2,1]),(-1,[2,1]),(-1,[1]),(-1,[1]),(-1,[3])          #20 a 39
	        ,(-1,[3]),(0,[2]), (-1,[2]), (0,[3]), (-1,[3]),(-1,[2,1]),(-1,[2,1]),(-1,[2,1]),(-1,[2,1]),(-1,[2,1]),(-1,[[2,1],3]),(-1,[[2,1],1]),(-1,[2]),(-1,[10]),(-1,[10]),(-1,[10])] 		
				#(a,b) contient a=on peut break? (0 peut pas break(damages) , -1 =seulement les damages peuvent break ; 1 break crouch ,2 break stand
				# 3 break air) , b = il peut break qui? et pareil avec a
				# mais ici 0 c pour les damages car ca break tout et 4 il ne break persone
				#pour les supper il fo le maxi dc le b est un tableux [[il peut break] , maxi minimal]
def breaks_bankai() :
	return []
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

def puissance(key,puissance,x,y,bankai) :
	if key == 51:
		super_b = ['super move b', [8,9], [10*WEAK,10*WEAK], [0,0], [0,0]]
		return [1 , {'data':super_b , 'index':-1 , 'start':8 , 'end':9 , 'type' : 2,'key' : 51}]
	else :
		return [1,{}]
####################################

def bankai(key,bankai,x,y) :
	if not bankai[0] :
		if key == 47 :
			special_b = ['special move b', [3,4,5,6,7]]          # x et y st les pourcentage(0 a 100) de longeur et largeur de l'image 
			return [1,{'type':1 ,'data':special_b , 'index':[0,1,2,3,4] ,'x':[15,15,48,82,82] ,'y':[15,65,40,15,65] ,'count':50} , 2,1]             #13 points
		elif key == 50 :
			super_a = ['super move a', [9,10,11,12,13]]          # x et y st les pourcentage(0 a 100) de longeur et largeur de l'image 
			return [1,{'type':1 ,'data':super_a , 'index':[0,1,2,3,4] ,'x':[15,15,48,82,82] ,'y':[15,65,40,15,65] ,'count':100} , 3 , 1.5] 
		else :
			return [1,{},1,1] 
	elif key in [47,50] :
		return [0,{},1,1]
	else:
		return bankai          #return [actif,{},facteur force , facteur deplacement]
####################################
####################################

def super(key,max_num) :           #2e valeur retournee est l'indice de l'image de la super a display avant
	if  key == 51:
		return [max_num - 1 , 1]             # -1 car on use 1 maxi pour executer ca ; si on modifie ds breaks fo aussi modifier ici
	if  key == 50:
		return [max_num - 3 , 2]   
	else:
		return [max_num , 0]                  # n'ont pas besoin de maxi pour s'executer
####################################
####################################

def computer(act_type,num_maxs,bankai) :
	if act_type :
		if bankai:
			if num_maxs >= 1:
				return list(range(41))[23:]+[42,44,45,46,48,49,51,52]
			else :
				return list(range(41))[23:]+[42,44,45,46,48,49,52]
		else:
			if num_maxs >= 3:
				return list(range(41))[23:]+[42,44,45,46,47,48,49,50,51,52]
			elif num_maxs >= 1:
				return list(range(41))[23:]+[42,44,45,46,47,48,49,51,52]
			else :
				return list(range(41))[23:]+[42,44,45,46,47,48,49,52]
	else :
		return [4,5,6,7,8,9]+[11,12,13,14,15,15]
####################################

def personality() :
	return random.choice([1,0,0,0,1,1,1,0,1,0,1,1,1        ,1,1,1,1,1,1,1,1,1,1,1,1])

def ds() :		#le 1er champ init a 0 va contenir l'image
	ken={ 'intro' : [[0, 70,120]  , [0, 70,124]  , [0, 75,129]  , [0, 109,119] ], 'win' : [[0, 109,119]  , [0, 75,130]  , [0, 70,124]  , [0, 70,120]  , [0, 72,120]  , [0, 80,120] ] , 'stance' : [[0, 92,119]  , [0, 92,119]  , [0, 91,120]  , [0, 90,120]  , [0, 87,119]  , [0, 89,119]  , [0, 88,118]  , [0, 91,119] ], 'turn' : [[0, 72,122]  , [0, 72,122] ] , 'walk' : [[0, 76,119]  , [0, 82,118]  , [0, 86,118]  , [0, 86,119]  , [0, 87,118]  , [0, 79,118] ],  'run' : [[0, 85,108]  , [0, 86,101]  , [0, 86,109]  , [0, 86,100] ],  'crouch' : [[0, 93,121]  , [0, 88,75] ], 'crouch turn' : [[0, 103,78]  , [0, 103,78] ], 'air dash' : [[0, 118,92]  , [0, 85,108] ], 'jump' : [[0, 93,121]  , [0, 88,75]  , [0, 103,122]  , [0, 118,92]  , [0, 103,122]  , [0, 93,121]  , [0, 88,75] ] , 'forward jump' : [[0, 93,121]  , [0, 88,75]  , [0, 92,115]  , [0, 118,92]  , [0, 107,116]  , [0, 93,121]  , [0, 88,75] ] ,'teleport' : [[0, 91,118]  , [0, 95,118]  , [0, 94,117] ],   'guard' : [ [0, 72,122]  , [0, 102,70] ], 'damage' : [[0, 95,118]  , [0, 100,97]  , [0, 96,116]  , [0, 103,107]  , [0, 124,81]  , [0, 124,66] ],  'fall down 1' : [[0, 102,81]  , [0, 87,105]  , [0, 142,65]  , [0, 136,45]  , [0, 103,70] ], 'fall down 2' : [[0, 107,101]  , [0, 96,116]  , [0, 103,107]  , [0, 129,85]  , [0, 142,65]  , [0, 136,45]  , [0, 103,70] ], 'weak attack' : [[0, 96,120]  , [0, 80,139]  , [0, 133,119]  , [0, 133,119]  , [0, 96,120] ], 'weak attack crouch g' : [[0, 117,77]  , [0, 105,78]  , [0, 168,75]  , [0, 168,75]  , [0, 164,75]  , [0, 117,77] ],  'weak attack crouch p' : [[0, 117,77]  , [0, 105,78]  , [0, 164,75]  , [0, 117,77] ], 'weak attack air g' : [[0, 104,84]  , [0, 98,88]  , [0, 164,79]  , [0, 164,79]  , [0, 162,77]  , [0, 104,84] ],  'weak attack air p' : [[0, 104,84]  , [0, 98,88]  , [0, 162,77]  , [0, 104,84] ], 'strong attack g' : [[0, 114,92]  , [0, 149,92]  , [0, 154,91]  , [0, 114,93]  , [0, 160,94]  , [0, 177,142]  , [0, 177,142]  , [0, 170,142]  , [0, 145,140]  , [0, 117,119] ],  'strong attack p' : [[0, 114,92]  , [0, 149,92]  , [0, 154,91]  , [0, 114,93]  , [0, 160,94]  , [0, 151,141]  , [0, 145,140]  , [0, 117,119] ], 'strong attack crouch g' : [[0, 107,82]  , [0, 116,75]  , [0, 173,75]  , [0, 176,75]  , [0, 124,81]  , [0, 122,79]  , [0, 101,78] ], 'strong attack crouch p' : [[0, 107,82]  , [0, 116,75]  , [0, 168,75]  , [0, 142,75]  , [0, 124,81]  , [0, 122,79]  , [0, 101,78] ],  'strong attack air g' : [[0, 116,93]  , [0, 112,90]  , [0, 198,132]  , [0, 193,154]  , [0, 131,102]   , [0, 89,98]  , [0, 102,87] ],  'strong attack air p' : [[0, 116,93]  , [0, 112,90]  , [0, 163,86]  , [0, 89,98]  , [0, 102,87] ] , 'strongest attack g' : [[0, 100,118]  , [0, 90,117]  , [0, 121,104]  , [0, 117,115]  , [0, 98,132]  , [0, 192,189]  , [0, 158,179]  , [0, 158,110] , [0, 135,105]  , [0, 135,105]  , [0, 136,103]  , [0, 107,119] ] , 'strongest attack p' : [[0, 100,118]  , [0, 90,117]  , [0, 121,104]  , [0, 117,115]  , [0, 98,132]  , [0, 136,110]  , [0, 135,105]  , [0, 135,105]  , [0, 136,103]  , [0, 107,119] ] ,  'strongest attack crouch g' : [[0, 117,77]  , [0, 122,76]  , [0, 104,75]  , [0, 144,76]  , [0, 172,170]  , [0, 172,167]  , [0, 116,167]  , [0, 119,167]  , [0, 115,165] ,[0, 102,108]] ,  'strongest attack crouch p' : [ [0, 117,77]  , [0, 122,76]  , [0, 104,75]  , [0, 144,76]  , [0, 111,167]  , [0, 119,167]  , [0, 115,165]  , [0, 102,108] ], 'strongest attack air g' : [[0, 116,93]  , [0, 89,132]  , [0, 99,128]  , [0, 89,140]  , [0, 174,174]  , [0, 174,147]  , [0, 149,113]  , [0, 129,105]  , [0, 133,88] , [0, 102,88] ], 'strongest attack air p' : [[0, 116,93]  , [0, 89,132]  , [0, 99,128]  , [0, 89,140]  , [0, 128,109]  , [0, 129,105]  , [0, 133,88]  , [0, 102,88] ] ,  'throw g' : [[0, 114,92]  , [0,119,92]  , [0, 120,94]  , [0, 179,94]  , [0, 179,94]  , [0, 179,94]  , [0, 177,94] ],  'throw' : [[0, 114,92]  , [0, 119,92]  , [0, 120,94]  , [0, 177,94] ], 'throw miss' : [[0, 114,92]  , [0, 119,92]  , [0, 119,91] ] , 'throw air' : [[0, 112,86]  , [0, 133,83]  , [0, 110,94]  , [0, 139,94] ],   'throw air miss' : [[0, 112,86]  , [0, 133,83]  , [0, 130,79] ],  'special move a g' : [[0, 107,119]  , [0, 105,78]  , [0, 107,78]  , [0, 115,93]  , [0, 110,107]  , [0, 183,178]  , [0, 178,174]  , [0, 178,133] , [0, 134,131]  , [0, 134,122]  , [0, 107,119] ] ,  'special move a p' : [[0, 107,119]  , [0, 105,78]  , [0, 107,78]  , [0, 115,93]  , [0, 110,107]  , [0, 134,131]  , [0, 134,122]  , [0, 107,119] ],   'special move b' : [[0, 79,113]  , [0, 77,113]  , [0, 81,113]  , [0, 4,16]  , [0, 4,18]  , [0, 4,20]  , [0, 4,26]  , [0, 4,30] ],   'special move c g' : [[0, 100,118]  , [0, 96,117]  , [0, 86,103]  , [0, 94,103]  , [0, 114,103]  , [0, 186,88]  , [0, 189,88]  , [0, 131,200]  , [0, 109,155] , [0, 127,155]  , [0, 97,153]  , [0, 119,153] ],  'special move c p' : [[0, 100,118]  , [0, 96,117]  , [0, 86,103]  , [0, 94,103]  , [0, 114,103]  , [0, 186,88]  , [0, 189,88]  , [0, 119,153]  , [0, 97,153] ] , 'super move a' : [[0, 82,111]  , [0, 86,112]  , [0, 94,112]  , [0, 86,112]  , [0, 82,111]  , [0, 80,114]  , [0, 76,118]  , [0, 75,118]  , [0, 135,118]  , [0, 4,14]  , [0, 4,16]  , [0, 4,18]  , [0, 4,24]  , [0, 4,28]  , [0, 109,119]  , [0, 75,130]  , [0, 70,124]  , [0, 70,120]  , [0, 72,120]  , [0, 80,120]  , [0, 72,120]  , [0, 70,120]] , 'super move b' : [[0, 144,111]  , [0, 137,111]  , [0, 150,112]  , [0, 142,126]  , [0, 151,151] , [0, 145,197] , [0, 144,111]  , [0, 137,111]  , [0, 96,193]  , [0, 93,193] , [0,1,1] ]}
	return ken
