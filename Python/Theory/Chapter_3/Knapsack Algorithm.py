def knapsack(W, weights, values, n):
    # Base case: कोई item न हो या capacity 0 हो
    if n == 0 or W == 0:
        return 0

    # अगर current item weight capacity से ज्यादा है, include नहीं कर सकते
    if weights[n - 1] > W:
        return knapsack(W, weights, values, n - 1)

    else:
        # Option 1: item include करो
        include_value = values[n - 1] + knapsack(W - weights[n - 1], weights, values, n - 1)
        # Option 2: item exclude करो
        exclude_value = knapsack(W, weights, values, n - 1)
        # Max value return करो
        return max(include_value, exclude_value)


# Example Data
values = [60, 100, 120]   # Profit of each item
weights = [10, 20, 30]    # Weight of each item
capacity = 50
n = len(values)

# Function Call
max_value = knapsack(capacity, weights, values, n)
print(f"Maximum value in Knapsack: {max_value}")
