"""
4.  In a long career for Yorkshire, Geoffrey Boycott played 609 matches, batted 1014
    times, was not out 162 times, and scored 48426 runs. Write a program to calculate
    and display Boycott's batting average.
    Note: A batting average is the number of runs scored divided by the number of
    completed innings (i.e. the total times batted minus the times not out).
"""

# Program to calculate Geoffrey Boycott's batting average
print("-" * 20)

# Given values
batted_times = 1014  # Total times batted
not_out_times = 162  # Times not out
scored_runs = 48426  # Total runs scored

# Calculate completed innings
completed_innings = batted_times - not_out_times

# Calculate batting average
batting_average = scored_runs / completed_innings

# Display the result
print(f"Boycott's batting average: {batting_average:.2f}")

print("-" * 20)