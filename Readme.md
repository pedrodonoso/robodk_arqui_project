
# Install virtualenv

```bash
    $ pip install virtualenv 
```

# Configurate virtualenv

```bash
    $ virtualenv -p /path/python venv
    $ source venv/bin/activate
    $ deactivate
```
# Install robodk

```bash
    $ pip install robodk
    $ pip install Flask
```

# Run api

```bash
    $ cd api
    $ flask --app main run
    $ flask --app main --debug run
```

# References

- [RodoDK API Python](https://robodk.com/doc/en/PythonAPI/index.html)
- [RoboDK](https://robodk.com/doc/es/Basic-Guide.html)

# LINUX

-  Es necesario configurar las variables de entorno en el archivo `~/.profile`.

```bash
    ROBODK_ROOT=$HOME/RoboDK/
    export LD_LIBRARY_PATH="$ROBODK_ROOT/bin/lib"
    export QT_PLUGIN_PATH="$ROBODK_ROOT/bin/plugins/"
    export QT_QPA_PLATFORM_PLUGIN_PATH="$ROBODK_ROOT/bin/plugins"
```
-   Recargar el archivo ejecutar `source ~/.profile`