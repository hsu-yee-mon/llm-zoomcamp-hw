fixed the problem of ipynb not using the existinig venv
```
source .venv/bin/activate
uv pip install ipykernel
python -m ipykernel install --user --name=.venv
```