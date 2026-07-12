import numpy as np

def entropy_node(y):
    if len(y) == 0:
        return 0.0

    # Count class frequencies
    _, counts = np.unique(y, return_counts=True)

    # Probabilities
    prob = counts / len(y)

    # Remove zero probabilities
    prob = prob[prob > 0]

    # Entropy
    entropy = -sum(p * np.log2(p) for p in prob)

    return float(entropy)
