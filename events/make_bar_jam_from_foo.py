from lib.pubsub import sub

@sub('foo.new')
def make_bar_jam_from_foo(foo):
    print('subscriber making bar jams:')
    print 'barjam'+foo
