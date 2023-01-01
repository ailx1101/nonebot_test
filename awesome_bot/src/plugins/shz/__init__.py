from nonebot import get_driver
from typing import Tuple, Any, Union
from nonebot import on_regex, on_command, on_message
from .config import Config
from nonebot.rule import Rule
from nonebot.params import CommandArg, RegexGroup
from nonebot.adapters.onebot.v11 import (Message, Bot,
                                         MessageSegment,
                                         GroupMessageEvent,
                                         PrivateMessageEvent)

global_config = get_driver().config
config = Config.parse_obj(global_config)


async def music_set_rule(event: Union[GroupMessageEvent, PrivateMessageEvent]) -> bool:
    if isinstance(event, GroupMessageEvent):
        print('foo插件成功了')
        msg = 'fooo'
        return msg
    elif isinstance(event, PrivateMessageEvent):
        print('私聊消息foooo')
        msg = '私聊'
        return msg


foo = on_command("foo", rule=Rule(music_set_rule), priority=1, block=False)


@foo.handle()
async def set_receive(bot: Bot, event: Union[GroupMessageEvent, PrivateMessageEvent],
                      args: Message = CommandArg()):
    msg = 'fooooo____'
    await bot.send(event=event, message=Message(MessageSegment.text(msg)))
