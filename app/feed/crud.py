from sqlmodel.ext.asyncio.session import AsyncSession


class FeedCRUD:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self):
        resp = await self.session.execute("select * from search_data limit 2")
        # print(resp.scalar())
        result = resp.fetchall()
        for row in result:
            print(row[0], row[2])
        return {"hero": "hero"}
