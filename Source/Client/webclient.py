import aiohttp
import defaultdata

class WebClient:
    def __init__(self, url : str):
        self.url = url
        self.session = aiohttp.ClientSession()

    async def Get(self, data):
        async with self.session:
            async with self.session.get("http://" + self.url) as response:
                jsonResponse = await response.json()
                return jsonResponse
    
    def RestartSession(self):
        self.session.close()
        self.session = aiohttp.ClientSession()
