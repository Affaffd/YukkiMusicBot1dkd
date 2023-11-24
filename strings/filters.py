from typing import List, Union

from pyrogram import filters


#
# Copyright (C) 2021-2022 by #????? ?????? ???? ???? ?????
# copyright @EITHON1 @V_V_G


def command(commands: Union[str, List[str]]):
    return filters.command(commands, "")

