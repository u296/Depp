import asyncio
from aiohttp import web

async def GetrequestHandler():
    return web.json_response({"anwser":"brööd"})

async def PostrequestHandler():
    pass

routes = web.RouteTableDef()
    
@routes.get('/')
async def GetresponseHandler(request):
    response = await asyncio.create_task(GetrequestHandler())
    return response

@routes.post('/post')
async def PostresponseHandler(request):
    response = await asyncio.create_task(PostrequestHandler())
    return response

class WebServer():
    

    def __init__(self):
        self.app = web.Application()
        self.app.add_routes(routes)

    def run(self):
        web.run_app(self.app)
    
    
