import pygame, sys, os, time,math, collision , functions ,random
from pygame.locals import *
##### IMPORT PLAYERS DATA STRUCTURES
import kenpachi , ichigo , byakuya

pygame.mixer.pre_init(22050, -16, 2, 4096)
pygame.init()
resolutions = pygame.display.list_modes()
good_res = (720, 480)
# look for most similar resolution to good_res
index = -1
while index > -len(resolutions) and not(resolutions[index][0] >= good_res[0] and resolutions[index][1] >= good_res[1]):
    index -= 1
SCREEN_WIDTH  = resolutions[index][0]
SCREEN_HEIGHT = resolutions[index][1]
windowSurface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.RESIZABLE,32)
pygame.display.set_caption("BNO")

################################# INITIALIZATION

#################################  FUNCTIONS

#scroll background
### take an image 'back' and return the shift dx and dy of the rectangle screeen whom up left corner is old_uplef=[x,y]###
def background_scroll(back,old_upleft,dx,dy):   #back est de type Surface 
	     #return a surface which is the  new screen  : dx,dy st les deplcements("-"pour haut et gauche) ,old_upleft=[x,y] 
	old_upleft[0] += dx      
	old_upleft[1] += dy
		#old_upleft est now le nouveau coin superieur gauche du nouveau ecran sur back
	back1 = back.subsurface(old_upleft[0],old_upleft[1],SCREEN_WIDTH,SCREEN_HEIGHT)
	return  back1

#######################  CONSTANTS ###################
BLOCK_RATIO = 3     # pourcentage enleve lorsque block
MAXI_CONST = 2
PLAYERS_STRENGHT = 2  #1
MIN_X_AREA = 50
MIN_Y_AREA = 40

YMAXSHROLL = SCREEN_HEIGHT / 15

SOL = SCREEN_HEIGHT - YMAXSHROLL

BACK_IMAGE_LENGTH = SCREEN_WIDTH * 3
BACK_IMAGE_HEIGHT = SCREEN_HEIGHT + SOL
############################################################


###### ici on determine le chemin vers les image .png du jeu #####
i=-1
while (sys.argv[0][i]!='/') and (sys.argv[0][i]!='\\') :
	i-=1
BNO_path = sys.argv[0][:i]

###################### CHOSE THE DISPLAY MODE ################

WINDOW_MODE_ = pygame.image.load(os.path.join('data', BNO_path + '/images/backgrounds/WINDOW.PNG')).convert_alpha()
FULLSCREEN_MODE_ = pygame.image.load(os.path.join('data', BNO_path + '/images/backgrounds/FULLSCREEN.PNG')).convert_alpha()
back = pygame.image.load(os.path.join('data', BNO_path + '/images/backgrounds/CHOOSE_BACK.PNG')).convert_alpha()
ok = 1
full_s = 0
windowSurface.blit(back,(-10,-10))
windowSurface.blit(WINDOW_MODE_,(SCREEN_WIDTH/2-155,SCREEN_HEIGHT/2-95))
pygame.display.update()
while ok:
	for event in pygame.event.get() :
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key in [K_UP , K_w , K_s , K_DOWN ,  K_a , K_d , K_LEFT , K_RIGHT]:
				if full_s :
					full_s = 0
					windowSurface.blit(back,(-10,-10))
					windowSurface.blit(WINDOW_MODE_,(SCREEN_WIDTH/2-155,SCREEN_HEIGHT/2-95))
				else :
					full_s = 1
					windowSurface.blit(back,(-10,-10))
					windowSurface.blit(FULLSCREEN_MODE_,(SCREEN_WIDTH/2-155,SCREEN_HEIGHT/2-95))
			elif event.key in [K_RETURN , K_KP_ENTER] :
				ok = 0
		if event.type == KEYUP:
			if event.key == K_ESCAPE :
				pygame.quit()
				sys.exit()
	pygame.display.update()
pygame.quit()	
pygame.mixer.pre_init(22050, -16, 2, 4096)
pygame.init()
if full_s :
	windowSurface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.FULLSCREEN,32)
	pygame.display.set_caption("BNO")
else :
	windowSurface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.RESIZABLE,32)
	pygame.display.set_caption("BNO")
	
################################SELECT PLAYERS
namestring1 = 'ichigo/'
namestring2 = 'kenpachi/'
couleur1 = 'normal/'
couleur2 = 'bleu/'
player1_name = ichigo
player2_name = kenpachi
player1 = player1_name.ds()
player2 = player2_name.ds()
###########################################pour test uniquement
######################   LOAD          PLAYER 1 ##############

folder_path1 = '/images/' + namestring1
folder_sounds1 = '/sounds/' + namestring1
for s in player1 :
	for k in range(len(player1[s])) :
		scal1 = 2*player1_name.scale(SOL, s, k)
		player1[s][k][0] = pygame.image.load(os.path.join('data', BNO_path + folder_path1 + couleur1 + s + '/' + str(k) + '.png')).convert_alpha()
		player1[s][k][1] *= scal1
		player1[s][k][2] *= scal1
		player1[s][k][0] = pygame.transform.scale(player1[s][k][0] ,(player1[s][k][1],player1[s][k][2]))
ymax1 = player1_name.ymax()
fight_img1 = pygame.image.load(os.path.join('data', BNO_path + folder_path1  + 'left_fight.png')).convert_alpha()
fight_name1 = pygame.image.load(os.path.join('data', BNO_path + folder_path1  + 'name.png')).convert_alpha()
super_img1 = [[0,0],[0,0]]

super_img1[0][0] = pygame.transform.scale(pygame.image.load(os.path.join('data', BNO_path + folder_path1  + 'fatal_img_l.png')).convert_alpha() ,(SCREEN_WIDTH , SCREEN_HEIGHT))
super_img1[0][1] = pygame.transform.scale(pygame.image.load(os.path.join('data', BNO_path + folder_path1  + 'fatal_img_r.png')).convert_alpha() ,(SCREEN_WIDTH , SCREEN_HEIGHT))
super_img1[1][0] = pygame.transform.scale(pygame.image.load(os.path.join('data', BNO_path + folder_path1  + 'super_img_l.png')).convert_alpha() ,(SCREEN_WIDTH , SCREEN_HEIGHT))
super_img1[1][1] = pygame.transform.scale(pygame.image.load(os.path.join('data', BNO_path + folder_path1  + 'super_img_r.png')).convert_alpha() ,(SCREEN_WIDTH , SCREEN_HEIGHT))
######################   LOAD          PLAYER 2 ##############
folder_path2 = '/images/' + namestring2
folder_sounds2 = '/sounds/' + namestring2

for s in player2 :
	for k in range(len(player2[s])) :
		scal1 = 2*player2_name.scale(SOL, s, k)
		player2[s][k][0] = pygame.image.load(os.path.join('data', BNO_path + folder_path2 + couleur2 + s + '/' + str(k) + '.png')).convert_alpha()
		player2[s][k][1] *= scal1
		player2[s][k][2] *= scal1
		player2[s][k][0] = pygame.transform.scale(player2[s][k][0] ,(player2[s][k][1],player2[s][k][2]))
ymax2 = player2_name.ymax()	
fight_img2 = pygame.image.load(os.path.join('data', BNO_path + folder_path2  + 'right_fight.png')).convert_alpha()
fight_name2 = pygame.image.load(os.path.join('data', BNO_path + folder_path2  + 'name.png')).convert_alpha()
super_img2 = [[0,0],[0,0]]
super_img2[0][0] = pygame.transform.scale(pygame.image.load(os.path.join('data', BNO_path + folder_path2  + 'fatal_img_l.png')).convert_alpha(),(SCREEN_WIDTH , SCREEN_HEIGHT))
super_img2[0][1] = pygame.transform.scale(pygame.image.load(os.path.join('data', BNO_path + folder_path2  + 'fatal_img_r.png')).convert_alpha(),(SCREEN_WIDTH , SCREEN_HEIGHT))
super_img2[1][0] = pygame.transform.scale(pygame.image.load(os.path.join('data', BNO_path + folder_path2  + 'super_img_l.png')).convert_alpha(),(SCREEN_WIDTH , SCREEN_HEIGHT))
super_img2[1][1] = pygame.transform.scale(pygame.image.load(os.path.join('data', BNO_path + folder_path2  + 'super_img_r.png')).convert_alpha(),(SCREEN_WIDTH , SCREEN_HEIGHT))
################################# LOAD BACKGROUND
background_folder_path = '/images/backgrounds/'
back = pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'Bleach.png')).convert_alpha()
back_size = back.get_size()
back = pygame.transform.scale(back,(BACK_IMAGE_LENGTH + 10,back_size[1]))
back_size = back.get_size()
back_upleft_initial = [(SCREEN_WIDTH - back_size[0])/2,SCREEN_HEIGHT - back_size[1]]      #le point ou afficher le back pour q'au ebut les players soient o middle
back_upleft = [(SCREEN_WIDTH - back_size[0])/2,SCREEN_HEIGHT - back_size[1]]
background_img_limit = [(BACK_IMAGE_LENGTH - back_size[0])/2 , -(back_size[0] + BACK_IMAGE_LENGTH )/2 + SCREEN_WIDTH]    #[xmax(left,right),ymax(down,up)]
################################# PAUSE ET AUTRES IMAGES
pause = pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'pause.png')).convert_alpha()
energy = pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'energy.png')).convert_alpha()
live1 = pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'live.png')).convert_alpha()
live2 = pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'live.png')).convert_alpha()
maxi_box =  pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'maxi_box.png')).convert_alpha()
maxi1 = pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'maxi.png')).convert_alpha()
maxi2 = pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'maxi.png')).convert_alpha()
draw = pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'draw.png')).convert_alpha()
fight =  pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'fight.png')).convert_alpha()
ko =  pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'ko.png')).convert_alpha()
maximum = pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'maximum.png')).convert_alpha()
maxs = [0,0,0,0]
maxs[0] = pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'max0.png')).convert_alpha()
maxs[1] = pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'max1.png')).convert_alpha()
maxs[2] = pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'max2.png')).convert_alpha()
maxs[3] = pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'max3.png')).convert_alpha()
perfect = pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'perfect.png')).convert_alpha()
round_img = pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'round.png')).convert_alpha()
rounds = [0,0,0,0,0]
rounds[1] = pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'round1.png')).convert_alpha()
rounds[2] = pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'round2.png')).convert_alpha()
rounds[3] = pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'round3.png')).convert_alpha()
rounds[4] = pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'round4.png')).convert_alpha()
victory = pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'v.png')).convert_alpha()
winner = pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'winner.png')).convert_alpha()
choc_bloc = [0,[0,0],pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'choc_bloc.png')).convert_alpha()]
choc_open = [0,[0,0],pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'choc_open.png')).convert_alpha()]

# CONSTANTES ###########
MAXI_BOX_Y , MAXI_BOX_X1 , MAXI_BOX_X2 = SOL + 9 , (SCREEN_WIDTH - 594)/2 , SCREEN_WIDTH - (SCREEN_WIDTH - 594)/2 - 154
MAX_NUM_Y , MAX_NUM_X1 , MAX_NUM_X2  = MAXI_BOX_Y - 9 , MAXI_BOX_X1 - 26 , MAXI_BOX_X2 + 154
ROUND_IMG_XY = [ (SCREEN_WIDTH - 237)/2 , (SCREEN_HEIGHT - 100)/2] 
ROUNDS_XY = [ROUND_IMG_XY[0] + 173 , (SCREEN_HEIGHT - 100)/2]
FIGHT_XY = [ (SCREEN_WIDTH - 400)/2 , (SCREEN_HEIGHT - 174)/2] 
DRAW_XY = [ (SCREEN_WIDTH - 258)/2 , (SCREEN_HEIGHT - 201)/2] 
KO_XY = [ (SCREEN_WIDTH - 252)/2 , (SCREEN_HEIGHT - 201)/2] 
PERFECT_XY = [ (SCREEN_WIDTH - 261)/2 , (SCREEN_HEIGHT - 70)/2] 
VICTORY_Y ,VICTORY_X1 , VICTORY_X2 = 50 , [(SCREEN_WIDTH - 200)/2 , (SCREEN_WIDTH - 200)/2 + 20] , [(SCREEN_WIDTH + 200)/2 , (SCREEN_WIDTH + 200)/2 - 20] 
WINNER_Y , WINNER_X1 , WINNER_X2 = (SCREEN_HEIGHT - 59)/2 , 20 , SCREEN_WIDTH - 200

# #####################
#infini
infini = pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'infini.png')).convert_alpha()
INFINI_XY = [SCREEN_WIDTH/2 - 20 , 17]
#
ENERGY_MID_GAP = 594
ENERGY_UPLEFT = [(SCREEN_WIDTH - ENERGY_MID_GAP)/2, 10]
FIGHT_IMG1_X = 0
FIGHT_IMG2_X = SCREEN_WIDTH - ENERGY_UPLEFT[0] 
FIGHT_IMG_Y = 15
FIGHT_NAME_Y = 65
NAME_SCALE = 2
LIFE_LENGHT = 260
MAXI_LENGHT = 148
bbbb = fight_name2.get_size()
FIGHT_NAME1_X = 10
FIGHT_NAME2_X = SCREEN_WIDTH - NAME_SCALE * bbbb[0] - 10
#print("@DBG", ENERGY_UPLEFT[0], SCREEN_WIDTH, SCREEN_HEIGHT)
fight_img1 = pygame.transform.scale(fight_img1 ,(ENERGY_UPLEFT[0] , 40))
fight_img2 = pygame.transform.scale(fight_img2 ,(ENERGY_UPLEFT[0] , 40))
fight_name2 = pygame.transform.scale(fight_name2 ,(NAME_SCALE * bbbb[0] , NAME_SCALE * bbbb[1]))
bbbb = fight_name1.get_size()
fight_name1 = pygame.transform.scale(fight_name1 ,(NAME_SCALE * bbbb[0] , NAME_SCALE * bbbb[1]))

live_val1  , live_val2 = LIFE_LENGHT , LIFE_LENGHT                    # qui diminu pendant le combat
maxi_val1 , maxi_val2 = 0 , 0                                         # < MAXI_LENGHT


LIVE1_X = LIFE_LENGHT + 7 + ENERGY_UPLEFT[0] - live_val1             #valeur variable        # + 7 car ce qui entoure live a epaisseur de 7
LIVE2_X =  SCREEN_WIDTH - (LIFE_LENGHT + 7 + ENERGY_UPLEFT[0])                    # + 7 car ce qui entoure live a epaisseur de 7
LIVE_Y = ENERGY_UPLEFT[1] + 15                                                 # 15 est la distance  du haut du cadre de energy a laive (y)
################################ OUTPUT BACKGROUND 
windowSurface.blit(back,back_upleft)

