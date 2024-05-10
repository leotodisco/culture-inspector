# Culture Inspector 
Culture Inspector is a Python tool designed to compute the cultural dispersion of a community of developers based on their nationality informations. Additionally, it provides recommendations about community smells, helping to identify potential issues within the community dynamics.

## Features 
- Computes the cultural dispersion of a community based on the nationality of its developers.
- Utilizes six values, each corresponding to one of Hofstede's cultural dimensions.
- Provides recommendations based on the computed cultural dispersion to identify potential community smells.

## Installation 

Python 3.11 is required to install this tool, then you should create a virtual environment by using the following command:

```bash
python3.11 -m venv myenv
```
You should enter you virtual environment with the following command:
```bash
source myenv/bin/activate
```

And you can install all the required dependencies with this command:
```bash
pip install -r requirements.txt
```

## How To Use the Tool
To use the tool, after getting in the virtual environment, you should run the runner with this command:
```bash
python runner.py
```

