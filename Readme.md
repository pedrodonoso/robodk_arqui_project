
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