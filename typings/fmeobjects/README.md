# fmeobjects
Stub typings for the FME Python API

The FME Python API is a compiled shared object (.so) library without docstrings. Adding this stub file to a projects typings will allow your IDE to populate the autocompletions and intellisense (e.g. pylance / pycharm)

## Usage

Clone this repo into a `./typings` directory of your project. If you have a different setup this may have been set with `"python.analysis.stubPath": "typings"`.

In your own code then you can either:
```
import fmeobjects

fmeobjects.FMEArc()
```

or

```
from fmeobjects import FMEArc

FMEArc()
```

## Caveat ##
As this stub was created with a structured hierarchy to match the API categories, if you start using a class or method e.g. `FMEDonut` without importing it your editor may choose to *autoadd* the appropriate import. In this case it would add:
```
from fmeobjects.geometries.areas import FMEDonut
```
which would correctly autocomplete the methods and give intelisense but means nothing to the executing code. You will get errors to nudge you like `Import "fmeobjects.geometries.areas" could not be resolved from source` which alert you to the mismatch.

You can avoid this if you clone the 'compiled' branch of this repo which flattens the code into the root __init__ to match the source.
