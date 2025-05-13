# Prompt to enter the number of participants
n = int(input("Enter the number of participants: "))

# Prompt to enter the scores separated by spaces
scores = list(map(int, input("Enter the scores separated by spaces: ").split()))

# Sort the scores in descending order and remove duplicates
unique_scores = sorted(set(scores), reverse=True)

# Check if there is a runner-up score
if len(unique_scores) > 1:
    runner_up_score = unique_scores[1]
    print(f"Runner-up score = {runner_up_score}")
else:
    print("No runner-up score available.")