# -*- coding: utf-8 -*-
# @Time    : 12/28/22 10:20 AM
# @FileName: test_module.py
# @Software: PyCharm
# @Github    ：sudoskys
import asyncio

from module.main import test_plugin
# 日志追踪调试
from loguru import logger
import sys

logger.remove()
handler_id = logger.add(sys.stderr, level="TRACE")
# 日志追踪调试


prompt = "孤独摇滚作者？"
table = {
    "search": [
        "https://www.baidu.com/baidu?tn=monline_7_dg&ie=utf-8&wd={}"
    ]
}
plugins = ["search"]


# Exec
async def main():
    result = await test_plugin(prompt=prompt, table=table, plugins=plugins)
    print(result)


asyncio.run(main())
