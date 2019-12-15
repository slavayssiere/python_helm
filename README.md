# Helm Python

This is a Helm 3 wrapper in python.
Use it for your Iac scripts.

## use

1) add helm_python in your requirements.txt
2) import Helm class 

```python
import Helm
```

3) init Helm class

```python
helm = Helm()
```

This init function check if Helm is installed in PATH and if Helm version is 3 or higher

## helm upgrade

```python
helm.upgrade(
    name="my-nginx", 
    path="stable/nginx"
)
```

is equivalent to :

```bash
helm upgrade -i my-nginx stable/nginx
```

where :
 - "name" is the name of helm installation
 - "path" is the Helm package localisation (for examples: "stable/prometheus-operator" or "../myfolder/mychart")

Optionnal :

- namespace: namespace for installation
- 

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
