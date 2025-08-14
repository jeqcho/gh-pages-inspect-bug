To replicate

1. Setup

```
python -m venv .venv
source .venv/bin/activate
pip install inspect-ai
```

2. Run eval

```
python example_task.py
```

3. Publish logs

```
inspect view bundle --output-dir docs
```

4. Commit and push to repo. Setup GitHub Pages in repo settings.