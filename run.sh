#!/usr/bin/env bash
echo "Starting pytapo cron..."
# Cron im Vordergrund starten (Docker benötigt keinen Hintergrundprozess)
crond -f -l 2
