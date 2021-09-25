#using pygame
FACT_PUSH  = 2     
DX_CONST = 50

def overlap(rect1,topleft1,rect2,topleft2) :	
    #on revoie overlap x et y (dc si overlap les valeurs st positives sinon elle st negatives)
    if topleft1[0] <= topleft2[0] :
        if topleft1[1] <= topleft2[1] :
            commun = [(rect1[0]  + topleft1[0] - topleft2[0]) , (rect1[1]  + topleft1[1] - topleft2[1])]
            commun_middle = [topleft2[0] + commun[0]/2 , topleft2[1] + commun[1]/2]
        else :
            commun = [(rect1[0]  + topleft1[0] - topleft2[0]) , (rect2[1]  + topleft2[1] - topleft1[1])]
            commun_middle = [topleft2[0] + commun[0]/2 , topleft1[1] + commun[1]/2]
    else :
        if topleft1[1] <= topleft2[1] :
            commun = [(rect2[0]  + topleft2[0] - topleft1[0]) , (rect1[1]  + topleft1[1] - topleft2[1])]
            commun_middle = [topleft1[0] + commun[0]/2 , topleft2[1] + commun[1]/2]
        else :
            commun = [(rect2[0]  + topleft2[0] - topleft1[0]) , (rect2[1]  + topleft2[1] - topleft1[1])]
            commun_middle = [topleft1[0] + commun[0]/2 , topleft1[1] + commun[1]/2]
    return [commun , commun_middle]


def collision(rect_prev1,topleft_prev1,rect_prev2,topleft_prev2,rect1,topleft1,rect2,topleft2,cur_key1,cur_key2):
          #return final topleft 1 et final topleft 2
    same_height = 0
    dx1 = topleft1[0] - topleft_prev1[0]
    dx2 = topleft2[0] - topleft_prev2[0]
    if topleft_prev2[0] > topleft_prev1[0] :
        dx = topleft_prev2[0] - topleft_prev1[0] - DX_CONST
    else:
        dx = topleft_prev1[0] - topleft_prev2[0] - DX_CONST
     ####   
    if ((topleft_prev1[0] < topleft_prev2[0] and topleft2[0] < topleft1[0]) or (topleft_prev1[0] > topleft_prev2[0] and topleft2[0] > topleft1[0])) and not cur_key1 in [14,15,42,44] and not cur_key2 in [14,15,42,44]:
        if topleft_prev1[1] < topleft_prev2[1] or topleft1[1] < topleft2[1] :
            if abs(topleft_prev2[1]+rect_prev2[1] - (topleft_prev1[1]+rect_prev1[1])) <= rect1[1]/2 and abs(topleft2[1]+rect2[1] - (topleft1[1]+rect1[1])) <= rect1[1]/2:
                same_height = 1
                if dx >= DX_CONST :                                                          #les 2 joueurs se collent
                    dx1 , dx2 = dx*dx1 /(abs(dx1) + abs(dx2)) , dx*dx2 /(abs(dx1) + abs(dx2))                     #regle de 3
                else :                                                                #un joueur pousse l'autre ou pas de mouv
                    dx1 , dx2 = (dx1 + dx2)/ FACT_PUSH , (dx1 + dx2)/ FACT_PUSH
                topleft1[0] = topleft_prev1[0] + dx1                      #regle de 3
                topleft2[0] = topleft_prev2[0] + dx2
            return [topleft1 , topleft2,[dx1,dx2], same_height]                                          #il y'a stop a faire
        else:                                           #if topleft_prev1[1] >= topleft_prev2[1]  and topleft1[1] >= topleft2[1]:
            if abs(topleft_prev1[1]+rect_prev1[1] - (topleft_prev2[1]+rect_prev2[1])) <= rect2[1]/2 and abs(topleft1[1]+rect1[1] - (topleft2[1]+rect2[1])) <= rect2[1]/2:
                same_height = 1
                if dx >= DX_CONST :                                                          #les 2 joueurs se collent
                    dx1 , dx2 = dx*dx1 /(abs(dx1) + abs(dx2)) , dx*dx2 /(abs(dx1) + abs(dx2))                     #regle de 3
                else :                                                                #un jour pousse l'autre ou pas de mouv
                    dx1 , dx2 = (dx1 + dx2)/ FACT_PUSH , (dx1 + dx2)/ FACT_PUSH
                topleft1[0] = topleft_prev1[0] + dx1                      #regle de 3
                topleft2[0] = topleft_prev2[0] + dx2
            return [topleft1 , topleft2,[dx1,dx2], same_height]  
    elif abs(topleft2[0] - topleft1[0]) <=  DX_CONST and not cur_key1 in [14,15,42,44] and not cur_key2 in [14,15,42,44]:               # cas ou les image st superpose ou tres proche on decale
        if topleft_prev1[1] < topleft_prev2[1] or topleft1[1] < topleft2[1] :
            if abs(topleft_prev2[1]+rect_prev2[1] - (topleft_prev1[1]+rect_prev1[1])) <= rect1[1]/2 and abs(topleft2[1]+rect2[1] - (topleft1[1]+rect1[1])) <= rect1[1]/2:
                same_height = 1
                if topleft_prev1[0] < topleft_prev2[0] :
                    topleft1[0] -= (DX_CONST - abs(topleft2[0] - topleft1[0]))/2
                    dx1 -= (DX_CONST - abs(topleft2[0] - topleft1[0]))/2
                    topleft2[0] += (DX_CONST - abs(topleft2[0] - topleft1[0]))/2
                    dx2 += (DX_CONST - abs(topleft2[0] - topleft1[0]))/2
                else :
                    topleft2[0] -= (DX_CONST - abs(topleft2[0] - topleft1[0]))/2
                    dx2 -= (DX_CONST - abs(topleft2[0] - topleft1[0]))/2
                    topleft1[0] += (DX_CONST - abs(topleft2[0] - topleft1[0]))/2
                    dx1 += (DX_CONST - abs(topleft2[0] - topleft1[0]))/2
            return [topleft1 , topleft2 , [dx1,dx2] , same_height]
        else:                                           #if topleft_prev1[1] >= topleft_prev2[1]  and topleft1[1] >= topleft2[1]:
            if abs(topleft_prev1[1]+rect_prev1[1] - (topleft_prev2[1]+rect_prev2[1])) <= rect2[1]/2 and abs(topleft1[1]+rect1[1] - (topleft2[1]+rect2[1])) <= rect2[1]/2:
                same_height = 1
                if topleft_prev1[0] < topleft_prev2[0] :
                    topleft1[0] -= (DX_CONST - abs(topleft2[0] - topleft1[0]))/2
                    dx1 -= (DX_CONST - abs(topleft2[0] - topleft1[0]))/2
                    topleft2[0] += (DX_CONST - abs(topleft2[0] - topleft1[0]))/2
                    dx2 += (DX_CONST - abs(topleft2[0] - topleft1[0]))/2
                else :
                    topleft2[0] -= (DX_CONST - abs(topleft2[0] - topleft1[0]))/2
                    dx2 -= (DX_CONST - abs(topleft2[0] - topleft1[0]))/2
                    topleft1[0] += (DX_CONST - abs(topleft2[0] - topleft1[0]))/2
                    dx1 += (DX_CONST - abs(topleft2[0] - topleft1[0]))/2
            return [topleft1 , topleft2 , [dx1,dx2], same_height]
    else :
        return [topleft1 , topleft2 , [dx1,dx2], same_height]
                
                
    