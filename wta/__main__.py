"""让 `python -m wta ...` 可以直接运行。"""

import sys

if sys.version_info < (3, 11):  # noqa: UP036  给用旧版本的人一句看得懂的提示，而不是一个导入错误
    raise SystemExit(f"需要 Python 3.11 或更高版本，当前是 {sys.version.split()[0]}。")

from .cli import main

raise SystemExit(main())
