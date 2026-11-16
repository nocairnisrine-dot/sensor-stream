
"""Tableau de bord texte."""


def render_dashboard(df, alerts=None):
    """Retourne un résumé texte des capteurs."""
    lines = ["=== SensorStream ==="]

    df = df.sort_values("timestamp")
    last = df.groupby("sensor_id").tail(1)

    for _, row in last.iterrows():
        name = row["sensor_id"]
        value = row["value"]
        lines.append(f"{name:<10} valeur : {value:.2f}")

    count = 0 if alerts is None else len(alerts)
    lines.append(f"Alertes : {count}")

    return "\n".join(lines)
