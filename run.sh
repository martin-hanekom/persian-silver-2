if pip3 -V | grep -qv '.venv'; then
  source .venv/bin/activate
fi
echo "$(pip3 -V)"
python3 src/main.py
deactivate
