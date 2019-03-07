from lib.pubsub import sub

@sub('foo.new')
def make_another_foo(foo):
    print('subscriber making foo jams:')
    print(foo + 'jam')
