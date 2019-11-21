from nonebot import on_command, CommandSession


@on_command('blog', aliases=('博文', '文章', '博客'))
async def blog(session: CommandSession):
    key = session.get('blog')


@blog.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['blog'] = stripped_arg
        return
    session.state[session.current_key] = stripped_arg


