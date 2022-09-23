import requests
import json
import pandas as pd

app = requests('https://api.pipe.run/v1/application/json/automations?show=1/companies?with=contactPhones')
token = 'eb91017198009e5fa4dd0fbac57ac4f1'

app = app.json('''{
"success": true,
"message": "OK",
"data": {
"id": 78,
"account_id": 1,
"user_id": 2,
"from_user_id": 1,
"deal_id": 47,
"company_id": 94,
"person_id": 49,
"webphone_id": 1,
"webphone_extension_id": 1,
"name": "Lucas Marinho",
"from_number": "",
"to_number": "55991318182",
"record_audio": 1,
"from_caller_id": "51992307570",
"to_caller_id": "55991318182",
"description": "",
"start_at": "2021-03-17 15:30:23",
"end_at": "",
"status": 200,
"record_url": "https://example.org/audio.mp3",
"external_call_id": 66558623,
"json_return": "",
"important": 1,
"duration": "00:05:31",
"cost": 1.46,
"created_at": "2021-03-17 14:02:54",
"updated_at": "2021-03-17 14:02:54"
}
}''')

app_contato = app['/companies?with=contactPhones']
app_contato_analista = app['TELEFONE DE CONTATO DO ANALISTA']
app_contato_ = app['TELEFONE DE CONTATO DO ANALISTA']

tmp_cntt = app['/companies?with=contactPhones']

pd.pivot_table (app, índice = tmp_cntt)