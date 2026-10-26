import math

def softmax(scores: list[float]) -> list[float]:
    sum = 0
    for score in scores:
        sum += math.exp(score - max(scores))
    return [math.exp(score - max(scores)) / sum for score in scores]