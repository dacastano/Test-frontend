import os
import pkgutil
import importlib

__all__ = []
PATH = [os.path.dirname(__file__)]

for module_info in pkgutil.walk_packages(PATH):
    module_name = module_info.name  # Get module name correctly
    __all__.append(module_name)

    # Import module dynamically using importlib
    spec = importlib.util.find_spec(module_name, package=__name__)
    if spec and spec.loader:
        _module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_module)
        globals()[module_name] = _module