################################ UPDATE
pygame.display.update()
#################################

############################LOAD BACKGROUNDS SOUNDS 
background_sounds_path = '/sounds/backgrounds/'
ko_sound = pygame.mixer.Sound(os.path.join('data', BNO_path + background_sounds_path +'ko.wav'))
rounds_sound = [0,0,0,0,0]
rounds_sound[1] = pygame.mixer.Sound(os.path.join('data', BNO_path + background_sounds_path +'round1.wav'))
rounds_sound[2] = pygame.mixer.Sound(os.path.join('data', BNO_path + background_sounds_path +'round2.wav'))
rounds_sound[3] = pygame.mixer.Sound(os.path.join('data', BNO_path + background_sounds_path +'round3.wav'))
rounds_sound[4] = pygame.mixer.Sound(os.path.join('data', BNO_path + background_sounds_path +'round4.wav'))
fight_sound = pygame.mixer.Sound(os.path.join('data', BNO_path + background_sounds_path +'fight.wav'))
super_sound =  pygame.mixer.Sound(os.path.join('data', BNO_path + background_sounds_path +'super.wav'))
#############################
################################ MAIN LOOP
FPS = 0.11
#FPS = 0.06
ACT_NUM_IMG_MAX = 20                     #LE NBRE D'IMAGE DE L'ACTION LA PLUS LONGUE
KO_TIME = ACT_NUM_IMG_MAX * FPS

# reste ici
QUEUE_ELEM_NUM =8			#nombre d'elements de la queue ( 2e partie de queue1 et 2)
new_match , new_round = 1 , 1
intro = 0
leftkey1,rightkey1,downkey1,upkey1 = K_a,K_d,K_s,K_w
p_main1,g_main1,p_pied1,g_pied1,miss1,pow1 = K_t,K_g,K_y,K_h,K_u,K_j
leftkey2,rightkey2,downkey2,upkey2 = K_RIGHT,K_LEFT,K_DOWN,K_UP
p_main2,g_main2,p_pied2,g_pied2,miss2,pow2 = K_KP4,K_KP1,K_KP5,K_KP2,K_KP6,K_KP3
pl1_active , pl2_active = 0 , 0
active_keyboard1 , active_keyboard2 = 0 , 0
cpu1_active , cpu2_active = 1 , 1
cpu_keyboard1 , cpu_keyboard2 = 0 , 0
vict_num1 , vict_num2 = 0 , 0
bankai1 ,bankai2 = [0,{},1,1] , [0,{},1,1]
main_break_key1 = {'normal':[],'bankai':[]}
main_break_key2 = {'normal':[],'bankai':[]}
players_list = [{'name':0,'small':0,'big':0,'file': kenpachi},{'name':0,'small':0,'big':0 ,'file': ichigo}] 
players_list[0]['name'] =  pygame.image.load(os.path.join('data', BNO_path + '/images/kenpachi/' + 'name_scaled.png')).convert_alpha()            #kenpachi 
players_list[1]['name'] =  pygame.image.load(os.path.join('data', BNO_path + '/images/ichigo/' + 'name_scaled.png')).convert_alpha()            #ichigo
players_list[0]['small'] =  pygame.image.load(os.path.join('data', BNO_path + '/images/kenpachi/' + 'choose_p_small.png')).convert_alpha()            #kenpachi
players_list[1]['small'] =  pygame.image.load(os.path.join('data', BNO_path + '/images/ichigo/' + 'choose_p_small.png')).convert_alpha()            #ichigo
players_list[0]['big'] =  pygame.image.load(os.path.join('data', BNO_path + '/images/kenpachi/' + 'choose_p_big.png')).convert_alpha()            #kenpachi
players_list[1]['big'] =  pygame.image.load(os.path.join('data', BNO_path + '/images/ichigo/' + 'choose_p_big.png')).convert_alpha()            #ichigo
une_ligne = 2                       # nombres d'icone par ligne ds choose player
name_strings = ['kenpachi/' , 'ichigo/']
couleurs = [['normal/','bleu/','vert/','rouge/'],['normal/','bleu/']]
first_left = [ (SCREEN_WIDTH - ( une_ligne * 70 + 16 * (une_ligne - 1) ))/2 , (SCREEN_HEIGHT-( len(players_list) * 50 / une_ligne + 16 * (len(players_list)/une_ligne - 1) ))/2 ]

