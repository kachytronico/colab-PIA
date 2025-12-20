from typing import Any

# Minimal pygame stub to silence linters/type-checkers for C-extension members used in the project

display: Any
font: Any
transform: Any
image: Any
Surface: Any
Font: Any
Rect: Any
init: Any
quit: Any

# module-level attributes sometimes referenced
version: Any

# Allow arbitrary attributes

class __getattr__:
    def __call__(self, name: str) -> Any: ...
