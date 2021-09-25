def test (key,cur_key,break_key,maxi_num) :
	if break_key[key][1] :		#ce n'est pas damage....
		if type(break_key[key][1][0]) == type([]):
			if  break_key[cur_key][0] in break_key[key][1][0] and break_key[key][1][1] <= maxi_num :
				return 1
			else :
				return 0
		elif  break_key[cur_key][0] in break_key[key][1]:
			return 1
		else :
			return 0
	else :
		return 1


		

####################################	
def mouvement (q,sm_ck,break_key,maxi_num) :		#sm_ck est same_move et cur_key
	s = ''	
	j = q[0][0]
	for i in range(q[1]) :
		s += q[0][1][j]
		j = (j+1) % q[1]
	if s[-1] == 'T' :
		if s[-3:] == 'DsT' or s[-3:] == 'sDT' or s[-4:] == 'DsdT' or s[-4:] == 'sDdT' :			#adoken
			if test(46,sm_ck[1],break_key,maxi_num) or sm_ck[0] == 0:
				sm_ck[0] = 0
				return 46,sm_ck[0]		#special move a p
			elif test(34,sm_ck[1],break_key,maxi_num) :
				sm_ck[0] = 0
				return 34,sm_ck[0]		#strong attack air p
			else :
				return sm_ck[1],sm_ck[0]
		elif s[-3:] == 'AsT' or s[-3:] == 'sAT' or s[-4:] == 'AsaT' or s[-4:] == 'sAaT' :			#helice
			if test(49,sm_ck[1],break_key,maxi_num) :
				sm_ck[0] = 0
				return 49,sm_ck[0]		#special move c p
			elif test(34,sm_ck[1],break_key,maxi_num) :
				sm_ck[0] = 0
				return 34,sm_ck[0]		#strong attack air p
			else :
				return sm_ck[1],sm_ck[0]
		elif test(30,sm_ck[1],break_key,maxi_num) :
			sm_ck[0] = 0
			return 30,sm_ck[0]		#strong attack p
		elif test(32,sm_ck[1],break_key,maxi_num) :
			sm_ck[0] = 0
			return 32,sm_ck[0]		#strong attack crouch p
		elif test(34,sm_ck[1],break_key,maxi_num) :
			sm_ck[0] = 0
			return 34,sm_ck[0]		#strong attack air p
		else :
			return sm_ck[1],sm_ck[0]
	elif s[-1] == 'G' :
		if s[-3:] == 'DsG' or s[-3:] == 'sDG' or s[-4:] == 'DsdG'or s[-4:] == 'sDdG' :			#adoken
			if test(45,sm_ck[1],break_key,maxi_num) :
				sm_ck[0] = 0
				return 45,sm_ck[0]		#special move a g
			elif test(33,sm_ck[1],break_key,maxi_num) :
				sm_ck[0] = 0
				return 33,sm_ck[0]		#strong attack air g
			else :
				return sm_ck[1],sm_ck[0]
		elif s[-3:] == 'AsG' or s[-3:] == 'sAG' or s[-4:] == 'AsaG' or s[-4:] == 'sAaG' :			#helice
			if test(48,sm_ck[1],break_key,maxi_num) :
				sm_ck[0] = 0
				return 48,sm_ck[0]		#special move c g
			elif test(33,sm_ck[1],break_key,maxi_num) :
				sm_ck[0] = 0
				return 33,sm_ck[0]		#strong attack air g
			else :
				return sm_ck[1],sm_ck[0]
		elif test(29,sm_ck[1],break_key,maxi_num) :
			sm_ck[0] = 0
			return 29,sm_ck[0]		#strong attack g
		elif test(31,sm_ck[1],break_key,maxi_num) :
			sm_ck[0] = 0
			return 31,sm_ck[0]		#strong attack crouch g
		elif test(33,sm_ck[1],break_key,maxi_num) :
			sm_ck[0] = 0
			return 33,sm_ck[0]		#strong attack air g
		else :
			return sm_ck[1],sm_ck[0]
	elif s[-1] == 'Y' :
		if s[-3:] == 'DsY' or s[-3:] == 'sDY' or s[-4:] == 'DsdY' or s[-4:] == 'sDdY' :			#adoken
			if test(36,sm_ck[1],break_key,maxi_num) :
				sm_ck[0] = 0
				return 36,sm_ck[0]		#strongest attack p
			elif test(40,sm_ck[1],break_key,maxi_num) :
				sm_ck[0] = 0
				return 40,sm_ck[0]		#strongest attack air p
			else :
				return sm_ck[1],sm_ck[0]
		elif s[-3:] == 'AsY' or s[-3:] == 'sAY' or s[-4:] == 'AsaY' or s[-4:] == 'sAaY' :			#helice
			if test(47,sm_ck[1],break_key,maxi_num) :
				sm_ck[0] = 0
				return 47,sm_ck[0]		#special move b
			elif test(27,sm_ck[1],break_key,maxi_num) :
				sm_ck[0] = 0
				return 27,sm_ck[0]		#weak attack air p
			else :
				return sm_ck[1],sm_ck[0]
		elif s[-3:] == 'SsY' or s[-3:] == 'sSY' or s[-4:] == 'SssY' or s[-4:] == 'sSsY' :			#lamme
			if test(54,sm_ck[1],break_key,maxi_num) :
				sm_ck[0] = 0
				return 54,sm_ck[0]		#special move p54
			elif test(27,sm_ck[1],break_key,maxi_num) :
				sm_ck[0] = 0
				return 27,sm_ck[0]		#weak attack air p
			else :
				return sm_ck[1],sm_ck[0]
		elif test(25,sm_ck[1],break_key,maxi_num) :
			sm_ck[0] = 0
			return 25,sm_ck[0]		#weak attack crouch p
		elif test(27,sm_ck[1],break_key,maxi_num) :
			sm_ck[0] = 0
			return 27,sm_ck[0]		#weak attack air p
		elif test(23,sm_ck[1],break_key,maxi_num) :
			sm_ck[0] = 0
			return 23,sm_ck[0]		#weak attack
		else :
			return sm_ck[1],sm_ck[0]
	elif s[-1] == 'H' :
		if s[-3:] == 'DsH' or s[-3:] == 'sDH' or s[-4:] == 'DsdH'or s[-4:] == 'sDdH' :			#adoken
			if test(35,sm_ck[1],break_key,maxi_num) :
				sm_ck[0] = 0
				return 35,sm_ck[0]		#strongest attack g
			elif test(39,sm_ck[1],break_key,maxi_num) :
				sm_ck[0] = 0
				return 39,sm_ck[0]		#strongest attack air g
			else :
				return sm_ck[1],sm_ck[0]
		elif s[-3:] == 'AsH' or s[-3:] == 'sAH' or s[-4:] == 'AsaH' or s[-4:] == 'sAaH' :			#helice
			if test(47,sm_ck[1],break_key,maxi_num) :
				sm_ck[0] = 0
				return 47,sm_ck[0]		#special move b
			elif test(26,sm_ck[1],break_key,maxi_num) :
				sm_ck[0] = 0
				return 26,sm_ck[0]		#weak attack air g
			else :
				return sm_ck[1],sm_ck[0]
		elif s[-3:] == 'SsH' or s[-3:] == 'sSH' or s[-4:] == 'SssH' or s[-4:] == 'sSsH' :			#lamme
			if test(53,sm_ck[1],break_key,maxi_num) :
				sm_ck[0] = 0
				return 53,sm_ck[0]		#special move p53
			elif test(27,sm_ck[1],break_key,maxi_num) :
				sm_ck[0] = 0
				return 26,sm_ck[0]		#weak attack air g
			else :
				return sm_ck[1],sm_ck[0]
		elif test(24,sm_ck[1],break_key,maxi_num) :
			sm_ck[0] = 0
			return 24,sm_ck[0]		#weak attack crouch g
		elif test(26,sm_ck[1],break_key,maxi_num) :
			sm_ck[0] = 0
			return 26,sm_ck[0]		#weak attack air g
		elif test(52,sm_ck[1],break_key,maxi_num) :
			sm_ck[0] = 0
			return 52,sm_ck[0]		#ken_throw
		else :
			return sm_ck[1],sm_ck[0]
	elif s[-1] == 'J' :
		if s[-3:] == 'DsJ' or s[-3:] == 'sDJ' or s[-4:] == 'DsdJ'or s[-4:] == 'sDdJ' :			#adoken
			if test(51,sm_ck[1],break_key,maxi_num) :
				sm_ck[0] = 0
				return 51,sm_ck[0]		#super move b 
			elif test(28,sm_ck[1],break_key,maxi_num) :
				sm_ck[0] = 0
				return 28,sm_ck[0]		#weak_at(tack)_pied_air
			else :
				return sm_ck[1],sm_ck[0]
		elif s[-3:] == 'AsJ' or s[-3:] == 'sAJ' or s[-4:] == 'AsaJ' or s[-4:] == 'sAaJ' :			#helice
			if test(50,sm_ck[1],break_key,maxi_num) :
				sm_ck[0] = 0
				return 50,sm_ck[0]		#super move a
			elif test(28,sm_ck[1],break_key,maxi_num) :
				sm_ck[0] = 0
				return 28,sm_ck[0]		#weak_at(tack)_pied_air
			else :
				return sm_ck[1],sm_ck[0]
		elif test(28,sm_ck[1],break_key,maxi_num) :
			sm_ck[0] = 0
			return 28,sm_ck[0]		#weak_at(tack)_pied_air
		elif test(37,sm_ck[1],break_key,maxi_num) :
			sm_ck[0] = 0
			return 37,sm_ck[0]		#strongest attack crouch g
		else :
			return sm_ck[1],sm_ck[0]
	elif s[-1] == 'U' :
		if s[-2:] == 'AU' :
			if test(15,sm_ck[1],break_key,maxi_num) :
				sm_ck[0] = 0
				return 15,sm_ck[0]		#teleport back
			elif test(44,sm_ck[1],break_key,maxi_num) :
				sm_ck[0] = 0
				return 44,sm_ck[0]		#throw air miss
			else :
				return sm_ck[1],sm_ck[0]
		elif s[-2:] == 'DU':
			if test(14,sm_ck[1],break_key,maxi_num) :
				sm_ck[0] = 0
				return 14,sm_ck[0]		#teleport avant
			#elif test(11,sm_ck[1],break_key,maxi_num) :           #en decommentant ceci ,esquiver en airdash est diff
			#	sm_ck[0] = 0
			#	return 11,sm_ck[0]		#air dash
			elif test(44,sm_ck[1],break_key,maxi_num) :
				sm_ck[0] = 0
				return 44,sm_ck[0]		#throw air miss
			else :
				return sm_ck[1],sm_ck[0]
		else :
			if test(38,sm_ck[1],break_key,maxi_num) :
				sm_ck[0] = 0
				return 38,sm_ck[0]		#strongest attack crouch p : u etant crouch
			elif sm_ck[1] == 4 or sm_ck[1] == 7:		#si cur_action est walk avant ou run avant
				if test(14,sm_ck[1],break_key,maxi_num) :
					sm_ck[0] = 0
				return 14,sm_ck[0]		#teleport avant
			elif sm_ck[1] == 5 or sm_ck[1] == 8:		#si cur_action est walk back ou run back
				if test(15,sm_ck[1],break_key,maxi_num) :
					sm_ck[0] = 0
				return 15,sm_ck[0]		#teleport back
			elif test(42,sm_ck[1],break_key,maxi_num) :
				sm_ck[0] = 0
				return 42,sm_ck[0]		#throw miss
			elif test(44,sm_ck[1],break_key,maxi_num) :
				sm_ck[0] = 0
				return 44,sm_ck[0]		#throw air miss
			else :
				return sm_ck[1],sm_ck[0]
	elif s[-2:] == 'aA' :
		if test(8,sm_ck[1],break_key,maxi_num) :
			sm_ck[0] = 0
		return 8,sm_ck[0]		#run back
	elif s[-2:] == 'dD' :
		if test(7,sm_ck[1],break_key,maxi_num) :
			sm_ck[0] = 0
			return 7,sm_ck[0]		#run avant
		elif test(11,sm_ck[1],break_key,maxi_num) :
			sm_ck[0] = 0
			return 11,sm_ck[0]		#air dash
		else :
			return sm_ck[1],sm_ck[0]
	else :
		return -1,sm_ck[0]

##############################

