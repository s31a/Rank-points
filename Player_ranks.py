# Rank to Points
rank_points = {'iron' : 0, 'bronze' : 0, 'silver' : 0, 'gold' : 5, 'plat' : 10, 'platinum' : 10, 'diamond' : 15, 'ascendant' : 25, 'asc' : 25, 'immortal' : 35, 'radiant' : 45}

# Ask for player ranks
def ask_for_ranks():
    ranks = []
    for i in range(5):
        rank = input(f"Enter rank for player {i+1}: ").lower()
        if rank not in rank_points:
            rank = input(f"Try again - Enter rank for player {i+1}: ").lower()
        ranks.append(rank)
    return ranks

# Tell the user if they went over the point limit
def is_over():
    if total_points > 100:
        print("You are over the point limit by", total_points - 100)
    else:
        print("You are ready to compete!")

# Calc points
def calculate_total_points(player_ranks):
    total_points = sum(rank_points[rank] for rank in player_ranks)
    return total_points

player_ranks = ask_for_ranks()
total_points = calculate_total_points(player_ranks)

print("Total points of all players:", total_points)
is_over()