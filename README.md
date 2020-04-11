# barman-plugin-cookiecutter

This a cookiecutter template to create plugins for [barman](https://github.com/barmanaginn/barman).

## Usage

Go in your barman dev instance. The recommendation is to use a separate directory for plugins.

```
cd plugins
cookiecutter https://github.com/barmanaginn/barman-plugin-cookiecutter
```

You will be prompted some questions to populate the templates :

```
repo_name [barman-myawesomeplugin]: barman-rankings
module_name [barman_myawesomeplugin]: barman_rankings
name [My awesome plugin]: Rankings
author [Your name]: Yoann Pietri
email [Your email]: me@nanoy.fr
description [Short description]: Add rankings to BarMan
repo_url [Repository url]: https://github.com/barmanginn/barman-rankings
year [Current year]: 2020
version [Version]: 0.1
```

You then need to install your plugin to create the entry point :
```
pip3 install ./barman-rankings
```
