import random


def generate_readings(n, low=15.0, high=35.0, seed=None):
    """Génère n mesures de température simulées.

    Bornes : low doit être inférieur ou égal à high.
    Chaque valeur est arrondie à 2 décimales, puis ramenée dans
    [low, high] : elle ne sort jamais des bornes.
    """
    if low > high:
        raise ValueError("low doit être inférieur ou égal à high")
    rng = random.Random(seed)
    values = []
    for _ in range(n):
        value = round(rng.uniform(low, high), 2)
        values.append(min(max(value, low), high))
    return values
