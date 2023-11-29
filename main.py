import random

def monty_hall_simulation(num_trials, switch_choice):
    wins = 0

    for _ in range(num_trials):
        # Step 1: Randomly assign the car and make choices
        car_behind = random.randint(1, 3)
        player_choice = random.randint(1, 3)

        # Step 2: Host opens a door
        doors = [1, 2, 3]
        doors.remove(player_choice)
        if car_behind in doors:
            doors.remove(car_behind)
        host_opens = random.choice(doors)

        # Step 3: Player decides whether to switch
        if switch_choice:
            remaining_doors = [1, 2, 3]
            remaining_doors.remove(player_choice)
            remaining_doors.remove(host_opens)
            player_choice = remaining_doors[0]

        # Step 4: Check if the player wins
        if player_choice == car_behind:
            wins += 1

    return wins

# Running the simulation
num_trials = 100000
wins_with_switch = monty_hall_simulation(num_trials, True)
wins_without_switch = monty_hall_simulation(num_trials, False)

print(f"Winning rate with switch: {wins_with_switch / num_trials}")
print(f"Winning rate without switch: {wins_without_switch / num_trials}")
