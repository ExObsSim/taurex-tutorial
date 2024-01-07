# TauREx-Helloworld

version 0.0.1-alpha

A plugin for [TauREx](https://github.com/ucl-exoplanets/TauREx3_public) 3.1 that provides the [Helloworld](link) temperature by Author for the retrieval


## Installation (PyPI)

Installing is simply done by running
```bash
pip install taurex_helloworld
```

### Installing from source


You can install from source by doing:
```bash
git clone https://github.com/[org_name]/taurex-helloworld.git
cd taurex_hellworld
pip install .
```

## Running in TauREx

Once installed you can select the temperature profile through the **profile_type** keyword under Temperature.

```
[Temperature]
profile_type = helloworld   # Valid keyword RandomTemperature, helloworld, hello-earth
```
