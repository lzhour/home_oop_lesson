import random

tree_positions = []

def random_position():
	random_x = random.randint(1,6)
	random_y = random.randint(1,6)

	new_tuple = (random_x, random_y)

	tree_positions.append(new_tuple)

if len(tree_positions) <= 2:
	for i in range(2):
		random_position()

if len(tree_positions) == 2:
	if tree_positions[0] == tree_positions[1]:
		del tree_positions[1]
		random_position()
	else:
		random_position()
		if tree_positions[2] == (tree_positions[0] or tree_positions[1]):
			del tree_positions[-1]
			random_position()
			
print tree_positions
