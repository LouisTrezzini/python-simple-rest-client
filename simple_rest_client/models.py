from collections import namedtuple

Request = namedtuple(
    'Request', ['url', 'method', 'params', 'body', 'headers', 'files', 'timeout']
)
Response = namedtuple(
    'Response', ['url', 'method', 'body', 'headers', 'status_code']
)
