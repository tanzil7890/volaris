import fire
from volaris import auto_init
from volaris.toolkit.rolling.base import Rolling
from volaris.utils.mod import find_all_classes

if __name__ == "__main__":
    sub_commands = {}
    for cls in find_all_classes("volaris.toolkit.rolling", Rolling):
        sub_commands[cls.__module__.split(".")[-1]] = cls
    # The sub_commands will be like
    # {'base': <class 'volaris.toolkit.rolling.base.Rolling'>, ...}
    # So the you can run it with commands like command below
    # - `python -m volaris.toolkit.rolling base --conf_path <path to the yaml> run`
    # - base can be replace with other module names
    auto_init()
    fire.Fire(sub_commands)
