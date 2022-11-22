import ubinascii
import picoweb
import customnetwork
customnetwork.setupSTA()

app = picoweb.WebApp(__name__)

def index(req, resp):
    if b"Authorization" not in req.headers:
        yield from resp.awrite(
            'HTTP/1.0 401 NA\r\n'
            'WWW-Authenticate: Basic realm="Picoweb Realm"\r\n'
            '\r\n'
        )
        return

    auth = req.headers[b"Authorization"].split(None, 1)[1]
    auth = ubinascii.a2b_base64(auth).decode()
    username, passwd = auth.split(":", 1)
    yield from picoweb.start_response(resp)
    yield from resp.awrite("You logged in with username: %s, password: %s" % (username, passwd))


import ulogging as logging
logging.basicConfig(level=logging.INFO)

app.run(debug=True, host = customnetwork.getIP(), port = 80)