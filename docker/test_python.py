import websocket
from websocket import create_connection

#websocket.enableTrace(True)

token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICItSnc0OENxRERuS2xIcS1JM1VreDJOTFc5OGpobWh0YlUtUm5sMUVheDlzIn0.eyJleHAiOjE2ODEzOTc5MTIsImlhdCI6MTY4MTM3NjMxMiwiYXV0aF90aW1lIjowLCJqdGkiOiJmZDcwODlhNS1kMTgzLTRlZjMtYmVmOC0xZTA4NDc2NjRkNDEiLCJpc3MiOiJodHRwOi8va2V5Y2xvYWs6ODA4MC9hdXRoL3JlYWxtcy95Z2dpbyIsImF1ZCI6InlnZ2lvLXNlcnZpY2VzIiwic3ViIjoiZTIwNWZhZjktODMxZS00YmJhLWI1YmQtY2ExNmU4ZGM4NzQzIiwidHlwIjoiSUQiLCJhenAiOiJ5Z2dpby1zZXJ2aWNlcyIsInNlc3Npb25fc3RhdGUiOiJmNGMyNGU1Mi01Y2YzLTQ2OGQtYjdkNS1lMTU3MmQ1ZTczNTEiLCJhdF9oYXNoIjoiQXhfRVNDZkF5SWtPWTFGMXI5VEQ0USIsInNpZCI6ImY0YzI0ZTUyLTVjZjMtNDY4ZC1iN2Q1LWUxNTcyZDVlNzM1MSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJkb21lbmljby5kZWd1Z2xpZWxtbyIsImVtYWlsIjoiZG9tZW5pY28uZGVndWdsaWVsbW9AZG9tby1pb3QuY29tIn0.f5yImaPxS1RJLo5IegMHQMuEUSo5N23g85FzMjDgDmjTDVZynR5cU7rPt8VYzilEGXlPGq148WIKhsw8ICwbCRQSCqbcXUwlTCDpL9SjCE0NfeOY83bDIATMhu_VDJvL9yMzzZk9N9BppPFUpBi2NjNm064TLRp4G1zjqqHEazLWJv9Pu1RmhgY35F4BWW2xNb9Bifh-7Rd1QQHFaHuS8UAcPZlpz-1UE1t42C3lcMQWnpZrZNBki8RYeZds07mwyJZwtBAnDGMo3QqSN0W5IBn7JjGORpSjspP-18oZT0FYAUt1vBxxXjxhJ0-_qFKct4wEouBLtq2vEErWOr_-DA"

header = "Authorization: Bearer " + token

ws = create_connection("ws://localhost:8300/dht-ws", header=[header])

print(ws.recv())
ws.close()