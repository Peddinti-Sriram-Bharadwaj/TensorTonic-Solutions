import math

def selu(x: list) -> list:
    """
    Returns SELU values rounded to four decimal places.
    """
    # Write code here
    lam = 1.0507009873554804934193349852946
    alpha = 1.6732632423543772848170429916717
    result = []
    for val in x:
        if val > 0:
            result.append(round(lam * val, 4))
        else:
            result.append(round(lam * alpha * (math.exp(val) - 1), 4))
    return result