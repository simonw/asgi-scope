from pprint import pformat


class App():
    def __init__(self, scope):
        self.scope = scope
        if scope['type'] != 'http':
            raise Exception()

    async def __call__(self, receive, send):
        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers': [
                [b'content-type', b'text/plain'],
            ],
        })
        await send({
            'type': 'http.response.body',
            'body': pformat(self.scope).encode('utf8'),
        })
