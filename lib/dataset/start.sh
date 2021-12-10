#!/usr/bin/env bash
deactivate

echo "Activating virtual environment"

source /home/lab/python-env/missuniverse-env/bin/activate

/home/lab/python-env/missuniverse-env/bin/python main.py

deactivate

echo "Activating Vibe environment"

conda activate vibe-env

python3 mainVibe.py
