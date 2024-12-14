
## Setup virtual env

```
python -m venv .venv 
. ./.venv/bin/activate
```

## Install dependant libraries

```
pip install pip-tools
pip-compile requirements.in
pip install -r requirements.txt
```
