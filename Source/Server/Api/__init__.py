import ast

import flask
import flask_restful

import SpreadSheetService

def apiInit():
    SpreadSheetService.gspreadInit()

    flaskApp = flask.Flask(__name__)
    flaskApi = flask_restful.Api(flaskApp)

    class modResource(flask_restful.Resource):
        def get(self, path):
            
            data = ast.literal_eval(flask.request.form['data'])

            if data['request_type'] == 'latest_version': # RETURN: LATEST VERSION OF MOD COMPATIBLE WITH MINECRAFT VERSION
                minecraftVersion = data['minecraft_version']
                modName = data['mod_name']

                SpreadSheetService.findCell(modName)

                # Data form is expected to be written in standard python
                # dictionary syntax.

            return {}, 404

    class modListResource(flask_restful.Resource):
        def get(self, path):
            return {}, 404