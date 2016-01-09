import hash_ring

def setup():
    nodes = ['hawkeye', 'scarlet widow', 'iron man', 'pepper', 'rhody']
    ring = hash_ring.HashRing(nodes=nodes)
    return ring, nodes

def test_add():
    """
    Test adding nodes
    """
    ring,_ = setup()
    ring.add_node('jackson pollock')
    ring.add_node('iron man')

def test_seen():
    """
    Ensure that after a large number of random lookups, all nodes have
    been represented.
    """
    ring,nodes = setup()
    seen = set()
    possible = set(nodes)
    for i in range(1000):
        seen.add(ring.get_node(str(i)))
    diff = possible - seen
    assert len(diff) == 0, "Keys differ %s" % diff

"""
Test removing nodes
"""
def test_remove():
    ring,nodes = setup()
    ring.remove_node('iron man')

    seen = set()
    possible = set(nodes)
    for i in range(50):
        seen.add(ring.get_node(str(i)))
    diff = possible - seen
    assert len(diff) == 1, "Were %d key(s) missing, should be only 1" % len(diff)

