from nonebot import on_command, CommandSession
from os import path
from re import search


@on_command('link', aliases=('链接', '网站', '网址', 'url', 'URL'))
async def link(session: CommandSession):
    key = session.get('link')
    
    res = search_link(key)
    if type(res) == int:
        await session.send(message[str(res)])
    else:
        if len(res) >= 2:
            await session.send('找到%d个结果呢，快夸夸竹竹~'%len(res))
        for line in res:
            print(line)
            await session.send('%s\n%s'%(line[0], line[1]))


@link.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['link'] = stripped_arg
        return
    session.state[session.current_key] = stripped_arg


def search_link(key_word):
    if not path.exists('./data/link.txt'):
        return 0
    with open(r'./data/link.txt', 'r', encoding='utf-8')as f:
        file = f.readlines()
    try:
        result = []
        for line in file:
            list = line.strip().split(' ')
            keys = list[0].split(',')
            for key in keys:
                if key_word in key:
                    result.append(list)
        if not result:
            return 2
        return result
    except Exception:
        return 1


message = {
    '0': '数据库文件不存在哦~',
    '1': '数据库的数据有误吧~',
    '2': '没有查询到呢，竹竹好笨~',
    '3': '出错了呀，竹竹也不知道为什么~'
}