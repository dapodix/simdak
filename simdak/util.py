import sys


def is_module_available(module_name) -> bool:
    if sys.version_info < (3, 0):
        # python 2
        import importlib

        torch_loader = importlib.find_loader(module_name)  # NOQA
    elif sys.version_info <= (3, 3):
        # python 3.0 to 3.3
        import pkgutil

        torch_loader = pkgutil.find_loader(module_name)  # NOQA
    elif sys.version_info >= (3, 4):
        # python 3.4 and above
        import importlib

        torch_loader = importlib.util.find_spec(module_name)  # NOQA

    return torch_loader is not None
