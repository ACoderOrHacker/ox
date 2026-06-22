# Metainfo Description

`meta` is a directory that contains the metainfo for the subproject.
it has the following files:

- `config.json`: contains the configurations and its descriptions for the subproject.
- `libraries.json`: contains the libraries for the subproject.

## config.json

### Member - `config`

`config` is an array that contains objects representing the configurations for the subproject.

Each object has the following members:

- `name`: the name of the configuration.
- `description`: the description of the configuration.

For example:

```json
{
    "name": "OX_EXAMPLE_SUBPROJECT_ENABLE_XXX",
    "description": "Enables the XXX feature of the subproject."
}
```

## libraries.json

### Member - `libraries`

`libraries` is an array that contains objects representing the libraries for the subproject.

Each object has the following members:

- `name`: the name of the library.
- `description`: the description of the library.
- `copyright`: the copyright of the library.
- `authors`: the authors of the library.
- `version`: the version of the library.
- `cpp_standard`: the **lowest** C++ standard supported by the library.
- `homepage`: the homepage of the library.

For example:

```json
{
    "name": "Example Library",
    "description": "A brief description of the library.",
    "copyright": "Copyright (C) ACoderOrHacker",
    "authors": ["ACoderOrHacker"],
    "version": "1.0.0",
    "cpp_standard": "17",
    "homepage": "https://ACoderOrHacker.github.io/ox"
}
```
