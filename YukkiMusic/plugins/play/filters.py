from pyrogram import filters
from typing import List, Union


#تعديل وتحديث مطور سورس ايثون
# copyright @EITHON1 @V_V_G


def command(commands: Union[str, List[str]]):
    return filters.command(commands, "")