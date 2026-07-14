module 1
fixed the problem of ipynb not using the existinig venv
```
source .venv/bin/activate
uv pip install ipykernel
python -m ipykernel install --user --name=.venv
```

module 2 
uv add onnxruntime tokenizers numpy tdqm minsearch gitsource
Resolved 49 packages in 5.01s
error: Distribution `onnxruntime==1.24.3 @ registry+https://pypi.org/simple` can't be installed because it doesn't have a source distribution or
       wheel for the current platform

hint: You're using CPython 3.10 (`cp310`), but `onnxruntime` (v1.24.3) only has wheels with the following Python implementation tags: `cp311`, `cp312`, `cp313`, `cp314`

```
uv add "onnxruntime==1.23.2" tokenizers numpy tqdm minsearch
```

