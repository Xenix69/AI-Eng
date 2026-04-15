# Function to analyze scores
def analyze_scores(scores):
    average = sum(scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)
    
    return average, highest, lowest


# List of student scores
scores = [75, 88, 92, 67, 84]

# Tuple unpacking
avg, high, low = analyze_scores(scores)

# Output
print("Average score:", avg)
print("Highest score:", high)
print("Lowest score:", low)