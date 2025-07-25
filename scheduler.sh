#!/bin/bash
# Script CRON pour Raspberry Pi (à exécuter entre 2h et 4h AM)

cd /home/pi/plex_rentabilite
python3 scraping.py
python3 analyse.py
python3 email_alert.py
