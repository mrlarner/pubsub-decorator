SUBSCRIBERS = dict()

def _register_subscriber(event, callback):
    if event in SUBSCRIBERS:
        SUBSCRIBERS[event].append(callback)
    else:
        SUBSCRIBERS[event] = [callback]

def sub(event):
    def subscription(handler):
        def decorated_handler(*args, **kwargs):
            return handler(*args, **kwargs)
        _register_subscriber(event, handler)
        return decorated_handler
    return subscription

def pub(event, **kwargs):
    if event in SUBSCRIBERS:
        _subscribers = SUBSCRIBERS[event]
        for subscriber in _subscribers:
            subscriber(**kwargs)
    else:
        print('no subscribers for %s' % event)
