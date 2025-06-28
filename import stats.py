import stats

numbers = [1, 2, 3, 3, 4, 5, 5, 5]

print("List:", numbers)
mean_value = stats.mean(numbers)
print(f"Mean: {mean_value}")

median_value = stats.median(numbers)
print(f"Median: {median_value}")

mode_value = stats.mode(numbers)
print(f"Mode: {mode_value}")
