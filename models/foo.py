from lib.pubsub import pub

def new():
    print('model making a new foo')
    pub('foo.new', foo='foo')
    return 'foo'
