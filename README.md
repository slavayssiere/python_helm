# Helm Python

## develop

### github

You can clone project on Github : [github.com/slavayssiere/helm_python](https://github.com/slavayssiere/helm_python)

### prerequisite

please install :

```bash
sudo python -m pip install --upgrade pip setuptools wheel
sudo python -m pip install tqdm
sudo python -m pip install --user --upgrade twine
```

to deploy to PyPi:

```bash
python setup.py bdist_wheel
python -m twine upload dist/*
```
