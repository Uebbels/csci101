#Brendan Uebelhoer
#CSCI 101 Section A
#Python Lab 2A
kings = 0.0
queens = 0.0
rooks = 0.0
bishops = 0.0
knihgts = 0.0
pawns = 0.0
print('input number of each chess piece')
kings = int(input('KINGS>'))
queens = int(input('QUEENS>'))
rooks = int(input('ROOKS>'))
bishops = int(input('BISHOPS>'))
knights = int(input('KNIGHTS>'))
pawns = int(input('PAWNS>'))
#print(kings, queens, rooks, bishops, knights, pawns)
diff_kings = 1 - kings
diff_queens = 1 - queens
diff_rooks = 2 - rooks
diff_bishops = 2- bishops
diff_knights = 2 - knights
diff_pawns = 8 - pawns
diff_total = [diff_kings, diff_queens, diff_rooks, diff_bishops, diff_knights, diff_pawns]
sum_diff_total = sum(diff_total)
print('you need:')
print('OUTPUT', diff_kings, diff_queens, diff_rooks, diff_bishops, diff_knights, diff_pawns)
print('total', sum_diff_total)
