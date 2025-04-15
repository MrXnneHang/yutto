from __future__ import annotations

from yutto.utils.console.formatter import get_string_width


class StatusBar:
    _enabled = False
    tip = ""
    _snippers = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    _count = 0
    _last_line_width = 0

    @classmethod
    def enable(cls):
        cls._enabled = True

    @classmethod
    def disable(cls):
        cls._enabled = False

    @classmethod
    def set_snippers(cls, snippers: list[str]):
        cls._snippers = snippers

    @classmethod
    def clear(cls):
        if not cls._enabled:
            print("clear: cls is not enabled")
            return
        print("\r" + cls._last_line_width * " " + "\r", end="\n")

    @classmethod
    def set(cls, text: str):
        if not cls._enabled:
            print("set: cls is not enabled")
            return
        cls.clear()
        print(text, end="\n")
        cls._last_line_width = get_string_width(text)

    # def set(cls, text: str):
    #     if not cls._enabled:
    #         return
    #     cls.clear()
    #     # 使用 ANSI 转义序列实现替代方案
    #     print(text, end="\n")  # 用换行符确保 wexpect 能捕获
    #     # 然后使用 ANSI 转义码移动光标回到上一行
    #     print("\033[1A\033[K", end="") # 上移一行并清除
    #     cls._last_line_width = get_string_width(text)

    @classmethod
    def set_tip(cls, tip: str):
        cls.tip = tip

    @classmethod
    def next_tick(cls):
        cls.set(cls._snippers[cls._count] + " " + cls.tip)
        cls._count += 1
        cls._count %= len(cls._snippers)
