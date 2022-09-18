if pip3 -V | grep -qv '.venv'; then
  if [ ! -d ".venv" ]; then
    python3 -m venv .venv
  fi
  source .venv/bin/activate
  pip3 install -r requirements.txt
fi
echo "$(pip3 -V)"
python3 src/main.py
deactivate