while True : 
	if new_round :
		win1 , win2 = 1 , 1
		if new_match :
			if not intro :                                           #choisit le joueur
				# #####TRAITE D'ABORD LA FIN DU JEU PRECEDENT 
				if vict_num1 > vict_num2 :
					image1 = pygame.transform.scale(pygame.image.load(os.path.join('data', BNO_path + folder_path1 + 'win_game.png')).convert_alpha() ,(SCREEN_WIDTH , SCREEN_HEIGHT))
					boool = 1
					while boool :
						event_list = pygame.event.get()
						for event in event_list :
							if event.type == QUIT:
								pygame.quit()
								sys.exit()
							if event.type == KEYDOWN or  event.type == KEYUP:
								if event.key == K_ESCAPE :
									pygame.quit()
									sys.exit()
								elif event.key in [p_main1 , p_main2 , g_main1 , g_main2] :
									boool = 0
									vict_num1 , vict_num2 = 0 , 0
						windowSurface.blit(image1,(0,0))
						pygame.display.update()
						
				elif vict_num1 < vict_num2 :
					image2 = pygame.transform.scale(pygame.image.load(os.path.join('data', BNO_path + folder_path2 + 'win_game.png')).convert_alpha() ,(SCREEN_WIDTH , SCREEN_HEIGHT))
					boool = 1
					while boool :
						event_list = pygame.event.get()
						for event in event_list :
							if event.type == QUIT:
								pygame.quit()
								sys.exit()
							if event.type == KEYDOWN or  event.type == KEYUP:
								if event.key == K_ESCAPE :
									pygame.quit()
									sys.exit()
								elif event.key in [p_main1 , p_main2 , g_main1 , g_main2] :
									boool = 0
									vict_num1 , vict_num2 = 0 , 0
						windowSurface.blit(image2,(0,0))
						pygame.display.update()
				else :
					# press start
					image2 = pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'press_start.png')).convert_alpha() 
					boool = 1
					cpu1_active = 1
					cpu2_active = 1
					while boool :
						event_list = pygame.event.get()
						for event in event_list :
							if event.type == QUIT:
								pygame.quit()
								sys.exit()
							if event.type == KEYDOWN or  event.type == KEYUP:
								if event.key == K_ESCAPE :
									pygame.quit()
									sys.exit()
								elif event.key == K_1 :
									boool = 0
									pl1_active = 1
									cpu1_active = 0
								elif event.key == K_2 :
									boool = 0
									pl2_active = 1
									cpu2_active = 0
								elif event.key == K_3 :             #watch computer computer match
									boool = 0
						windowSurface.blit(image2,((SCREEN_WIDTH - 144)/2,(SCREEN_HEIGHT - 40)/2))
						pygame.display.update()
						time.sleep(0.5)
					# ###############
				##############################   CHOOSE PLAYER #####################
					i = 0                     # pour 1
					j = une_ligne - 1         # pour 2
					namestring1 = ''
					namestring2 = ''
					back = pygame.image.load(os.path.join('data', BNO_path + '/images/backgrounds/CHOOSE_BACK.PNG')).convert_alpha()
					while namestring1 == '' or namestring2 == '':
						if pl1_active and cpu2_active and namestring2 == '':
							j = random.choice(range(len(players_list)))
							namestring2 = name_strings[j]
							couleur2 = couleurs[j][1]
							player2_name = players_list[j]['file']
						elif pl2_active and cpu1_active and namestring1 == '':
							i = random.choice(range(len(players_list)))
							namestring1 = name_strings[i]
							couleur1 = couleurs[i][1]
							player1_name = players_list[i]['file']
						event_list = pygame.event.get()
						for event in event_list :
							if event.type == QUIT:
								pygame.quit()
								sys.exit()
							if event.type == KEYDOWN :
								if event.key == K_ESCAPE :
									pygame.quit()
									sys.exit()
								elif event.key == K_1 and not pl1_active :
									pl1_active = 1
									cpu1_active = 0
									namestring1 = ''
								elif event.key == K_2 and not pl2_active :
									pl2_active = 1
									cpu2_active = 0
									namestring2 = ''
								if (pl1_active or not pl2_active) and namestring1 == '' :
									if event.key == p_main1:
										namestring1 = name_strings[i]
										couleur1 = couleurs[i][0]
										player1_name = players_list[i]['file']
									elif event.key == g_main1:
										namestring1 = name_strings[i]
										couleur1 = couleurs[i][1]
										player1_name = players_list[i]['file']
									elif event.key == p_pied1:
										namestring1 = name_strings[i]
										couleur1 = couleurs[i][2%len(couleurs[i])]
										player1_name = players_list[i]['file']
									elif event.key == g_pied1:
										namestring1 = name_strings[i]
										couleur1 = couleurs[i][3%len(couleurs[i])]
										player1_name = players_list[i]['file']
									elif event.key == leftkey1 :
										i = (i-1)%len(players_list)
									elif event.key == rightkey1 :
										i = (i+1)%len(players_list)
									elif event.key == downkey1 :
										i = (i + une_ligne)%len(players_list)
									elif event.key == upkey1 :
										i = (i - une_ligne)%len(players_list)
									if namestring1 == namestring2 and couleur1 == couleur2 :
										if couleurs[i][0] == couleur1 :
											couleur1 = couleurs[i][1]
										else:
											couleur1 = couleurs[i][0]
								if (pl2_active or not pl1_active) and namestring2 == '' :
									if event.key == p_main2:
										namestring2 = name_strings[j]
										couleur2 = couleurs[j][0]
										player2_name = players_list[j]['file']
									elif event.key == g_main2:
										namestring2 = name_strings[j]
										couleur2 = couleurs[j][1]
										player2_name = players_list[j]['file']
									elif event.key == p_pied2:
										namestring2 = name_strings[j]
										couleur2 = couleurs[j][2%len(couleurs[j])]
										player2_name = players_list[j]['file']
									elif event.key == g_pied2:
										namestring2 = name_strings[j]
										couleur2 = couleurs[j][3%len(couleurs[j])]
										player2_name = players_list[j]['file']
									elif event.key == leftkey2 :
										j = (j-1)%len(players_list)
									elif event.key == rightkey2 :
										j = (j+1)%len(players_list)
									elif event.key == downkey2 :
										j = (j + une_ligne)%len(players_list)
									elif event.key == upkey2 :
										j = (j - une_ligne)%len(players_list)
									if namestring2 == namestring1 and couleur2 == couleur1 :
										if couleurs[j][0] == couleur2 :
											couleur2 = couleurs[j][1]
										else:
											couleur2 = couleurs[j][0]
						windowSurface.blit(back,(-10,-10))
						position1 = first_left + []            # +[] pour qy=ue ce ne soit pas reference sur first_left
						for _iter in range (len(players_list)) :
							position1[0] = first_left[0] + 86*(_iter % une_ligne)
							if not _iter % une_ligne and _iter:
								position1[1] +=  66 
							windowSurface.blit(players_list[_iter]['small'],position1)
							if _iter == i :
								if cpu1_active :
									windowSurface.blit(pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'cpu1.png')).convert_alpha(),[0,20])
									if namestring1 == '':
										windowSurface.blit(pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'select_cpu1.png')).convert_alpha(),[position1[0]-8,position1[1]-8])
								else:
									windowSurface.blit(pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'player1.png')).convert_alpha(),[0,20])
									windowSurface.blit(pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'select1.png')).convert_alpha(),[position1[0]-8,position1[1]-8])
							if _iter == j :
								if cpu2_active :
									windowSurface.blit(pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'cpu2.png')).convert_alpha(),[SCREEN_WIDTH - 131 ,20])
									if namestring2 == '':
										windowSurface.blit(pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'select_cpu2.png')).convert_alpha(),[position1[0]-8,position1[1]-8])
								else:
									windowSurface.blit(pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'player2.png')).convert_alpha(),[SCREEN_WIDTH - 131 ,20])
									windowSurface.blit(pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'select2.png')).convert_alpha(),[position1[0]-8,position1[1]-8])
						windowSurface.blit(players_list[i]['big'],(0 , SCREEN_HEIGHT - 250))                  #player 1
						windowSurface.blit(players_list[i]['name'],(0 , SCREEN_HEIGHT - 40)) 
						windowSurface.blit(players_list[j]['big'],(SCREEN_WIDTH - players_list[j]['big'].get_width() , SCREEN_HEIGHT - 250))                 #player 2
						windowSurface.blit(players_list[j]['name'],(SCREEN_WIDTH - players_list[j]['name'].get_width() , SCREEN_HEIGHT - 40)) 
						pygame.display.update()
				####################################################################
				# ############## LOAD PLAYERS##########
					player1 = player1_name.ds()
					player2 = player2_name.ds()
					######################   LOAD          PLAYER 1 ##############
					
					folder_path1 = '/images/' + namestring1
					folder_sounds1 = '/sounds/' + namestring1
					for s in player1 :
						for k in range(len(player1[s])) :
							scal1 = 2*player1_name.scale(SOL, s, k)
							player1[s][k][0] = pygame.image.load(os.path.join('data', BNO_path + folder_path1 + couleur1 + s + '/' + str(k) + '.png')).convert_alpha()
							player1[s][k][1] *= scal1
							player1[s][k][2] *= scal1
							player1[s][k][0] = pygame.transform.scale(player1[s][k][0] ,(player1[s][k][1],player1[s][k][2]))
					ymax1 = player1_name.ymax()
					fight_img1 = pygame.image.load(os.path.join('data', BNO_path + folder_path1  + 'left_fight.png')).convert_alpha()
					fight_name1 = pygame.image.load(os.path.join('data', BNO_path + folder_path1  + 'name.png')).convert_alpha()
					super_img1 = [[0,0],[0,0]]
					
					super_img1[0][0] = pygame.transform.scale(pygame.image.load(os.path.join('data', BNO_path + folder_path1  + 'fatal_img_l.png')).convert_alpha() ,(SCREEN_WIDTH , SCREEN_HEIGHT))
					super_img1[0][1] = pygame.transform.scale(pygame.image.load(os.path.join('data', BNO_path + folder_path1  + 'fatal_img_r.png')).convert_alpha() ,(SCREEN_WIDTH , SCREEN_HEIGHT))
					super_img1[1][0] = pygame.transform.scale(pygame.image.load(os.path.join('data', BNO_path + folder_path1  + 'super_img_l.png')).convert_alpha() ,(SCREEN_WIDTH , SCREEN_HEIGHT))
					super_img1[1][1] = pygame.transform.scale(pygame.image.load(os.path.join('data', BNO_path + folder_path1  + 'super_img_r.png')).convert_alpha() ,(SCREEN_WIDTH , SCREEN_HEIGHT))
				     # sounds
					player1_sound = pygame.mixer.Sound(os.path.join('data', BNO_path + folder_sounds1 +'intro.wav'))
					######################   LOAD          PLAYER 2 ##############
					folder_path2 = '/images/' + namestring2
					folder_sounds2 = '/sounds/' + namestring2
					
					for s in player2 :
						for k in range(len(player2[s])) :
							scal1 = 2*player2_name.scale(SOL, s, k)
							player2[s][k][0] = pygame.image.load(os.path.join('data', BNO_path + folder_path2 + couleur2 + s + '/' + str(k) + '.png')).convert_alpha()
							player2[s][k][1] *= scal1
							player2[s][k][2] *= scal1
							player2[s][k][0] = pygame.transform.scale(player2[s][k][0] ,(player2[s][k][1],player2[s][k][2]))
					ymax2 = player2_name.ymax()	
					fight_img2 = pygame.image.load(os.path.join('data', BNO_path + folder_path2  + 'right_fight.png')).convert_alpha()
					fight_name2 = pygame.image.load(os.path.join('data', BNO_path + folder_path2  + 'name.png')).convert_alpha()
					super_img2 = [[0,0],[0,0]]
					super_img2[0][0] = pygame.transform.scale(pygame.image.load(os.path.join('data', BNO_path + folder_path2  + 'fatal_img_l.png')).convert_alpha(),(SCREEN_WIDTH , SCREEN_HEIGHT))
					super_img2[0][1] = pygame.transform.scale(pygame.image.load(os.path.join('data', BNO_path + folder_path2  + 'fatal_img_r.png')).convert_alpha(),(SCREEN_WIDTH , SCREEN_HEIGHT))
					super_img2[1][0] = pygame.transform.scale(pygame.image.load(os.path.join('data', BNO_path + folder_path2  + 'super_img_l.png')).convert_alpha(),(SCREEN_WIDTH , SCREEN_HEIGHT))
					super_img2[1][1] = pygame.transform.scale(pygame.image.load(os.path.join('data', BNO_path + folder_path2  + 'super_img_r.png')).convert_alpha(),(SCREEN_WIDTH , SCREEN_HEIGHT))
				    # sounds
					player2_sound = pygame.mixer.Sound(os.path.join('data', BNO_path + folder_sounds2 +'intro.wav'))
				    # ###
					#########################################
					bbbb = fight_name2.get_size()
					FIGHT_NAME1_X = 10
					FIGHT_NAME2_X = SCREEN_WIDTH - NAME_SCALE * bbbb[0] - 10
					fight_img1 = pygame.transform.scale(fight_img1 ,(ENERGY_UPLEFT[0] , 40))
					fight_img2 = pygame.transform.scale(fight_img2 ,(ENERGY_UPLEFT[0] , 40))
					fight_name2 = pygame.transform.scale(fight_name2 ,(NAME_SCALE * bbbb[0] , NAME_SCALE * bbbb[1]))
					bbbb = fight_name1.get_size()
					fight_name1 = pygame.transform.scale(fight_name1 ,(NAME_SCALE * bbbb[0] , NAME_SCALE * bbbb[1]))
				# #####################################
				# ##################  LOAD BACK ##############
					back = pygame.image.load(os.path.join('data', BNO_path + background_folder_path + 'Bleach.png')).convert_alpha()
					back = pygame.transform.scale(back,(BACK_IMAGE_LENGTH + 10,back_size[1]))
					windowSurface.blit(back,back_upleft)
					pygame.display.update()
				# ######################################
	#################################
					RIGHT_SPACE = int(round((player1['stance'][0][1] + player2['stance'][0][1])/2))  #c l'abscisse initiale du joueur 2
	#################################
					intro = 1
					back_upleft = [(SCREEN_WIDTH - back_size[0])/2,SCREEN_HEIGHT - back_size[1]]
					index1 ,index2 = 0,0
					key1,key2,cur_key1,cur_key2 = 0,0,0,0                            #intro
					cur_action1 , cur_action2 = player1_name.clavier(key1,cur_key1,index1,0,bankai1[0]),player2_name.clavier(key2,cur_key2,index2,0,bankai2[0])
					player1_sound.play(0, 0 ,0)        #intro
					player2_sound.play(0, 0 ,0)         #intro
			else :
				
				before = time.perf_counter()
				rect2 = player2[cur_action2[0]][cur_action2[1][index2]][1:3]
				position1 = [0,SOL - (cur_action1[3][index1] + player1[cur_action1[0]][cur_action1[1][index1]][2])]
				position2 = [SCREEN_WIDTH-RIGHT_SPACE - (rect2[0] - RIGHT_SPACE) , SOL - (cur_action2[3][index2] + player2[cur_action2[0]][cur_action2[1][index2]][2])]
				image1 =  player1[cur_action1[0]][cur_action1[1][index1]][0]
				image2 =  player2[cur_action2[0]][cur_action2[1][index2]][0]
				windowSurface.blit(back,back_upleft)
				windowSurface.blit(image1,position1)
				windowSurface.blit(pygame.transform.flip(image2,1,0),position2)
				
				index1 += 1
				index2 += 1
				event_list = pygame.event.get() 
				boool = 0
				for event in event_list :
					if event.type == QUIT:
						pygame.quit()
						sys.exit()
					if event.type == KEYDOWN :
						if event.key in [p_main1 , p_main2 , g_main1 , g_main2] :
							boool = 1
							pygame.mixer.music.stop()
				if index1 >= len(cur_action1[2]) or index2 >= len(cur_action2[2]) or boool:
					round_num = 1 
					count_round_fight = 0
					new_match = 0
					intro = 0                                    # ################
					maxi_val1 , maxi_val2 = 0 , 0                                         # < MAXI_LENGHT
					num_maxs1 , num_maxs2  = 3 , 3
					vict_num1 , vict_num2 = 0 , 0
					time.sleep(4 * FPS)
				after = time.perf_counter()
				time_offset = FPS - (after - before)              # 1000 parceque time.perf_counter renvoi float en seconde or time.sleep use milliseconde
				if time_offset < 0.0 :
					time_offset=0.0
				time.sleep(time_offset + FPS)
				pygame.display.flip()
			
		else :
			if count_round_fight == 0 :
				bankai1 ,bankai2 = [0,{},1,1] , [0,{},1,1]
				back_upleft = [(SCREEN_WIDTH - back_size[0])/2,SCREEN_HEIGHT - back_size[1]]
				index1 ,index2 = 0,0
				key1,key2,cur_key1,cur_key2 = 2,2,2,2                            #stance
				cur_action1 , cur_action2 = player1_name.clavier(key1,cur_key1,index1,0,bankai1[0]),player2_name.clavier(key2,cur_key2,index2,0,bankai2[0])
			before = time.perf_counter()
			rect2 = player2[cur_action2[0]][cur_action2[1][index2]][1:3]
			position1 = [0,SOL - (cur_action1[3][index1] + player1[cur_action1[0]][cur_action1[1][index1]][2])]
			position2 = [SCREEN_WIDTH-RIGHT_SPACE - (rect2[0] - RIGHT_SPACE) , SOL - (cur_action2[3][index2] + player2[cur_action2[0]][cur_action2[1][index2]][2])]
			image1 =  player1[cur_action1[0]][cur_action1[1][index1]][0]
			image2 =  player2[cur_action2[0]][cur_action2[1][index2]][0]
			windowSurface.blit(back,back_upleft)
			windowSurface.blit(image1,position1)
			windowSurface.blit(pygame.transform.flip(image2,1,0),position2)
			if count_round_fight <= round(0.5/FPS):
				count_round_fight += 1
			elif count_round_fight <= round(1.8/FPS):
				if count_round_fight == round(0.5/FPS) + 1:
					rounds_sound[round_num].play(0,0,0)
				count_round_fight += 1
				windowSurface.blit(round_img,ROUND_IMG_XY)
				if count_round_fight >= round(1.0/FPS):
					windowSurface.blit(rounds[round_num],ROUNDS_XY)
			elif count_round_fight <= round(2.3/FPS):
				if count_round_fight == round(1.8/FPS) + 1:
					fight_sound.play(0,0,0)
				count_round_fight += 1
				windowSurface.blit(fight,FIGHT_XY)
			else :
				round_num += 1                      #num du round
				count_round_fight = 0               #en bas on ajoute 1 ca devient 0
				# ######### INITIALIZATION
				######  KEYS ###########
				leftkey1,rightkey1,downkey1,upkey1 = K_a,K_d,K_s,K_w
				p_main1,g_main1,p_pied1,g_pied1,miss1,pow1 = K_t,K_g,K_y,K_h,K_u,K_j
				leftkey2,rightkey2,downkey2,upkey2 = K_RIGHT,K_LEFT,K_DOWN,K_UP
				p_main2,g_main2,p_pied2,g_pied2,miss2,pow2 = K_KP4,K_KP1,K_KP5,K_KP2,K_KP6,K_KP3
				#######################
				back_upleft = [(SCREEN_WIDTH - back_size[0])/2,SCREEN_HEIGHT - back_size[1]]
				reach_edge = 0                                # know si on est o bord : 0 non , 1 bord gauche , 2 bord droit
				direction1 ,changedir1 = 1,1                       # -1 :the player look left ; 1: the player look right
				direction2 ,changedir2 =-1,-1
				#index1,index2 = 0,0				# current image in action .ex image 0.png
				key1,key2,cur_key1,cur_key2 = 2,2,2,2 	# cr_key est l'action qui est entraine de looper
				prev_key1,prev_key2 = 2,2
				move1,move2 = player1_name.clavier(key1,cur_key1,index1,0,bankai1[0]),player2_name.clavier(key2,cur_key2,index2,0,bankai2[0])	#stance
				cur_action1 ,cur_action2 = move1 , move2
				position1 = [0,SOL - (cur_action1[3][index1] + player1[cur_action1[0]][cur_action1[1][index1]][2])]
				position_left1 = position1
				position2 = [SCREEN_WIDTH-RIGHT_SPACE,SOL - (cur_action2[3][index2] + player2[cur_action2[0]][cur_action2[1][index2]][2])]
				position_left2 = position2
				rect1 = player1[cur_action1[0]][cur_action1[1][index1]][1:3]
				rect2 = player2[cur_action2[0]][cur_action2[1][index2]][1:3]
				left1,right1,up1,down1,left2,right2,up2,down2 = 0,0,0,0,0,0,0,0			# 0 mean key up ,  1 mean key down
				same_move1,same_move2 = 1,1
				queue1 , queue2 = [0,['','','','','','','','']] , [0,['','','','','','','','']]	#SqQueue ; queue : [position courante #ou inserer , [elements]]
				main_break_key1['normal'] , main_break_key1['bankai']  = player1_name.breaks(), player1_name.breaks_bankai()
				break_key1 = main_break_key1['normal']
				main_break_key2['normal'] , main_break_key2['bankai']  = player2_name.breaks(), player2_name.breaks_bankai()
				break_key2 = main_break_key2['normal']
				prev_base1 , prev_base2 = 0,0		#ce sont les positions de la base de l'image qui vient d'etre display par raport a SOL (cur_action1[3][index1])	
				descend1,descend2 = [0,0,-1],[0,0,-1]
				win1 , win2 = 1 , 1
				live_val1  , live_val2 = LIFE_LENGHT , LIFE_LENGHT                    # qui diminu pendant le combat
				LIVE1_X = LIFE_LENGHT + 7 + ENERGY_UPLEFT[0] - live_val1             #valeur variable
				new_match , new_round = 0 , 0
				bankai1 ,bankai2 = [0,{},1,1] , [0,{},1,1]
				mass1 , mass2 = [0,{}] , [0,{}]	
				touch_mass1 , touch_mass2 = 0 , 0                     # val valeur elevee sur l'energie lorque touche mass
				reachedge_mass1 , reachedge_mass2 = 0 , 0             # vaut 1 si la puissance sort de l'ecran
				hits1 , hits2 = 0 , 0
				
				######## a modifier lor de l'add du CPU
				if pl1_active:
					active_keyboard1 = 1
				if pl2_active:
					active_keyboard2 = 1
				if cpu1_active:
					cpu_keyboard1 = 1
				if cpu2_active:
					cpu_keyboard2 = 1
				#############
				event_list = pygame.event.get()              # vide la liste des events
				# ########################
			after = time.perf_counter()
			time_offset = FPS - (after - before)              # 1000 parceque time.perf_counter renvoi float en seconde or time.sleep use milliseconde
			if time_offset < 0.0 :
				time_offset=0.0
			time.sleep(time_offset)
			pygame.display.flip()
			index1 = (index1 +1) % len(cur_action1[2])
			index2 = (index2 +1) % len(cur_action2[2])
			
		
	else :
		
		###
		#before et after st use pour prendre le temps de calcul et offset le temps de pause pour un fps constant
		###
		before = time.perf_counter()
		queue1[1][queue1[0]] = ''				#pour le cas ou rien n'est presse dc fo mettre des vides
		queue2[1][queue2[0]] = ''				# lettre maj veut dire keydown , min veut dire up
		
		# ################### CPU 1
		if cpu_keyboard1:
			key1 = random.choice(player1_name.computer(player1_name.personality(),num_maxs1,bankai1[0]))                   # 1 for attack 0 for defend
			if functions.test(key1,cur_key1,break_key1,num_maxs1):
				same_move1 = 0
			left1,right1,up1,down1=random.choice([0,1]),random.choice([0,1]),random.choice([0,1]),random.choice([0,1])
			if not same_move1 :
				same_move1 = 1
				mass_aux = player1_name.puissance(key1,mass1,position_left1[0],prev_base1,bankai1[0])
				bankai_aux = player1_name.bankai(key1,bankai1,position_left1[0],prev_base1)
				if mass_aux[0] and bankai_aux[0] : 
					prev_key1 = cur_key1
					cur_key1 = key1 
					prev_action1 = move1
					cur_action1 = player1_name.clavier(key1,prev_key1,index1,prev_base1,bankai1[0])		# cur_key et index c pour l'interception d'air
				# ### sounds	
					player1_sound = pygame.mixer.Sound(os.path.join('data', BNO_path + folder_sounds1 + player1_name.songs(key1)))
					player1_sound.play(0,0,0)
				# ####	
					index1 = -1      # -1 et n on 0 car en bas on ajoute 1 et ca devient 0
					if len(mass1[1]) == 0:
						mass1 = [0,mass_aux[1]]
					if len(bankai1[1]) == 0 and len(bankai_aux[1]) != 0:
						bankai1 = bankai_aux
						if bankai1[1]['type'] == 2 :
							break_key1 = main_break_key1['bankai']
		# ###############
		
		# ################### CPU 2
		if cpu_keyboard2:
			key2 = random.choice(player2_name.computer(player2_name.personality(),num_maxs2,bankai2[0]))                   # 1 for attack 0 for defend
			if functions.test(key2,cur_key2,break_key2,num_maxs2):
				same_move2 = 0
			left2,right2,up2,down2=random.choice([0,1]),random.choice([0,1]),random.choice([0,1]),random.choice([0,1])
			if not same_move2 :
				same_move2 = 1
				mass_aux = player2_name.puissance(key2,mass2,position_left2[0],prev_base2,bankai2[0])
				bankai_aux = player2_name.bankai(key2,bankai2,position_left2[0],prev_base2)
				if mass_aux[0] and bankai_aux[0] :
					prev_key2 = cur_key2
					cur_key2 = key2 
					prev_action2 = move2
					cur_action2 = player2_name.clavier(key2,prev_key2,index2,prev_base2,bankai2[0])		# cur_key et index c pour l'interception d'air
				# #### sounds
					player2_sound = pygame.mixer.Sound(os.path.join('data', BNO_path + folder_sounds2 + player2_name.songs(key2)))
					player2_sound.play(0,0,0)
				# ######
					index2 = -1      # -1 et n on 0 car en bas on ajoute 1 et ca devient 0
					if len(mass2[1]) == 0:
						mass2 = [0,mass_aux[1]]
					if len(bankai2[1]) == 0 and len(bankai_aux[1]) != 0:
						bankai2 = bankai_aux
						if bankai2[1]['type'] == 2 :
							break_key2 = main_break_key2['bankai']
		# ###############
		
		event_list = pygame.event.get()
		if len(event_list)  == 0 :				#cas ou aucun key n'est presse
			queue1[0] = (queue1[0] + 1) % QUEUE_ELEM_NUM	
			queue2[0] = (queue2[0] + 1) % QUEUE_ELEM_NUM	
		for event in event_list :
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
			#PLAYER 1
				if active_keyboard1 :                                 #test si on prend en compte le player1
					if event.key == leftkey1 :
						left1 = 1
						queue1[1][queue1[0]] = 'A'
						queue1[0] = (queue1[0] + 1) % QUEUE_ELEM_NUM
						key1,same_move1 = functions.mouvement([queue1 , QUEUE_ELEM_NUM],[same_move1,cur_key1],break_key1,num_maxs1)
						if key1 < 0 :
							if up1 :
								key1 = 13			#backward_jump
								if functions.test(key1,cur_key1,break_key1,num_maxs1):
									same_move1 = 0
							elif down1 :
								key1 = 9			#crouch
								if functions.test(key1,cur_key1,break_key1,num_maxs1):
									same_move1 = 0
							else :
								key1 = 5			#'walk_back'
								if functions.test(key1,cur_key1,break_key1,num_maxs1):
									same_move1 = 0
					elif  event.key == rightkey1 :
						right1 = 1
						queue1[1][queue1[0]] = 'D'
						queue1[0] = (queue1[0] + 1) % QUEUE_ELEM_NUM
						key1,same_move1 = functions.mouvement([queue1 , QUEUE_ELEM_NUM],[same_move1,cur_key1],break_key1,num_maxs1)
						if key1 < 0 :
							if up1 :
								key1 = 12					#forward jump
								if functions.test(key1,cur_key1,break_key1,num_maxs1):
									same_move1 = 0
							elif down1 :
								key1 = 9					#crouch
								if functions.test(key1,cur_key1,break_key1,num_maxs1):
									same_move1 = 0
							else :
								key1 = 4					#'walk avant'
								if functions.test(key1,cur_key1,break_key1,num_maxs1):
									same_move1 = 0
					elif  event.key == downkey1 :
						down1 = 1
						key1 = 9						#'crouch'
						if functions.test(key1,cur_key1,break_key1,num_maxs1):
									same_move1 = 0
						queue1[1][queue1[0]] = 'S'
						queue1[0] = (queue1[0] + 1) % QUEUE_ELEM_NUM
					elif  event.key == upkey1:
						up1 = 1
						queue1[1][queue1[0]] = 'W'
						queue1[0] = (queue1[0] + 1) % QUEUE_ELEM_NUM
						if not down1 :
							if left1 :
								key1 = 13					#backward jump
								if functions.test(key1,cur_key1,break_key1,num_maxs1):
									same_move1 = 0
							elif right1 :
								key1 = 12					#forward jump
								if functions.test(key1,cur_key1,break_key1,num_maxs1):
									same_move1 = 0
							else :
								key1 = 6					#'jump'
								if functions.test(key1,cur_key1,break_key1,num_maxs1):
									same_move1 = 0
					elif event.key == p_main1 :
						queue1[1][queue1[0]] = 'T'
						queue1[0] = (queue1[0] + 1) % QUEUE_ELEM_NUM
						key1,same_move1 = functions.mouvement([queue1 , QUEUE_ELEM_NUM],[same_move1,cur_key1],break_key1,num_maxs1)
					elif event.key == g_main1 :
						queue1[1][queue1[0]] = 'G'
						queue1[0] = (queue1[0] + 1) % QUEUE_ELEM_NUM
						key1,same_move1 = functions.mouvement([queue1 , QUEUE_ELEM_NUM],[same_move1,cur_key1],break_key1,num_maxs1)
					elif event.key == p_pied1 :
						queue1[1][queue1[0]] = 'Y'
						queue1[0] = (queue1[0] + 1) % QUEUE_ELEM_NUM
						key1,same_move1 = functions.mouvement([queue1 , QUEUE_ELEM_NUM],[same_move1,cur_key1],break_key1,num_maxs1)
					elif event.key == g_pied1 :
						queue1[1][queue1[0]] = 'H'
						queue1[0] = (queue1[0] + 1) % QUEUE_ELEM_NUM
						key1,same_move1 = functions.mouvement([queue1 , QUEUE_ELEM_NUM],[same_move1,cur_key1],break_key1,num_maxs1)
					elif event.key == miss1 :
						queue1[1][queue1[0]] = 'U'
						queue1[0] = (queue1[0] + 1) % QUEUE_ELEM_NUM
						key1,same_move1 = functions.mouvement([queue1 , QUEUE_ELEM_NUM],[same_move1,cur_key1],break_key1,num_maxs1)
					elif event.key == pow1 :
						queue1[1][queue1[0]] = 'J'
						queue1[0] = (queue1[0] + 1) % QUEUE_ELEM_NUM
						key1,same_move1 = functions.mouvement([queue1 , QUEUE_ELEM_NUM],[same_move1,cur_key1],break_key1,num_maxs1)
					else :
						queue1[0] = (queue1[0] + 1) % QUEUE_ELEM_NUM		#cas  ou la touche pressee n'est pas use par le jeu
	
			#PLAYER 2
				if active_keyboard2 :                                 #test si on prend en compte le player2
					if event.key == leftkey2 :
						left2 = 1
						queue2[1][queue2[0]] = 'A'
						queue2[0] = (queue2[0] + 1) % QUEUE_ELEM_NUM
						key2,same_move2 = functions.mouvement([queue2 , QUEUE_ELEM_NUM],[same_move2,cur_key2],break_key2,num_maxs2)
						if key2 < 0 :
							if up2 :
								key2 = 13			#backward_jump
								if functions.test(key2,cur_key2,break_key2,num_maxs2):
									same_move2 = 0
							elif down2 :
								key2 = 9			#crouch
								if functions.test(key2,cur_key2,break_key2,num_maxs2):
									same_move2 = 0
							else :
								key2 = 5			#'walk_back'
								if functions.test(key2,cur_key2,break_key2,num_maxs2):
									same_move2 = 0
					elif  event.key == rightkey2 :
						right2 = 1
						queue2[1][queue2[0]] = 'D'
						queue2[0] = (queue2[0] + 1) % QUEUE_ELEM_NUM
						key2,same_move2 = functions.mouvement([queue2 , QUEUE_ELEM_NUM],[same_move2,cur_key2],break_key2,num_maxs2)
						if key2 < 0 :
							if up2 :
								key2 = 12					#forward jump
								if functions.test(key2,cur_key2,break_key2,num_maxs2):
									same_move2 = 0
							elif down2 :
								key2 = 9					#crouch
								if functions.test(key2,cur_key2,break_key2,num_maxs2):
									same_move2 = 0
							else :
								key2 = 4					#'walk avant'
								if functions.test(key2,cur_key2,break_key2,num_maxs2):
									same_move2 = 0
					elif  event.key == downkey2 :
						down2 = 1
						key2 = 9						#'crouch'
						if functions.test(key2,cur_key2,break_key2,num_maxs2):
									same_move2 = 0
						queue2[1][queue2[0]] = 'S'
						queue2[0] = (queue2[0] + 1) % QUEUE_ELEM_NUM
					elif  event.key == upkey2:
						up2 = 1
						queue2[1][queue2[0]] = 'W'
						queue2[0] = (queue2[0] + 1) % QUEUE_ELEM_NUM
						if not down2 :
							if left2 :
								key2 = 13					#backward jump
								if functions.test(key2,cur_key2,break_key2,num_maxs2):
									same_move2 = 0
							elif right2 :
								key2 = 12					#forward jump
								if functions.test(key2,cur_key2,break_key2,num_maxs2):
									same_move2 = 0
							else :
								key2 = 6					#'jump'
								if functions.test(key2,cur_key2,break_key2,num_maxs2):
									same_move2 = 0
					elif event.key == p_main2 :
						queue2[1][queue2[0]] = 'T'
						queue2[0] = (queue2[0] + 1) % QUEUE_ELEM_NUM
						key2,same_move2 = functions.mouvement([queue2 , QUEUE_ELEM_NUM],[same_move2,cur_key2],break_key2,num_maxs2)
					elif event.key == g_main2 :
						queue2[1][queue2[0]] = 'G'
						queue2[0] = (queue2[0] + 1) % QUEUE_ELEM_NUM
						key2,same_move2 = functions.mouvement([queue2 , QUEUE_ELEM_NUM],[same_move2,cur_key2],break_key2,num_maxs2)
					elif event.key == p_pied2 :
						queue2[1][queue2[0]] = 'Y'
						queue2[0] = (queue2[0] + 1) % QUEUE_ELEM_NUM
						key2,same_move2 = functions.mouvement([queue2 , QUEUE_ELEM_NUM],[same_move2,cur_key2],break_key2,num_maxs2)
					elif event.key == g_pied2 :
						queue2[1][queue2[0]] = 'H'
						queue2[0] = (queue2[0] + 1) % QUEUE_ELEM_NUM
						key2,same_move2 = functions.mouvement([queue2 , QUEUE_ELEM_NUM],[same_move2,cur_key2],break_key2,num_maxs2)
					elif event.key == miss2 :
						queue2[1][queue2[0]] = 'U'
						queue2[0] = (queue2[0] + 1) % QUEUE_ELEM_NUM
						key2,same_move2 = functions.mouvement([queue2 , QUEUE_ELEM_NUM],[same_move2,cur_key2],break_key2,num_maxs2)
					elif event.key == pow2 :
						queue2[1][queue2[0]] = 'J'
						queue2[0] = (queue2[0] + 1) % QUEUE_ELEM_NUM
						key2,same_move2 = functions.mouvement([queue2 , QUEUE_ELEM_NUM],[same_move2,cur_key2],break_key2,num_maxs2)
					else :
						queue2[0] = (queue2[0] + 1) % QUEUE_ELEM_NUM		#cas  ou la touche pressee n'est pas use par le jeu
	
			if event.type == KEYUP:
				if event.key == K_ESCAPE :
					pygame.quit()
					sys.exit()
				if event.key == K_RETURN :		#pause
					windowSurface.blit(pause,(SCREEN_WIDTH/2-65,SCREEN_HEIGHT/2-28))
					pygame.display.update()
					queue1 = [0,['','','','','','','','']]
					queue2 = [0,['','','','','','','','']]
					pause_bool = 1
					while pause_bool :
						for event in pygame.event.get() :
							if event.type == KEYDOWN:
							#player1
								if active_keyboard1 :                                 #test si on prend en compte le player1
									if event.key == leftkey1 :
										left1 = 1
									elif  event.key == rightkey1 :
										right1 = 1
									elif  event.key == downkey1 :
										down1 = 1
									elif  event.key == upkey1:
										up1 = 1
								
							#player2	
								if active_keyboard2 :                                 #test si on prend en compte le player2
									if event.key == leftkey2 :
										left2 = 1
									elif  event.key == rightkey2 :
										right2 = 1
									elif  event.key == downkey2 :
										down2 = 1
									elif  event.key == upkey2:
										up2 = 1
							elif event.type == KEYUP:
								if event.key == K_ESCAPE :
									pygame.quit()
									sys.exit()
								elif event.key == K_RETURN :
									pause_bool = 0
								else:
							#player1
									if active_keyboard1 :                                 #test si on prend en compte le player1
										if event.key == leftkey1 :
											left1 = 0
											block1 = 0
										elif  event.key == rightkey1 :
											right1 = 0
											block1 = 0
										elif  event.key == downkey1 :
											down1 = 0
										elif  event.key == upkey1:
											up1 = 0
							#player2
									if active_keyboard2 :                                 #test si on prend en compte le player2
										if event.key == leftkey2 :
											left2 = 0
											block2 = 0
										elif  event.key == rightkey2 :
											right2 = 0
											block2 = 0
										elif  event.key == downkey2 :
											down2 = 0
										elif  event.key == upkey2:
											up2 = 0
					######### PAUSE ##########
			#PLAYER 1
				if active_keyboard1 :                                 #test si on prend en compte le player1
					if event.key == leftkey1 :
						left1 = 0
						block1 = 0
						queue1[1][queue1[0]] = 'a'
						queue1[0] = (queue1[0] + 1) % QUEUE_ELEM_NUM
						if up1 :
							if right1 :
								key1 = 12		#for jump
							else :
								key1 = 6		#'jump'
							if functions.test(key1,cur_key1,break_key1,num_maxs1):
								same_move1 = 0
						elif down1 :
							key1 = 9		#'crouch'
							if functions.test(key1,cur_key1,break_key1,num_maxs1):
								same_move1 = 0
						elif right1 :
							key1 = 4		#'walk avant'
							if functions.test(key1,cur_key1,break_key1,num_maxs1):
								same_move1 = 0
						elif cur_key1 == 5 :			#walk back
							key1, same_move1 = 2, 0 	#action devient stance
					elif  event.key == rightkey1 :
						right1 = 0
						block1 = 0
						queue1[1][queue1[0]] = 'd'
						queue1[0] = (queue1[0] + 1) % QUEUE_ELEM_NUM
						if up1 :
							if left1 :
								key1 = 13		#back jump
							else :
								key1 = 6				#'jump'
							if functions.test(key1,cur_key1,break_key1,num_maxs1):
								same_move1 = 0
						elif down1 :
							key1 = 9					#'crouch'
							if functions.test(key1,cur_key1,break_key1,num_maxs1):
								same_move1 = 0
						elif left1 :
							key1 = 5		#walk back'
							if functions.test(key1,cur_key1,break_key1,num_maxs1):
								same_move1 = 0
						elif cur_key1 == 4 :			#walk avant
							key1, same_move1 = 2, 0 	#action devient stance
					elif  event.key == downkey1 :
						down1 = 0
						queue1[1][queue1[0]] = 's'
						queue1[0] = (queue1[0] + 1) % QUEUE_ELEM_NUM
					elif  event.key == upkey1 :
						up1 = 0
						queue1[1][queue1[0]] = 'w'
						queue1[0] = (queue1[0] + 1) % QUEUE_ELEM_NUM
						if down1 :
							key1 = 9					#crouch
							if functions.test(key1,cur_key1,break_key1,num_maxs1):
								same_move1 = 0
						elif left1 :
							key1 = 5					#'walk_back'
							if functions.test(key1,cur_key1,break_key1,num_maxs1):
								same_move1 = 0
						elif right1 :		
							key1 = 4					#'walk_avant'
							if functions.test(key1,cur_key1,break_key1,num_maxs1):
								same_move1 = 0
					else :
						queue1[0] = (queue1[0] + 1) % QUEUE_ELEM_NUM		#cas  ou la touche pressee n'est pas use par le jeu
			
			#PLAYER 2
				if active_keyboard2 :                                 #test si on prend en compte le player2
					if event.key == leftkey2 :
						left2 = 0
						block2 = 0
						queue2[1][queue2[0]] = 'a'
						queue2[0] = (queue2[0] + 1) % QUEUE_ELEM_NUM
						if up2 :
							if right2 :
								key2 = 12		#for jump
							else :
								key2 = 6		#'jump'
							if functions.test(key2,cur_key2,break_key2,num_maxs2):
								same_move2 = 0
						elif down2 :
							key2 = 9		#'crouch'
							if functions.test(key2,cur_key2,break_key2,num_maxs2):
								same_move2 = 0
						elif right2 :
							key2 = 4		#'walk avant'
							if functions.test(key2,cur_key2,break_key2,num_maxs2):
								same_move2 = 0
						elif cur_key2 == 5 :			#walk back
							key2, same_move2 = 2, 0 	#action devient stance
					elif  event.key == rightkey2 :
						right2 = 0
						block2 = 0
						queue2[1][queue2[0]] = 'd'
						queue2[0] = (queue2[0] + 1) % QUEUE_ELEM_NUM
						if up2 :
							if left2 :
								key2 = 13		#back jump
							else :
								key2 = 6				#'jump'
							if functions.test(key2,cur_key2,break_key2,num_maxs2):
								same_move2 = 0
						elif down2 :
							key2 = 9					#'crouch'
							if functions.test(key2,cur_key2,break_key2,num_maxs2):
								same_move2 = 0
						elif left2 :
							key2 = 5		#walk back'
							if functions.test(key2,cur_key2,break_key2,num_maxs2):
								same_move2 = 0
						elif cur_key2 == 4 :			#walk avant
							key2, same_move2 = 2, 0 	#action devient stance
					elif  event.key == downkey2 :
						down2 = 0
						queue2[1][queue2[0]] = 's'
						queue2[0] = (queue2[0] + 1) % QUEUE_ELEM_NUM
					elif  event.key == upkey2 :
						up2 = 0
						queue2[1][queue2[0]] = 'w'
						queue2[0] = (queue2[0] + 1) % QUEUE_ELEM_NUM
						if down2 :
							key2 = 9					#crouch
							if functions.test(key2,cur_key2,break_key2,num_maxs2):
								same_move2 = 0
						elif left2 :
							key2 = 5					#'walk_back'
							if functions.test(key2,cur_key2,break_key2,num_maxs2):
								same_move2 = 0
						elif right2 :		
							key2 = 4					#'walk_avant'
							if functions.test(key2,cur_key2,break_key2,num_maxs2):
								same_move2 = 0
					else :
						queue2[0] = (queue2[0] + 1) % QUEUE_ELEM_NUM		#cas  ou la touche pressee n'est pas use par le jeu
				
			
			#player 1
			####@@@@@@##### IMPORTANT : puisque le joueur peut presser lestouch rapidement , ds un mem for on peut avoir 2 event du meme jouer dc fo update 		############# cur_key car sinon on pourait break l'ancien et ca breakerait le new
			if not same_move1 and active_keyboard1:
				same_move1 = 1
				mass_aux = player1_name.puissance(key1,mass1,position_left1[0],prev_base1,bankai1[0])
				bankai_aux = player1_name.bankai(key1,bankai1,position_left1[0],prev_base1)
				if mass_aux[0] and bankai_aux[0] : 
					prev_key1 = cur_key1
					cur_key1 = key1 
					prev_action1 = move1
					cur_action1 = player1_name.clavier(key1,prev_key1,index1,prev_base1,bankai1[0])		# cur_key et index c pour l'interception d'air
				# ### sounds	
					player1_sound = pygame.mixer.Sound(os.path.join('data', BNO_path + folder_sounds1 + player1_name.songs(key1)))
					player1_sound.play(0,0,0)
				# #####
					index1 = -1      # -1 et n on 0 car en bas on ajoute 1 et ca devient 0
					if len(mass1[1]) == 0:
						mass1 = [0,mass_aux[1]]
					if len(bankai1[1]) == 0 and len(bankai_aux[1]) != 0:
						bankai1 = bankai_aux
						if bankai1[1]['type'] == 2 :
							break_key1 = main_break_key1['bankai']
			#player 2
			####@@@@@@##### IMPORTANT : puisque le joueur peut presser lestouch rapidement , ds un mem for on peut avoir 2 event du meme jouer dc fo update 		############# cur_key car sinon on pourait break l'ancien et ca breakerait le new
			if not same_move2 and active_keyboard2:
				same_move2 = 1
				mass_aux = player2_name.puissance(key2,mass2,position_left2[0],prev_base2,bankai2[0])
				bankai_aux = player2_name.bankai(key2,bankai2,position_left2[0],prev_base2)
				if mass_aux[0] and bankai_aux[0] :
					prev_key2 = cur_key2
					cur_key2 = key2 
					prev_action2 = move2
					cur_action2 = player2_name.clavier(key2,prev_key2,index2,prev_base2,bankai2[0])		# cur_key et index c pour l'interception d'air
				# ### sounds	
					player2_sound = pygame.mixer.Sound(os.path.join('data', BNO_path + folder_sounds2 + player2_name.songs(key2)))
					player2_sound.play(0,0,0)
				# #####	
					index2 = -1      # -1 et n on 0 car en bas on ajoute 1 et ca devient 0
					if len(mass2[1]) == 0:
						mass2 = [0,mass_aux[1]]
					if len(bankai2[1]) == 0 and len(bankai_aux[1]) != 0:
						bankai2 = bankai_aux
						if bankai2[1]['type'] == 2 :
							break_key2 = main_break_key2['bankai']
		## END FOR  #####################
	#PLAYER 1		
		if index1 == (len(cur_action1[1]) - 1) :	
			same_move1 = 0
			prev_key1 = cur_key1
			if cur_key1 == 8 :			# run back  alors  on arrette de courrir par derriere
				if left1 :
					key1 = 5		#walk back :on marche par derriere	
				else : 
					key1 = 2		#stance
			#	queue1 = [0,['','','','','','','','']]		#vide la queue
			elif cur_key1 == 7 :
				if right1 :
					key1 = 7		#walk avant :on marche par derriere
					prev_key1 = 4		#pour qu'on recommence a l'image 0	
				else : 
					key1 = 2		#stance
			#	queue1 = [0,['','','','','','','','']]		#vide la queue
			elif cur_key1 >= 23 or cur_key1 == 14 or cur_key1 == 15 :
			#	queue1 = [0,['','','','','','','','']]		#vide la queue
				if down1 :
					key1 = 9			#crouch apres execution d'une piche courbee
					prev_key1 = key1		#pour qu'on affiche juste la 2e image (1.png)
				elif up1 :
					if left1 :
						key1 = 13	#backward jump
					elif right1 :
						key1 = 12	#forward jump
					else :
						key1 = 6	#jump
				elif left1 :
					key1 = 5		#walk back
				elif right1 :
					key1 = 4		#walk avant
				else :
					key1 = 2			#stance apres execution d'une piche 
		#  #### important
			elif cur_key1 in [21,22] :
				if live_val1 == 0 :
					same_move1 = 1
					prev_key1 = cur_key1
					prev_action1 = cur_action1
					[cur_action1 , key1] = [['fall down 2',[player1_name.stay_down()[1][-1],player1_name.stay_down()[1][-1]]  , [1,1] ,[-20,-20] , [0,0]] , 22]
					cur_key1 = key1
					index1 = -1     # -1 et n on 0 car en bas on ajoute 1 et ca devient 0
				else:
					if down1 :
						key1 = 9			#crouch apres execution d'une piche courbee
						prev_key1 = key1		#pour qu'on affiche juste la 2e image (1.png)
					elif up1 :
						if left1 :
							key1 = 13	#backward jump
						elif right1 :
							key1 = 12	#forward jump
						else :
							key1 = 6	#jump
					elif left1 :
						key1 = 5		#walk back
					elif right1 :
						key1 = 4		#walk avant
					else :
						key1 = 2			#stance apres execution d'une piche 
			elif cur_key1 in [18,19,20]:
				if kicking_key2 > 0:
					same_move1 = 1
					prev_key1 = cur_key1
					prev_action1 = cur_action1
					[cur_action1 , key1] = player2_name.trajectoire(kicking_key2,cur_key1,prev_base1,live_val1,index1)		# cur_key et index c pour l'interception d'air
					if hits1 >= 3 :            #pour empecher les enchainements infinis
						hits1 = 0
						for _iter in range (len(cur_action1[2])):
							cur_action1[2][_iter] = 0
					cur_key1 = key1
					index1 = -1     # -1 et n on 0 car en bas on ajoute 1 et ca devient 0
					kicking_key2 = -1
				else:
					if live_val1 == 0 :
						same_move1 = 1
						[cur_action1 , key1] = [player1_name.stay_down() , 22]
						cur_key1 = key1
						index1 = -1     # -1 et n on 0 car en bas on ajoute 1 et ca devient 0
					descend1 = player1_name.descendre(13 , prev_base1,bankai1[0])
					if descend1[0] :
						key1 = descend1[2]		# forward jump 
						move1 = player1_name.clavier(descend1[2],key1,descend1[1],prev_base1,bankai1[0])	#pour que ce soit coe si jump etait avant
					else :
						if down1 :
							key1 = 9			#crouch apres execution d'une piche courbee
							prev_key1 = key1		#pour qu'on affiche juste la 2e image (1.png)
						elif up1 :
							if left1 :
								key1 = 13	#backward jump
							elif right1 :
								key1 = 12	#forward jump
							else :
								key1 = 6	#jump
						elif left1 :
							key1 = 5		#walk back
						elif right1 :
							key1 = 4		#walk avant
						else :
							key1 = 2			#stance apres execution d'une piche 
		# ######
			elif cur_key1 == 11 :		#air dash
				descend1 = player1_name.descendre(12 , prev_base1,bankai1[0])		 
				if right1 :
					same_move1 = 1				#on continu comme si avant c'etait la mem action
					descend1[0] = 1			#on recommence air dash
					descend1[1] = 1			#index rentre a 1 ca il continu juste ,pas 0
					key1,descend1[2] = 11,11	#key prend air dash
					move1 = cur_action1
				elif descend1[0] :
					key1 = descend1[2]		# forward jump 
					move1 = player1_name.clavier(descend1[2],key1,descend1[1],prev_base1,bankai1[0])	#pour que ce soit coe si jump etait avant
				else :
					key1 = 2		#stance
			#	queue1 = [0,['','','','','','','','']]		#vide la queue	
			elif cur_key1 == 1:             # win
				same_move1  = 1 
				move1 = cur_action1
				prev_key1 = cur_key1
				prev_action1 = cur_action1
				[cur_action1 , key1] = [['win',[len(player1['win'])-1,len(player1['win'])-1]  , [1,1] ,[0,0] , [0,0]] , 1]
				cur_key1 = key1
				index1 = -1     # -1 et n on 0 car en bas on ajoute 1 et ca devient 0
			else :
				if down1 :
					key1 = 9		#crouch
				elif up1 :
					if left1 :
						key1 = 13	#backward jump
					elif right1 :
						key1 = 12	#forward jump
					else :
						key1 = 6	#jump
				elif left1 :
					key1 = 5		#walk back
				elif right1 :
					key1 = 4		#walk avant
				else :
					key1 = 2			#stance	
		
		if descend1[0]  :
			same_move1 = 1
			cur_action1 = move1
			index1 = descend1[1]
			descend1[0] = 0
		elif not same_move1 :			# une action est terminee
			same_move1 = 1
			####$$$$$$$$$$
			if direction1 != changedir1 :
				if not (cur_key1==key1 and key1==7):       #pour run on ne se tourne pas si on n'arrette pas de run
					left1,right1 = right1,left1
					direction1 = changedir1		#si le joueur a change de direction alors coe l'action est fini ca prends effet
					leftkey1, rightkey1 = rightkey1, leftkey1	#swap left et right
					if key1 in [4,7,12,14]:
						key1+=1
					elif key1 in [5,8,13,15]:
						key1-=1
			####$$$$$$$$$$
			cur_action1 = player1_name.clavier(key1,cur_key1,1,prev_base1,bankai1[0])		#index 1car plus petite valeur( en fait pas utilise) 
			cur_key1 = key1
			if prev_key1 == cur_key1 :
				index1 = 1%len(cur_action1[2])
			else :
				index1 = 0
		else :
			index1 = index1 + 1
					
	#PLAYER 2
		if index2 == (len(cur_action2[1]) - 1) :	
			same_move2 = 0
			prev_key2 = cur_key2
			if cur_key2 == 8 :			# run back  alors  on arrette de courrir par derriere
				if left2 :
					key2 = 5		#walk back :on marche par derriere	
				else : 
					key2 = 2		#stance
			#	queue2 = [0,['','','','','','','','']]		#vide la queue
			elif cur_key2 == 7 :
				if right2 :
					key2 = 7		#walk avant :on marche par derriere
					prev_key2 = 4		#pour qu'on recommence a l'image 0	
				else : 
					key2 = 2		#stance
			#	queue2 = [0,['','','','','','','','']]		#vide la queue
			elif cur_key2 >= 23 or cur_key2 == 14 or cur_key2 == 15 :
			#	queue2 = [0,['','','','','','','','']]		#vide la queue
				if down2 :
					key2 = 9			#crouch apres execution d'une piche courbee
					prev_key2 = key2		#pour qu'on affiche juste la 2e image (1.png)
				elif up2 :
					if left2 :
						key2 = 13	#backward jump
					elif right2 :
						key2 = 12	#forward jump
					else :
						key2 = 6	#jump
				elif left2 :
					key2 = 5		#walk back
				elif right2 :
					key2 = 4		#walk avant
				else :
					key2 = 2			#stance apres execution d'une piche 
					
			#  #### important
			elif cur_key2 in [21,22] :
				if live_val2 == 0 :
					same_move2 = 1
					prev_key2 = cur_key2
					prev_action2 = cur_action2
					[cur_action2 , key2] = [['fall down 2',[player2_name.stay_down()[1][-1],player2_name.stay_down()[1][-1]]  , [1,1] ,[-20,-20] , [0,0]] , 22]
					cur_key2 = key2
					index2 = -1     # -1 et n on 0 car en bas on ajoute 1 et ca devient 0
				else:
					if down2 :
						key2 = 9			#crouch apres execution d'une piche courbee
						prev_key2 = key2		#pour qu'on affiche juste la 2e image (1.png)
					elif up2 :
						if left2 :
							key2 = 13	#backward jump
						elif right2 :
							key2 = 12	#forward jump
						else :
							key2 = 6	#jump
					elif left2 :
						key2 = 5		#walk back
					elif right2 :
						key2 = 4		#walk avant
					else :
						key2 = 2			#stance apres execution d'une piche 
			elif cur_key2 in [18,19,20]:
				if kicking_key1 > 0:
					same_move2 = 1
					prev_key2 = cur_key2
					prev_action2 = cur_action2
					[cur_action2 , key2] = player1_name.trajectoire(kicking_key1,cur_key2,prev_base2,live_val2,index2)		# cur_key et index c pour l'interception d'air
					if hits2 >= 3 :            #pour empecher les enchainements infinis
						hits2 = 0
						for _iter in range (len(cur_action2[2])):
							cur_action2[2][_iter] = 0
					cur_key2 = key2
					index2 = -1     # -1 et n on 0 car en bas on ajoute 1 et ca devient 0
					kicking_key1 = -1
				else:
					if live_val2 == 0 :
						same_move2 = 1
						[cur_action2 , key2] = [player2_name.stay_down() , 22]
						cur_key2 = key2
						index2 = -1     # -1 et n on 0 car en bas on ajoute 1 et ca devient 0
					descend2 = player2_name.descendre(13 , prev_base2,bankai2[0])
					if descend2[0] :
						key2 = descend2[2]		# forward jump 
						move2 = player2_name.clavier(descend2[2],key2 , descend2[1],prev_base2,bankai2[0])	#pour que ce soit coe si jump etait avant
					else :
						if down2 :
							key2 = 9			#crouch apres execution d'une piche courbee
							prev_key2 = key2		#pour qu'on affiche juste la 2e image (1.png)
						elif up2 :
							if left2 :
								key2 = 13	#backward jump
							elif right2 :
								key2 = 12	#forward jump
							else :
								key2 = 6	#jump
						elif left2 :
							key2 = 5		#walk back
						elif right2 :
							key2 = 4		#walk avant
						else :
							key2 = 2			#stance apres execution d'une piche 
		# ######
		
			elif cur_key2 == 11 :		#air dash
				descend2 = player2_name.descendre(12 , prev_base2,bankai2[0])		 
				if right2 :
					same_move2 = 1				#on continu comme si avant c'etait la mem action
					descend2[0] = 1			#on recommence air dash
					descend2[1] = 1			#index rentre a 1 ca il continu juste ,pas 0
					key2,descend2[2] = 11,11	#key prend air dash
					move2 = cur_action2
				elif descend2[0] :
					key2 = descend2[2]		# forward jump 
					move2 = player2_name.clavier(descend2[2],key2,descend2[1],prev_base2,bankai2[0])	#pour que ce soit coe si jump etait avant
				else :
					key2 = 2		#stance
			#	queue2 = [0,['','','','','','','','']]		#vide la queue	
			elif cur_key2 == 1:
				same_move2  = 1 	
				move2 = cur_action2
				prev_key2 = cur_key2
				prev_action2 = cur_action2
				[cur_action2 , key2] = [['win',[len(player2['win'])-1,len(player2['win'])-1]  , [1,1] ,[0,0] , [0,0]] , 1]
				cur_key2 = key2
				index2 = -1     # -1 et n on 0 car en bas on ajoute 1 et ca devient 0
			else :
				if down2 :
					key2 = 9		#crouch
				elif up2 :
					if left2 :
						key2 = 13	#backward jump
					elif right2 :
						key2 = 12	#forward jump
					else :
						key2 = 6	#jump
				elif left2 :
					key2 = 5		#walk back
				elif right2 :
					key2 = 4		#walk avant
				else :
					key2 = 2			#stance	
					
		if descend2[0]  :
			same_move2 = 1
			cur_action2 = move2
			index2 = descend2[1]
			descend2[0] = 0
		elif not same_move2 :			# une action est terminee
			same_move2 = 1
			####$$$$$$$$$$
			if direction2 != changedir2 :
				if not (cur_key2==key2 and key2==7):       #pour run on ne se tourne pas si on n'arrette pas de run
					left2,right2=right2,left2
					direction2 = changedir2		#si le joueur a change de direction alors coe l'action est fini ca prends effet
					leftkey2, rightkey2 = rightkey2, leftkey2	#swap left et right
					if key2 in [4,7,12,14]:
						key2+=1
					elif key2 in [5,8,13,15]:
						key2-=1
			####$$$$$$$$$$
			cur_action2 = player2_name.clavier(key2,cur_key2,1,prev_base2,bankai2[0])		#index est 1 car plus petite valeur( en fait pas utilise) 
			cur_key2 = key2
			if prev_key2 == cur_key2 :
				index2 = 1%len(cur_action2[2])
			else :
				index2 = 0
		else :
			index2 = index2 + 1
			
		
	#player 1
		### pour GUARD ###
		if abs(cur_action2[2][index2]) > 2 or len(mass2[1]):
			if cur_key1 == 5 :                    #walk back
				cur_action1 = player1_name.clavier(16,5,index1,prev_base1,bankai1[0])
				block1 = 1
			elif cur_key1 == 9 and left1 :
				cur_action1 = player1_name.clavier(17,9,index1,prev_base1,bankai1[0])
				block1 = 2
			else:
				block1 = 0
		else:
			block1 = 0
		###########
	# ############ mass1 ##########
		if len(mass1[1]):
			mass1[1]['index'] += 1
			if mass1[1]['index'] >= mass1[1]['start'] and mass1[1]['index'] <= mass1[1]['end'] :
				mass1[0] = 1
				mass_img1 = player1 [mass1[1]['data'][0]][mass1[1]['data'][1] [mass1[1]['index'] - mass1[1]['start']]] [0]
				mass1[1]['data'][3][mass1[1]['index'] - mass1[1]['start']] = SOL  - mass1[1]['data'][3][mass1[1]['index'] - mass1[1]['start']] - player1[mass1[1]['data'][0]][mass1[1]['data'][1] [mass1[1]['index'] - mass1[1]['start']]][2]
			elif mass1[1]['index'] > mass1[1]['end'] :
				mass1 = [0,{}]

	# ###############################
		image1 =  player1[cur_action1[0]][cur_action1[1][index1]][0]
		dx1 = int(round(cur_action1[4][index1] * bankai1[3])) * direction1
		new_x1 = position1[0] + dx1                      #on multipli par direction pour le deplacement gauche droite
		
		prev_base1 = cur_action1[3][index1]
		position1[1] = SOL - prev_base1 - player1[cur_action1[0]][cur_action1[1][index1]][2]
		dy1 = prev_base1 * (SCREEN_HEIGHT - SOL)/ymax1
		rect_prev1 = rect1
		rect1 = player1[cur_action1[0]][cur_action1[1][index1]][1:3]
		

		
	#player2
		### pour GUARD ###
		if abs(cur_action1[2][index1]) > 2 or len(mass1[1]):             ## car les 2 joueurs ne peuvent pas bloquer o mem moment
			if cur_key2 == 5 :                    #walk back
				cur_action2 = player2_name.clavier(16,5,index2,prev_base2,bankai2[0])
				block2 = 1
			elif cur_key2 == 9 and left2 :
				cur_action2 = player2_name.clavier(17,9,index2,prev_base2,bankai2[0])
				block2 = 2
			else:
				block2 = 0
		else:
			block2 = 0
		###################
	# ############ mass2 ##########
		if len(mass2[1]):
			mass2[1]['index'] += 1
			if mass2[1]['index'] >= mass2[1]['start'] and mass2[1]['index'] <= mass2[1]['end'] :
				mass2[0] = 1
				mass_img2 = player2 [mass2[1]['data'][0]][mass2[1]['data'][1] [mass2[1]['index'] - mass2[1]['start']]] [0]
				mass2[1]['data'][3][mass2[1]['index'] - mass2[1]['start']] = SOL  - mass2[1]['data'][3][mass2[1]['index'] - mass2[1]['start']] - player2[mass2[1]['data'][0]][mass2[1]['data'][1] [mass2[1]['index'] - mass2[1]['start']]][2]
			elif mass2[1]['index'] > mass2[1]['end'] :
				mass2 = [0,{}]

	# ###############################
		image2 =  player2[cur_action2[0]][cur_action2[1][index2]][0]
		dx2 = int(round(cur_action2[4][index2] * bankai2[3]))  * direction2
		new_x2 = position2[0] + dx2                      #on multipli par direction pour le deplacement gauche droite
		
		prev_base2 = cur_action2[3][index2]
		position2[1] = SOL - prev_base2 - player2[cur_action2[0]][cur_action2[1][index2]][2]
		dy2 = prev_base2 * (SCREEN_HEIGHT - SOL)/ymax2
		rect_prev2 = rect2
		rect2 = player2[cur_action2[0]][cur_action2[1][index2]][1:3]
		

		##############    on fait diminuer les maxi si il y'a super #############
		if index1 == 0 :
			[num_maxs1 , super_img_index] = player1_name.super(cur_key1,num_maxs1)
			if super_img_index:
				super_sound.play(0,0,0)
				if direction1 == 1 :
					windowSurface.blit(super_img1[super_img_index-1][0],(0,0))
				else :
					windowSurface.blit(super_img1[super_img_index-1][1],(0,0))
				pygame.display.flip()
				time.sleep(5*FPS)
		if index2 == 0 :
			[num_maxs2 , super_img_index] = player2_name.super(cur_key2,num_maxs2)
			if super_img_index:
				super_sound.play(0,0,0)
				if direction2 == 1 :
					windowSurface.blit(super_img2[super_img_index-1][0],(0,0))
				else :
					windowSurface.blit(super_img2[super_img_index-1][1],(0,0))
				pygame.display.flip()
				time.sleep(5*FPS)
		#############################################################
	# #########
		########### schrool background et display players ###########
		##renew le background (scroll)
		 ### pour y schroll
		back_upleft[1] = back_upleft_initial[1] + (dy1 + dy2)
		position1[1],position2[1] = position1[1]+(dy1 + dy2) , position2[1]+(dy1 + dy2)
		if mass1[0] :
			mass1[1]['data'][3][mass1[1]['index'] - mass1[1]['start']] += (dy1 + dy2)
		if mass2[0] :
			mass2[1]['data'][3][mass2[1]['index'] - mass2[1]['start']] += (dy1 + dy2)
		###
		###teste la collision entre les joueurs
		[[new_x1,position1[1]],[new_x2,position2[1]],[dx1,dx2], same_height] = collision.collision(rect_prev1,position1,rect_prev2,position2,rect1,[new_x1,position1[1]],rect2,[new_x2,position2[1]],cur_key1,cur_key2)
		####
		 ###pour x schroll
		if reach_edge ==1 :         #gauche
			if (new_x1 >=SCREEN_WIDTH/2 and new_x2 >= SCREEN_WIDTH/2) or  new_x1>=SCREEN_WIDTH-RIGHT_SPACE or  new_x2>=SCREEN_WIDTH-RIGHT_SPACE:
				reach_edge = 0
		elif reach_edge ==2 :       #droite
			if (new_x1 <=SCREEN_WIDTH/2 -  RIGHT_SPACE and new_x2 <= SCREEN_WIDTH/2 -  RIGHT_SPACE) or new_x1 <= 0 or new_x2 <= 0 :
				reach_edge = 0
		absciss = back_upleft[0] - (dx1 + dx2)/2
		_b_up_l = back_upleft[0]
		if absciss > background_img_limit[0]  :                # on scholl selement si on n'est pas o bord
			reach_edge = 1                          #left edge       
		if absciss < background_img_limit[1]:
			reach_edge = 2                         #right  edge
		if (not reach_edge) :
			aaaa =  back_upleft[0] - absciss 
			if abs(new_x1 - new_x2) < SCREEN_WIDTH -  RIGHT_SPACE :
				if aaaa > 0:                      #back image va vers la gauche
					if new_x1 - aaaa >=0  and new_x2 - aaaa >=0 :
						back_upleft[0] = absciss
						new_x1,new_x2 = new_x1 - (dx1 + dx2)/2 , new_x2 - (dx1 + dx2)/2
				else :
					if new_x1 - aaaa <= SCREEN_WIDTH - RIGHT_SPACE and new_x2 - aaaa <= SCREEN_WIDTH - RIGHT_SPACE:
						back_upleft[0] = absciss
						new_x1,new_x2 = new_x1 - (dx1 + dx2)/2 , new_x2 - (dx1 + dx2)/2
			else :
				if dx1 == 0 and dx2 != 0 :
					if new_x1 < new_x2:
						aaaa = new_x1
					else :
						aaaa = -( SCREEN_WIDTH - RIGHT_SPACE - new_x1 )
					back_upleft[0] -= aaaa
					new_x1,new_x2 = new_x1 - aaaa , new_x2 - aaaa
				elif dx2 == 0 and dx1 != 0 :
					if new_x2 < new_x1:
						aaaa = new_x2
					else :
						aaaa = -(SCREEN_WIDTH - RIGHT_SPACE - new_x2 )
					back_upleft[0] -= aaaa
					new_x1,new_x2 = new_x1 - aaaa , new_x2 - aaaa
				elif dx1>0 and dx2>0 :
					back_upleft[0] -= min(dx1,dx2)
					new_x1,new_x2 = new_x1 - min(dx1,dx2) , new_x2 - min(dx1,dx2)
				elif dx1<0 and dx2<0:
					back_upleft[0] -= max(dx1,dx2)
					new_x1,new_x2 = new_x1 - max(dx1,dx2) , new_x2 - max(dx1,dx2)
								
		#player1
		if new_x1 > 0 and new_x1 < SCREEN_WIDTH - RIGHT_SPACE  :
			position1[0] = new_x1
		else :
			if new_x1 <= 0 :
				if new_x1 < new_x2 or not same_height:
					position1[0] = 0
				else :
					position1[0] =  collision.DX_CONST
			else :
				if new_x1 > new_x2 or not same_height :
					position1[0] = SCREEN_WIDTH-RIGHT_SPACE 		#on met a la position la plus droite de stance
				else :
					position1[0] = SCREEN_WIDTH-RIGHT_SPACE - collision.DX_CONST
		#player2		
		if new_x2 > 0 and new_x2 < SCREEN_WIDTH - RIGHT_SPACE :
			position2[0] = new_x2
		else :
			if new_x2 <= 0 :
				if new_x2 < new_x1 or not same_height:
					position2[0] = 0
				else :
					position2[0] =  collision.DX_CONST
			else :
				if new_x2 > new_x1 or not same_height:
					position2[0] = SCREEN_WIDTH-RIGHT_SPACE 		#on met a la position la plus droite de stance
				else :
					position2[0] = SCREEN_WIDTH-RIGHT_SPACE - collision.DX_CONST	
		############
		
		
		########### DETECTE COLLISION POUR ATTACK  ########## les fonctions: collision.overlap et player.trajectoire
		#ici c pour equilibrer le cote gauche, pour que sa base soit a droite
		if direction1 < 0:
			position_left1 = [position1[0] - (rect1[0] - RIGHT_SPACE) ,  position1[1]]
		else:
			position_left1 = position1
		if direction2 < 0:
			position_left2 = [position2[0] - (rect2[0] - RIGHT_SPACE) ,  position2[1]]
		else:
			position_left2 = position2
			
	################ Initialisation des x de puissance  ###########
		if mass1[0] :
			if mass1[1]['index'] == mass1[1]['start'] :
				if direction1 == 1 :
					mass1[1]['data'][4][0] += position_left1[0]
				else :
					mass1[1]['data'][4][0] = position_left1[0] + player1[cur_action1[0]][cur_action1[1][index1]][1] - mass1[1]['data'][4][0] - player1[mass1[1]['data'][0]][mass1[1]['data'][1] [mass1[1]['index'] - mass1[1]['start']]][1]
				for _iter in list(range(len(mass1[1]['data'][4])))[1:] :
					mass1[1]['data'][4][_iter] =   mass1[1]['data'][4][_iter - 1] + mass1[1]['data'][4][_iter] * direction1
			mass1[1]['data'][4][mass1[1]['index'] - mass1[1]['start']] +=  back_upleft[0] - _b_up_l
			position_mass1 = [ mass1[1]['data'][4][mass1[1]['index'] - mass1[1]['start']],mass1[1]['data'][3][mass1[1]['index'] - mass1[1]['start']] ]
			rect_mass1 = [ player1[mass1[1]['data'][0]][mass1[1]['data'][1] [mass1[1]['index'] - mass1[1]['start']]][1] , player1[mass1[1]['data'][0]][mass1[1]['data'][1] [mass1[1]['index'] - mass1[1]['start']]][2] ]
			if rect_mass1[0] > SCREEN_WIDTH and rect_mass1[0]  < 0 :
				reachedge_mass1 = 1
			if mass1[1]['index'] == mass1[1]['start'] and mass1[1]['key']!=cur_key1 :
				mass1 = [0,{}]
		if mass2[0] :
			if mass2[1]['index'] == mass2[1]['start'] :
				if direction2 == 1 :
					mass2[1]['data'][4][0] += position_left2[0]
				else :
					mass2[1]['data'][4][0] = position_left2[0] + player2[cur_action2[0]][cur_action2[1][index2]][1] - mass2[1]['data'][4][0] - player2[mass2[1]['data'][0]][mass2[1]['data'][1] [mass2[1]['index'] - mass2[1]['start']]][1]
				for _iter in list(range(len(mass2[1]['data'][4])))[1:] :
					mass2[1]['data'][4][_iter] =  mass2[1]['data'][4][_iter - 1] + mass2[1]['data'][4][_iter] * direction2
			mass2[1]['data'][4][mass2[1]['index'] - mass2[1]['start']] +=  back_upleft[0] - _b_up_l
			position_mass2 = [ mass2[1]['data'][4][mass2[1]['index'] - mass2[1]['start']],mass2[1]['data'][3][mass2[1]['index'] - mass2[1]['start']] ] 
			rect_mass2 = [ player2[mass2[1]['data'][0]][mass2[1]['data'][1] [mass2[1]['index'] - mass2[1]['start']]][1] , player2[mass2[1]['data'][0]][mass2[1]['data'][1] [mass2[1]['index'] - mass2[1]['start']]][2] ]
			if rect_mass2[0] > SCREEN_WIDTH and rect_mass2[0]  < 0 :
				reachedge_mass2 = 1
			if mass2[1]['index'] == mass2[1]['start'] and mass2[1]['key']!=cur_key2 :
				mass2 = [0,{}]
	###############################################################
	   # on traite mass player collision
		if mass1[0] :
			[commun , commun_middle_mass1] = collision.overlap(rect2 , position_left2 , rect_mass1 , position_mass1)
			if commun[0] > MIN_X_AREA and commun[1] > MIN_Y_AREA and cur_action2[2][index2] not in [0,2]:    # cur_action car ne touche pas esquiver ,joueur a terre ...
				touch_mass1 =  mass1[1]['data'][2][mass1[1]['index'] - mass1[1]['start']] 
				if mass1[1]['type'] == 1:
					reachedge_mass1 = 1
			if mass2[0]:
				[commun , commun_middle_mass2] = collision.overlap(rect1 , position_left1 , rect_mass2 , position_mass2)
				if commun[0] > MIN_X_AREA and commun[1] > MIN_Y_AREA and cur_action1[2][index1] not in [0,2]:      # cur_action car ne touche pas esquiver ,joueur a terre ...
					touch_mass2 =  mass2[1]['data'][2][mass2[1]['index'] - mass2[1]['start']] 
					if mass1[1]['type'] == 1:
						reachedge_mass2 = 1
				[commun , commun_middle] = collision.overlap(rect_mass2 , position_mass2 , rect_mass1 , position_mass1)
				if commun[0] > 0 and commun[1] > 0:
					if mass1[1]['type'] == 1  :
						reachedge_mass1 = 1
					if mass2[1]['type'] == 1 :
						reachedge_mass2 = 1		
		elif mass2[0] :
			[commun , commun_middle_mass2] = collision.overlap(rect1 , position_left1 , rect_mass2 , position_mass2)
			if commun[0] > MIN_X_AREA and commun[1] > MIN_Y_AREA and cur_action1[2][index1] not in [0,2]:     # cur_action car ne touche pas esquiver ,joueur a terre ...
				touch_mass2 =  mass2[1]['data'][2][mass2[1]['index'] - mass2[1]['start']] 
				if mass2[1]['type'] == 1:
					reachedge_mass2 = 1
	   # ##########################
		#REMARK
		#  nop(before)        ici on use action 2 pour player 2 strike o 1er if car coe les 2 ne peuvent pas bloquer o mem moment,
		#          dc si le 1 bloc alors on n'entre pas ds le if player 1 strike dc on ne modifie pas cur_action2 ,si 1 ne bloc pas 
		#          corcement on go o if qui ne use pas cur_action2 dc la modification possibl en haut ne pose pas de PB
		cur_action2_aux , index2_aux , cur_key2_aux = cur_action2 , index2 , cur_key2                        #save la valeur pour if abs(cur_action2...)
		cur_action1_aux , index1_aux , cur_key1_aux = cur_action1 , index1 , cur_key1                        #save la valeur pour if abs(cur_action2...)
		[commun , commun_middle] = collision.overlap(rect1 , position_left1 , rect2 , position_left2)
		if commun[0] > MIN_X_AREA and commun[1] > MIN_Y_AREA:                        #il y'a overlap
			if num_maxs1 < 3 :
				maxi_val1 += abs(int(round(cur_action1[2][index1] * bankai1[2]))) / MAXI_CONST 
				if maxi_val1 >= MAXI_LENGHT :
					num_maxs1 += 1
					maxi_val1 -= MAXI_LENGHT
			else :
				maxi_val1 = 0
				
			if num_maxs2 < 3 :
				maxi_val2 += abs(int(round(cur_action2[2][index2] * bankai2[2]))) / MAXI_CONST 
				if maxi_val2 >= MAXI_LENGHT :
					num_maxs2 += 1
					maxi_val2 -= MAXI_LENGHT
			else :
				maxi_val2 = 0
			
			##########################  pour le porter ##############
			pas_porter = 1
			if cur_key1 in [29,33] and right1 and index1 ==0:                   #grande main air et sol
				if abs(cur_action2[2][index2]) in [1 , 2] and not(cur_key2 in [29,33] and right2 and index2 ==0):              #joueur 2 n'ataque pas
					pas_porter = 0
					if cur_key1 == 29:
						key1 = 41
					else:
						key1 = 43
					cur_action1 = player1_name.clavier(key1,cur_key1,index1,prev_base1,bankai1[0])
					cur_key1 = key1
					index1 = 0
					[cur_action2 , key2] = player1_name.trajectoire(cur_key1,cur_key2,prev_base2,live_val2,index2)
					prev_key2 , cur_key2 = cur_key2 , key2
					index2 = -1
					AREA_INIT_VAL_X = player2[cur_action2[0]][cur_action2[1][index2]][1] * PLAYERS_STRENGHT
					AREA_INIT_VAL_Y = player2[cur_action2[0]][cur_action2[1][index2]][2] * PLAYERS_STRENGHT
					live_val2 -= commun[0] * commun[1] * abs(int(round(cur_action1[2][index1] * bankai1[2]))) /(AREA_INIT_VAL_X*AREA_INIT_VAL_Y)
				elif cur_key2 in [29,33] and right2 and index2 ==0:
					pas_porter = 0
					if cur_key1 == 29:
						key1 ,key2 = 41,41
						cur_key1,cur_key2 = key1 ,key2
						cur_action1,cur_action2 = player1_name.throw(0,bankai1[0],prev_base1), player2_name.throw(0,bankai2[0],prev_base2)
					else:
						key1 ,key2 = 43,43
						cur_key1,cur_key2 = key1 ,key2
						cur_action1,cur_action2 = player1_name.throw(1,bankai1[0],prev_base1), player2_name.throw(1,bankai2[0],prev_base2)
			elif cur_key2 in [29,33] and right2 and index2 ==0:                   #grande main air et sol
				if abs(cur_action1[2][index1]) in [1 , 2] :              #joueur 1 n'ataque pas
					pas_porter = 0
					if cur_key2 == 29:
						key2 = 41
					else:
						key2 = 43
					cur_action2 = player2_name.clavier(key2,cur_key2,index2,prev_base2,bankai2[0])
					cur_key2 = key2
					index2 = 0
					[cur_action1 , key1] = player2_name.trajectoire(cur_key2,cur_key1,prev_base1,live_val1,index1)
					prev_key1 , cur_key1 = cur_key1 , key1
					index1 = -1
					AREA_INIT_VAL_X = player1[cur_action1[0]][cur_action1[1][index1]][1] * PLAYERS_STRENGHT
					AREA_INIT_VAL_Y = player1[cur_action1[0]][cur_action1[1][index1]][2] * PLAYERS_STRENGHT
					lll= commun[0] * commun[1] * abs(int(round(cur_action2[2][index2] * bankai2[2]))) /(AREA_INIT_VAL_X*AREA_INIT_VAL_Y)
					live_val1 -=lll
					LIVE1_X += lll
			########################################################
			if pas_porter :
				
				if abs(cur_action1[2][index1]) > 2 and cur_key2 not in [14,15,42,44] and  cur_action2[2][index2] not in [0,2]:                    #player 1 strike
					kicking_key1 = cur_key1
					AREA_INIT_VAL_X = player2[cur_action2[0]][cur_action2[1][index2]][1] * PLAYERS_STRENGHT
					AREA_INIT_VAL_Y = player2[cur_action2[0]][cur_action2[1][index2]][2] * PLAYERS_STRENGHT
					if (cur_action1[2][index1] * cur_action2[2][index2] > 0 or len(cur_action1_aux) == 6) and block2:
						live_val2 -= commun[0] * commun[1] * abs(int(round(cur_action1[2][index1] * bankai1[2]))) / (BLOCK_RATIO *AREA_INIT_VAL_X*AREA_INIT_VAL_Y)
						choc_bloc[0:2] = [1,[commun_middle[0]-75,commun_middle[1]-70]]
					else:
						if cur_key2 in [21,22]:   #a ete intercepte sans touch le sol
							hits2 += 1 
						choc_open[0:2] = [1,[commun_middle[0]-95,commun_middle[1]-100]]
						live_val2 -= commun[0] * commun[1] * abs(int(round(cur_action1[2][index1] * bankai1[2]))) /(AREA_INIT_VAL_X*AREA_INIT_VAL_Y)
						if cur_action2[2][index2] < 0:
							key2 = 20               #damage down
						elif cur_action1[2][index1] <0:
							key2 = 19               #damage updown  
						else:
							key2 = 18                #damage upup
						prev_action2 = cur_action2
						cur_action2 = player2_name.clavier(key2,cur_key2,index2,prev_base2,bankai2[0])
						prev_key2 , cur_key2 = cur_key2 , key2
						index2 = -1
				if abs(cur_action2_aux[2][index2_aux]) > 2 and cur_key1 not in [14,15,42,44] and  cur_action1[2][index1] not in [0,2]:                  #player 2 strike
					kicking_key2 = cur_key2_aux
					AREA_INIT_VAL_X = player1[cur_action1[0]][cur_action1[1][index1]][1] * PLAYERS_STRENGHT
					AREA_INIT_VAL_Y = player1[cur_action1[0]][cur_action1[1][index1]][2] * PLAYERS_STRENGHT
					if (cur_action2_aux[2][index2_aux] * cur_action1[2][index1] > 0 or len(cur_action2_aux) == 6) and block1:
						lll= commun[0] * commun[1] * abs(int(round(cur_action2_aux[2][index2_aux] * bankai2[2]))) / (BLOCK_RATIO *AREA_INIT_VAL_X*AREA_INIT_VAL_Y)
						live_val1 -= lll
						LIVE1_X += lll
						choc_bloc[0:2] = [1,[commun_middle[0]-75,commun_middle[1]-70]]
					else:
						if cur_key1 in [21,22]:   #a ete intercepte sans touch le sol
							hits1 += 1
						choc_open[0:2] = [1,[commun_middle[0]-95,commun_middle[1]-100]]
						lll= commun[0] * commun[1] * abs(int(round(cur_action2_aux[2][index2_aux] * bankai2[2]))) /(AREA_INIT_VAL_X*AREA_INIT_VAL_Y)
						live_val1 -=lll
						LIVE1_X += lll
						if cur_action1[2][index1] < 0:
							key1 = 20               #damage down
						elif cur_action1[2][index1] <0:
							key1 = 19               #damage updown  
						else:
							key1 = 18                #damage upup
						prev_action1 = cur_action1
						cur_action1 = player1_name.clavier(key1,cur_key1,index1,prev_base1,bankai1[0])
						prev_key1 , cur_key1 = cur_key1 , key1
						index1 = -1
					
		##############################################################	
		# on remove l'energie si il y'a playe mas collision
		if touch_mass1 :
			if num_maxs1 < 3 :
				maxi_val1 += abs(int(round(touch_mass1 * bankai1[2]))) / MAXI_CONST 
				if maxi_val1 >= MAXI_LENGHT :
					num_maxs1 += 1
					maxi_val1 -= MAXI_LENGHT
			else :
				maxi_val1 = 0
			kicking_key1 = mass1[1]['key']
			if  block2:
				live_val2 -=  abs(int(round(touch_mass1 * bankai1[2]))) / BLOCK_RATIO 
				choc_bloc[0:2] = [1,[commun_middle_mass1[0]-75,commun_middle_mass1[1]-70]]
			else:
				choc_open[0:2] = [1,[commun_middle_mass1[0]-95,commun_middle_mass1[1]-100]]
				live_val2 -=  abs(int(round(touch_mass1 * bankai1[2]))) 
				if cur_action2_aux[2][index2_aux] < 0:
					key2 = 20               #damage down
				else:
					key2 = 18                #damage upup
				prev_action2 = cur_action2_aux
				cur_action2 = player2_name.clavier(key2,cur_key2_aux,index2_aux,prev_base2,bankai2[0])
				prev_key2 , cur_key2 = cur_key2_aux , key2
				index2 = -1
			touch_mass1 = 0
		if touch_mass2 :
			if num_maxs2 < 3 :
				maxi_val2 += abs(int(round(touch_mass2 * bankai2[2]))) / MAXI_CONST 
				if maxi_val2 >= MAXI_LENGHT :
					num_maxs2 += 1
					maxi_val2 -= MAXI_LENGHT
			else :
				maxi_val2 = 0
			kicking_key2 = mass2[1]['key']
			if  block1:
				lll=  abs(int(round(touch_mass2 * bankai2[2]))) / BLOCK_RATIO 
				live_val1 -= lll
				LIVE1_X += lll
				choc_bloc[0:2] = [1,[commun_middle_mass2[0]-75,commun_middle_mass2[1]-70]]
			else:
				choc_open[0:2] = [1,[commun_middle_mass2[0]-95,commun_middle_mass2[1]-100]]
				lll= abs(int(round(touch_mass2 * bankai2[2])))
				live_val1 -=lll
				LIVE1_X += lll
				if cur_action1_aux[2][index1_aux] < 0:
					key1 = 20               #damage down
				else:
					key1 = 18                #damage upup
				prev_action1 = cur_action1_aux
				cur_action1 = player1_name.clavier(key1,cur_key1_aux,index1_aux,prev_base1,bankai1[0])
				prev_key1 , cur_key1 = cur_key1_aux , key1
				index1 = -1
			touch_mass2 = 0
		##############   SCALE LIVE ###########
		if live_val1 <=0 :
			live_val1 = 0 
			win1 = 0
			if block1 :                    # pour le cas ou il perd en bloquant
				cur_key1 = 18
		if live_val2 <=0 :
			live_val2 = 0 
			win2 = 0
			if block2 :                      # pour le cas ou il perd en bloquant
				cur_key2 = 18
		###############
		
		##########     BLIT      ################
		windowSurface.blit(back,back_upleft)
		#player 1
		if direction1 == 1 :
			windowSurface.blit(image1,(position_left1[0],position_left1[1]))
		else :
			windowSurface.blit(pygame.transform.flip(image1,1,0),(position_left1[0],position_left1[1]))
		
		#plater 2
		if direction2 == 1 :
			windowSurface.blit(image2,(position_left2[0],position_left2[1]))
		else :
			windowSurface.blit(pygame.transform.flip(image2,1,0),(position_left2[0],position_left2[1]))
			
		#bankai
		if bankai1[0]:
			if bankai1[1]['type']==1:
				for _iter in range(len(bankai1[1]['index'])) :
					bankai_img = player1[bankai1[1]['data'][0]][bankai1[1]['data'][1][bankai1[1]['index'][_iter]]][0]
					bankai_x = rect1[0] * bankai1[1]['x'][_iter]/100 + position_left1[0]
					bankai_y = rect1[1] * bankai1[1]['y'][_iter]/100 + position_left1[1]
					windowSurface.blit(bankai_img,(bankai_x,bankai_y))
					bankai1[1]['index'][_iter] = (bankai1[1]['index'][_iter] + 1)% len(bankai1[1]['data'][1])
				bankai1[1]['count'] -= 1
				if bankai1[1]['count'] <=0 :
					bankai1 = [0,{},1,1]
			elif bankai1[1]['type']==2 :
				bankai1[1]['count'] -= 1
				if bankai1[1]['count'] <=0 :
					key1 = 55
					prev_action1 = cur_action1
					cur_action1 = player1_name.clavier(key1,cur_key1,index1,prev_base1,bankai1[0])
					prev_key1,cur_key1 = cur_key1,key1
					bankai1 = [0,{},1,1] 
					break_key1 = main_break_key1['normal']
		if bankai2[0]:
			if bankai2[1]['type']==1:
				for _iter in range(len(bankai2[1]['index'])) :
					bankai_img = player2[bankai2[1]['data'][0]][bankai2[1]['data'][1][bankai2[1]['index'][_iter]]][0]
					bankai_x = rect2[0] * bankai2[1]['x'][_iter]/100 + position_left2[0] 
					bankai_y = rect2[1] * bankai2[1]['y'][_iter]/100 + position_left2[1]
					windowSurface.blit(bankai_img,(bankai_x,bankai_y))
					bankai2[1]['index'][_iter] = (bankai2[1]['index'][_iter] + 1)% len(bankai2[1]['data'][1])
				bankai2[1]['count'] -= 1
				if bankai2[1]['count'] <=0 :
					bankai2 = [0,{},1,1]
			elif bankai2[1]['type']==2 :
				bankai2[1]['count'] -= 1
				if bankai2[1]['count'] <=0 :
					key2 = 55
					prev_action2 = cur_action2
					cur_action2 = player2_name.clavier(key2,cur_key2,index2,prev_base2,bankai2[0])
					prev_key2,cur_key2 = cur_key1,key2
					bankai2 = [0,{},1,1] 
					break_key2 = main_break_key2['normal']
		#mass 
		if mass1[0] :
			if direction1 == 1 :
				windowSurface.blit(mass_img1,position_mass1)
			else :
				windowSurface.blit(pygame.transform.flip(mass_img1,1,0),position_mass1)
			if reachedge_mass1 :
				mass1 = [0,{}]
				reachedge_mass1 = 0
			else:
				mass1[0] = 0
		if mass2[0] :
			if direction2 == 1 :
				windowSurface.blit(mass_img2,position_mass2)
			else :
				windowSurface.blit(pygame.transform.flip(mass_img2,1,0),position_mass2)
			if reachedge_mass2 :
				mass1 = [0,{}]
				reachedge_mass2 = 0
			else :
				mass2[0] = 0
				
		# choc
		if choc_open[0] :
			windowSurface.blit(choc_open[2],choc_open[1])
			choc_open[0] = 0
		elif choc_bloc[0] :
			windowSurface.blit(choc_bloc[2],choc_bloc[1])
			choc_bloc[0] = 0
			
		## energy
		windowSurface.blit(energy,ENERGY_UPLEFT)
		windowSurface.blit(infini,INFINI_XY)
		windowSurface.blit(fight_img1,(FIGHT_IMG1_X,FIGHT_IMG_Y))
		windowSurface.blit(fight_img2,(FIGHT_IMG2_X,FIGHT_IMG_Y))
		windowSurface.blit(fight_name1,(FIGHT_NAME1_X,FIGHT_NAME_Y))
		windowSurface.blit(fight_name2,(FIGHT_NAME2_X,FIGHT_NAME_Y))
		windowSurface.blit(pygame.transform.scale(live1 ,(live_val1 , 15)),(LIVE1_X,LIVE_Y))
		windowSurface.blit(pygame.transform.scale(live2 ,(live_val2 , 15)),(LIVE2_X,LIVE_Y))
		windowSurface.blit(maxs[num_maxs1],(MAX_NUM_X1 , MAX_NUM_Y))
		windowSurface.blit(maxs[num_maxs2],(MAX_NUM_X2 , MAX_NUM_Y))	
		if num_maxs1 == 3 :
			windowSurface.blit(maximum,(MAXI_BOX_X1 , MAXI_BOX_Y))
		else :
			windowSurface.blit(maxi_box,(MAXI_BOX_X1 , MAXI_BOX_Y))
			windowSurface.blit(pygame.transform.scale(maxi1 ,(maxi_val1 , 10)),(MAXI_BOX_X1 + 151 - maxi_val1 , MAXI_BOX_Y + 3))
			
		if num_maxs2 == 3 :
			windowSurface.blit(maximum,(MAXI_BOX_X2 , MAXI_BOX_Y))
		else :
			windowSurface.blit(maxi_box,(MAXI_BOX_X2 , MAXI_BOX_Y))
			windowSurface.blit(pygame.transform.scale(maxi2 ,(maxi_val2 , 10)),(MAXI_BOX_X2 + 3 , MAXI_BOX_Y + 3))
		i=0
		while i < vict_num1:
			windowSurface.blit(victory,(VICTORY_X1[i],VICTORY_Y ))
			i +=1
		i=0
		while i < vict_num2:
			windowSurface.blit(victory,(VICTORY_X2[i],VICTORY_Y ))
			i +=1
		
		# #### TRAITE LA FIN DU ROUND ########
		if not(win1 and win2):	
			count_round_fight += 1
			if count_round_fight <= ACT_NUM_IMG_MAX :
				if not(win1 or win2) :
					windowSurface.blit(draw,DRAW_XY)
					if  count_round_fight == ACT_NUM_IMG_MAX:                  #match over
						count_round_fight = 0
						if round_num == 4 :
							new_match , new_round = 1 , 1
						else:
							new_round = 1
				else :
					windowSurface.blit(ko,KO_XY)
					if count_round_fight == 2 :
						ko_sound.play(0,0,0)
						time.sleep(5 * FPS)
						
			elif win1 :
				if count_round_fight == ACT_NUM_IMG_MAX + 1 :
					vict_num1 += 1
					active_keyboard1 , active_keyboard2 = 0 , 0                         #desactive les claviers
					cpu_keyboard1 , cpu_keyboard2 = 0 , 0
					left1,right1,up1,down1,left2,right2,up2,down2 = 0,0,0,0,0,0,0,0	
					prev_action1 ,prev_key1 = cur_action1, cur_key1
					cur_action1  = player1_name.clavier(1,1,0,0,0)
					cur_key1, key1 = 1 , 1
					index1 = 0
				if count_round_fight <= ACT_NUM_IMG_MAX + round(1.0/FPS) :
					windowSurface.blit(winner,(WINNER_X1,WINNER_Y))
				elif live_val1 == LIFE_LENGHT and count_round_fight <= ACT_NUM_IMG_MAX + round(2.0/FPS) :
					windowSurface.blit(perfect,PERFECT_XY)
				elif vict_num1 == 2 :
					new_match , new_round = 1 , 1
					count_round_fight = 0
				else :
					new_round = 1
					count_round_fight = 0
				i=0
				while i < vict_num1:
					windowSurface.blit(victory,(VICTORY_X1[i],VICTORY_Y ))
					i +=1
			elif win2 :
				if count_round_fight == ACT_NUM_IMG_MAX + 1 :
					vict_num2 += 1
					active_keyboard1 , active_keyboard2 = 0 , 0
					cpu_keyboard1 , cpu_keyboard2 = 0 , 0
					left1,right1,up1,down1,left2,right2,up2,down2 = 0,0,0,0,0,0,0,0	
					prev_action2 ,prev_key2 = cur_action2, cur_key2
					cur_action2  = player2_name.clavier(1,1,0,0,0)
					cur_key2, key2 = 1 , 1
					index2 = 0
				if count_round_fight <= ACT_NUM_IMG_MAX + round(1.0/FPS) :
					windowSurface.blit(winner,(WINNER_X2,WINNER_Y))
				elif live_val2 == LIFE_LENGHT and count_round_fight <= ACT_NUM_IMG_MAX + round(2.0/FPS) :
					windowSurface.blit(perfect,PERFECT_XY)
				elif  vict_num2 == 2:
					new_match , new_round = 1 , 1
					count_round_fight = 0
				else :
					new_round = 1
					count_round_fight = 0
				i=0
				while i < vict_num2:
					windowSurface.blit(victory,(VICTORY_X2[i],VICTORY_Y ))
					i +=1

		################
		
		
		
		#######   a uncomment apres ajout du player 2
		# fait que les joueurs se tournent
		if position1[0] < position2[0] :
			changedir1,changedir2 = 1,-1
		else :
			changedir1,changedir2 = -1,1 	
		if cur_key1 <=5 :	                                       #pour stance et walk si change direction c directement
			if changedir1 != direction1 :	
				same_move1 =  0  
		if cur_key2 <=5 :	                                        #pour stance et walk si change direction c directement
			if changedir2 != direction2 :
				same_move2 = 0 
		#########################################
	
	
		################################## FPS
		after = time.perf_counter()
		time_offset = FPS - (after - before)              # 1000 parceque time.perf_counter renvoi float en seconde or time.sleep use milliseconde
		if time_offset < 0.0 :
			time_offset=0.0
		time.sleep(time_offset)
		
		################################ UPDATE
		pygame.display.flip()
