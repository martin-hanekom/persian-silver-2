#!/bin/bash
if [ ! -d "venv" ]; then
  python3 -m pip install virtualenv
  python3 -m virtualenv venv
  source venv/bin/activate
  pip3 install -r requirements.txt
else
  source venv/bin/activate
fi
echo "$(pip3 -V)"
python3 src/main.py
