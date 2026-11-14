# SensorStream

Pipeline Python de flux de capteurs IoT :
génération, tampon, statistiques glissantes,
alertes, stockage et affichage texte.

## Installation

    pip install -r requirements.txt
    python -m pytest

## Fonctionnalités

Format des données : timestamp, sensor_id, value

- generator : simule des capteurs - NOCAIR Nesrine

- buffer : garde les N dernières mesures - MEKKAOUI Anass

- sliding-window : fenêtre glissante (moyenne, min, max) - BAHIAOUI Imane

- alerts : détecte les seuils dépassés - JAMMARI Zineb

- timeseries-storage : sauvegarde SQLite des mesures - IBNOU EL KHATAB Farouk

- textdashboard : résumé texte des capteurs - MOUSSALIM Ali
