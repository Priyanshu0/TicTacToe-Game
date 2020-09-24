import itertools

def all_same(L):
	if(len(set(L)) == 1 and L[0] != 0):
		return True
	return False

def win (current_game):
	#horizontal
	for row in current_game:
		if all_same(row):
			print(f"Player {row[0]} is the winner horizontally")
			return True
	# Diagonal
	diags_order = []
	for ix in range(game_size):
		diags_order.append(current_game[ix][ix])
	diags_reverse = []
	for ix in range(game_size - 1, -1, -1):
		diags_reverse.append(current_game[ix][game_size - 1 - ix])
	if all_same(diags_order):
		print(f"Player {diags_order[0]} is the winner diagonally")
		return True
	if all_same(diags_reverse):
		print(f"Player {diags_reverse[0]} is the winner diagonally")
		return True

	#vertical
	for col in range(game_size):
		check = []
		for row in current_game:
			check.append(row[col])
		if all_same(check):
			print(f"Player {check[0]} is the winner vertically")
			return True

	return False

def game_board(game_map, player = 0, row = 0, column = 0, just_display = False):
	try:
		if game_map[row][column] != 0:
			print("This position is occupado!")
			return game_map,False
		print("   " + "  ".join([str(i) for i in range(len(game_map))]))
		if not just_display:
			game_map[row][column] = player
		for count, row in enumerate(game_map):
			print(count, row)
		return game_map, True
	except IndexError as e:
		temp = [i for i in range(game_size)]
		print(f"Error: make sure you input row/column as {temp}", e)
		return game_map,False

	except Exception as e:
		print("Something went very wrong!",e)
		return game_map,False


play = True
players = [1,2]
while play:
	global game_size
	game_size = int(input("What size game of tic tac toe? : "))
	game = [[0 for i in range(game_size)] for i in range(game_size)]
	game_won = False
	game, _ = game_board(game, just_display = True)
	player_choice = itertools.cycle([1,2])
	temp = [i for i in range(game_size)]
	while not game_won:
		current_player = next(player_choice)
		print(f"Current Player {current_player}")
		played = False
		while not played:
			column_choice = int(input(f"What column do you want to play? {temp}: "))
			row_choice = int(input(f"What row do you want to play? {temp}: "))
			game, played = game_board(game, current_player, row_choice, column_choice)

		if win(game):
			game_won = True
			again = input("The game is over, would you like to play again? (y/n): ")
			if again.lower() == 'y':
				print("restrating")
			elif again.lower() == 'n':
				print("Bye")
				play = False
			else:
				print("Not a valid answer, so see you later")
				play = False
