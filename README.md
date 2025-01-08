# Caesar cipher

Command line application that encodes textfiles using
the [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher).

## Installation

```
python3 -m venv .venv
pip install .
```

## Usage

Encode file

```python3 main.py -f input/input.txt -c 3```

Decode file

```python3 main.py -f input/input_shift_3.txt -c 3 -d```
