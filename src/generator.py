import random


def generate_readings(n, low=15.0, high=35.0, seed=None):
    """Génère n mesures de température simulées."""
    rng = random.Random(seed)
    return [round(rng.uniform(low, high), 2) for _ in range(n)]
