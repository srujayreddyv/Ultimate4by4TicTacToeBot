import random
import copy
class Player35():

	temp_board=''
	temp_block=''
	newcells=''	
	def __init__(self):
		pass
	def checksideblock(self,a,b,i,j):
		if i==a and j!=b and j!=(b+3):
			return 1
		if i==(a+3) and j!=b and j!=(b+3):
			return 1
		if j==b and i!=a and i!=(a+3):
			return 1
		if j==(b+3) and i!=a and i!=(a+3)	:
			return 1
		return 0

	def evalfunc(self,matrix,a,b,flag,bs):
		xl_side=0;
		xl_cor=0;
		ol_side=0;
		ol_cor=0;
		x1row=0;
		o1row=0;
		x2row=0;
		o2row=0;
		x3row=0;
		o3row=0;
		hor_x=0;
		ver_x=0;
		hor_o=0;
		ver_o=0;
		o_won=0;
		x_won=0;		
		for i in range(4):
			hor_x=0;
			hor_o=0;
			for j in range(4):	
				if self.checksideblock(a,b,a+i,b+j) and matrix[i+a][j+b]=='x':
					xl_side=xl_side+1;
				elif self.checksideblock(a,b,a+i,b+j)==0 and matrix[i+a][j+b]=='x':
					xl_cor=xl_cor+1;
				if self.checksideblock(a,b,a+i,b+j) and matrix[i+a][j+b]=='o':
					ol_side=ol_side+1;
				elif self.checksideblock(a,b,a+i,b+j)==0 and matrix[i+a][j+b]=='o':
					ol_cor=ol_cor+1;
				if matrix[i+a][j+b]=='x':
					hor_x=hor_x+1;
				elif matrix[i+a][j+b]=='o':
					hor_o=hor_o+1;
			if hor_x==1 and hor_o==0:
				x1row=x1row+1
			if hor_x==2 and hor_o==0:
				x2row=x2row+1
			if hor_x==3 and hor_o==0:
				x3row=x3row+1
			if hor_x==4 and hor_o==0:
				x_won=1
			if hor_o==1 and hor_x==0:
				o1row=o1row+1
			if hor_o==2 and hor_x==0:
				o2row=o2row+1
			if hor_o==3 and hor_x==0:
				o3row=o3row+1
			if hor_o==4 and hor_x==0:
				o_won=1

		for j in range(4):
			ver_x=0;
			ver_o=0;
			for i in range(4):				
				if matrix[i+a][j+b]=='x':
					ver_x=ver_x+1;
				elif matrix[i+a][j+b]=='o':
					ver_o=ver_o+1;
			if ver_x==1 and ver_o==0:
				x1row=x1row+1
			if ver_x==2 and ver_o==0:
				x2row=x2row+1
			if ver_x==3 and ver_o==0:
				x3row=x3row+1
			if ver_x==4 and ver_o==0:
				x_won=1
			if ver_o==1 and ver_x==0:
				o1row=o1row+1
			if ver_o==2 and ver_x==0:
				o2row=o2row+1
			if ver_o==3 and ver_x==0:
				o3row=o3row+1
			if ver_o==4 and ver_x==0:
				o_won=1

		diag_x=0;
		diag_o=0;
		for i in range(4):
			if matrix[i+a][i+b]=='x':
				diag_x=diag_x+1
			if matrix[i+a][i+b]=='o':
				diag_o=diag_o+1
		if diag_x==1 and diag_o==0:
			x1row=x1row+1
		if diag_x==2 and diag_o==0:
			x2row=x2row+1
		if diag_x==3 and diag_o==0:
			x3row=x3row+1
		if diag_x==4 and diag_o==0:
			x_won=1
		if diag_o==1 and diag_x==0:
			o1row=o1row+1
		if diag_o==2 and diag_x==0:
			o2row=o2row+1
		if diag_o==3 and diag_x==0:
			o3row=o3row+1
		if diag_o==4 and diag_x==0:
			o_won=1

		diag_x=0;
		diag_o=0;
		for i in range(4):
			if matrix[i+a][3+b-i]=='x':
				diag_x=diag_x+1
			if matrix[i+a][3+b-i]=='o':
				diag_o=diag_o+1
		if diag_x==1 and diag_o==0:
			x1row=x1row+1
		if diag_x==2 and diag_o==0:
			x2row=x2row+1
		if diag_x==3 and diag_o==0:
			x3row=x3row+1
		if diag_x==4 and diag_o==0:
			x_won=1
		if diag_o==1 and diag_x==0:
			o1row=o1row+1
		if diag_o==2 and diag_x==0:
			o2row=o2row+1
		if diag_o==3 and diag_x==0:
			o3row=o3row+1
		if diag_o==4 and diag_x==0:
			o_won=1

		if flag == 'x' :
			if x_won == 1 and bs == 1:
				return 1e10
			elif x_won == 1 and bs == 2 :
				return 1e17
			elif o_won == 1 and bs == 1 :
				return -1e10
			elif o_won == 1 and bs == 2 :
				return -1e17
			else :
				return ((x1row)*20) + ((x2row)*100) + ((x3row)*600) + (xl_side) + (xl_cor*4) -((((o1row)*20) + ((o2row)*100) + ((o3row)*600) + (ol_side) + (ol_cor*4)))
		else :
			if x_won == 1 and bs == 1:
				return -1e9
			elif x_won == 1 and bs == 2:
				return -1e17
			elif o_won == 1 and bs == 1:
				return 1e10	
			elif o_won and bs==2 :
				return 1e17
			else :
				return (((o1row)*20) + ((o2row)*100) + ((o3row)*600) + (ol_side) + (ol_cor*4)) - (((x1row)*20) + ((x2row)*100) + ((x3row)*600) + (xl_side) + (xl_cor*4))
		
	def search(self,board,old_move,cells,flag,depth,mflag,nflag,alpha,beta):
		nmove=(0,0)
		if beta<=alpha :
			if flag == mflag :
				return (1e18,nmove)
			else :
				return (-1e18,nmove)
		temp_board=copy.deepcopy(board.board_status)
		temp_block=copy.deepcopy(board.block_status)
		pasf=''
		if flag==mflag :
			pasf=nflag
		else :
			pasf=mflag
		if depth >= 3	 :
			x1=0
			for i in range(4):
				for j in range(4):
					if board.block_status[i][j] == '-' :
						x1=x1+self.evalfunc(board.board_status,i*4,j*4,mflag,1)
			x2=self.evalfunc(board.block_status,0,0,mflag,2)
			free=0
			if board.block_status[old_move[0]/4][old_move[1]/4] != '-' :
				free = -1000
			return (x1+(x2*4000)+free,nmove)
		else :
			ans=0
			if flag==mflag : 
				ans=-1e18
			else :
				ans=1e18
			for i in range(len(cells)) :
				newcells=board.find_valid_move_cells(cells[i])
				if flag == mflag :
					board.update(old_move,cells[i],flag)
					temp=self.search(board,cells[i],newcells,nflag,depth+1,mflag,nflag,alpha,beta)
					if temp[0] >= ans :
						ans=temp[0]
						nmove=cells[i]	
						alpha=max(alpha,ans)
					if beta<=alpha :
						board.board_status=copy.deepcopy(temp_board)
						board.block_status=copy.deepcopy(temp_block)
						break;

				else :
					board.update(old_move,cells[i],flag)
					temp=self.search(board,cells[i],newcells,mflag,depth+1,mflag,nflag,alpha,beta)
					if temp[0] <= ans :
						ans=temp[0]
						nmove=cells[i]
						beta=min(ans,beta)
					if beta<=alpha :
						board.board_status=copy.deepcopy(temp_board)
						board.block_status=copy.deepcopy(temp_block)
						break			
				board.board_status=copy.deepcopy(temp_board)
				board.block_status=copy.deepcopy(temp_block)
				if ans == 1e18 or ans == -1e18 :
					break

			return (ans,nmove) 

	def move(self, board, old_move, flag):
		#You have to implement the move function with the same signature as this
		#Find the list of valid cells allowed
		if old_move == (-1,-1) :
			return (4,5)
		cells = board.find_valid_move_cells(old_move)
		random.shuffle(cells)
		xflag='-'
		if flag=='x' :
			xflag='o'
		else :
			xflag='x'
		finalmove=self.search(board,old_move,cells,flag,0,flag,xflag,-1e18,1e18)
		return finalmove[1]
