---
parent: File Operations
grand_parent: Technologie Informatyczne II
nav_order:  4
---

# Saving and loading Python objects

So far, manual saving and reading of file contents has been described. This is useful if you want to operate on files with data and results saved in plain text. However, if we want to write/read the content of any Python variables (e.g. to save the state of the program), manual text creation and its interpretation can be cumbersome.

Fortunately, Python comes with a number of modules that make this task much easier. The most basic module is the module  `pickle`. It allows you to write or read any variable with one command. Its use is best illustrated by an example:

```python
import pickle

# The variable data contains a dictionary of the collected data that we want to save
data = {'a': [1,2,3], 'b': "Ala has a cat", 'c': 123}

with open ('data. pickle', 'wb') as save_file:
    pickle.dump(data, save_file)
```

The function `dump(variable, file)` from the `pickle` module writes the contents of the *variable* to the specified *file*. The file must be opened in binary mode (you must add additional character `b`  in open mode). The content of the file is specific to Python and it should not be opened e.g. in a text editor (in fact, the exact content does not matter: it is important that Python can interpret it correctly). The file created in this way can be read in another program using function `picklebpickle` from the `pickle` module that will return the previously saved variable:

```python
import pickle

with open ('data.pickle', 'rb') as read_file:
    data = pickle.load(read_file)
```

 Pickle functions `dump` and  `load` can be called several times for a given file. Then successive variables are written to it, which can be read one by one. However, in order to save the program settings, it is recommended to create one dictionary containing them all and save/load it once.

There are other modules that work similarly to `pickle`. For example `json` and `yaml` (the latter is not the standard Python module, but in the distribution of Anaconda is installed by default). Unlike the `pickle` module, they require files that are opened in text mode (without `b`). They will create text files in [JSON](https://en.wikipedia.org/wiki/JSON) or [YAML](https://en.wikipedia.org/wiki/YAML) formats that can be read and edited in external tools. At the same time, these formats can be read from Python:
```python
import json

data = {'a': [1,2,3], 'b': "Ala ma cat", 'c': 123}

with open('data.json', 'w') as saved_file:
     json.dump(data, saved_file)


with open('data.json', 'r') as read_file:
    print(json.load(read_file))
```
or
```python
import yaml

data = {'a': [1,2,3], 'b': "Ala ma cat", 'c': 123}

with open('data.yaml', 'w') as saved_file:
     yaml.dump(data, saved_file)


with open('data.yaml', 'r') as read_file:
    print(yaml.safe_load(read_file))  # Unlike pickle and json yaml uses safe_load instead of load
```
The above codes work the same as for the module `pickle`. However, please open the file `data.yaml` in a text editor: its content should be readable and possible to modify manually.

***Attention!***  When using the `json` module, it is not possible to save a variable of any type (e.g. tuples which must first be converted into lists). `pickle` and `yaml` do not have this limitation.


<hr/>

Opublikowano na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
