import aiomysql, asyncio, logging



async def create_pool(loop):
    global __pool
    __pool = await aiomysql.create_pool(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123456',
        db='esf',
        autocommit=True,
        maxsize=10,
        minsize=1,
        loop=loop
    )


async def select(sql, args, size=None):
    global __pool
    with(await __pool) as conn:
        cur = await conn.cursor(aiomysql.DictCursor)
        await cur.execute(sql.replace('?', '%s'), args or ())
        if size:
            rs = await cur.fetchmany(size)
        else:
            rs = await cur.fecthall()
        await cur.close()
        return rs


async def execute(sql, args, autocommit=False):
    global __pool
    with(await __pool) as conn:
        if not autocommit:
            await conn.begin()
        try:
            cur = await conn.cursor(aiomysql.DictCursor)
            await cur.execute(sql.replace('?', '%s'), args)
            affected = cur.rowcount
            await cur.close()
            if not autocommit:
                await conn.commit()
        except BaseException as e:
            if not autocommit:
                await conn.rollback()
            raise
        return affected


async def insert(table, map):
    field = []
    args = []
    for k, v in map:
        field.append(k)
        args.append('\'' + v + '\'')
    sql = 'insert into %s (%s) VALUE (%s)' % (table, ','.join(field), ','.join(args))
    await execute(sql, [])