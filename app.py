from pprint import pformat


async def app(scope, receive, send):
    await send(
        {
            "type": "http.response.start",
            "status": 200,
            "headers": [[b"content-type", b"text/plain"],],
        }
    )
    await send(
        {"type": "http.response.body", "body": pformat(scope).encode("utf8"),}
    )
