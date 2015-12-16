__author__ = 'joe'
# -*- coding: utf-8 -*-

class NotFlask():
    def __init__(self):
        self.routes = {}

    def route(self, route_str):
        def decorator(f):
            self.routes[route_str] = f
            return f
        return decorator

    def serve(self, path):
        view_function = self.routes.get(path)
        if view_function:
            return view_function()
        else:
            raise ValueError('Route "{}" has not been registered'.format(path))



app = NotFlask()

@app.route('/')
def hello():
    return "hello world"

print(app.serve('/'))

class TestNotFlask(unittest.Testcase):
    def setUp(self):
        self.app = NotFlask()

    def test_valid_route(self):
        @self.app.route('/')
        def index():
            return 'hello world'

        self.assertEqual(self.app.serve('/'), 'Hello World')

    def test_invalid_route(self):
        with self.assertRaises(ValueError):
            self.app.serve('/invalid')