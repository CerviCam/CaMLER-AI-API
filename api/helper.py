def parse_bytes_to_json(data):
    return json.loads(data.decode('utf-8'))

def path(url, handler, **kwargs):
    def add_to_app(app):
        app.add_url_rule(url, None, handler, **kwargs)

    return add_to_app