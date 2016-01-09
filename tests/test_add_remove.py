import hash_ring

def setup():
    """
    Create a simple HashRing for testing.
    """
    nodes = ['hawkeye', 'scarlet widow', 'iron man', 'pepper', 'rhody'] # Assemble!
    ring = hash_ring.HashRing(nodes=nodes)
    return ring, nodes

def try_many(n, ring, nodes):
    """
    Return the number of
    """
    seen = set()
    possible = set(nodes)
    for i in range(1000):
        seen.add(ring.get_node(str(i)))
    diff = possible - seen
    return diff

def test_add():
    """
    Test adding nodes
    """
    ring,nodes = setup()
    ring.add_node('jackson pollock')
    diff = try_many(1000, ring, nodes)
    assert len(diff) == 0, "Not all keys represented after addition"

def test_seen():
    """
    Ensure that after a large number of random lookups, all nodes have
    been represented.
    """
    ring,nodes = setup()
    diff = try_many(1000, ring, nodes)
    assert len(diff) == 0, "Keys differ, but shouldn't: %s" % diff

"""
Test removing nodes
"""
def test_remove():
    ring,nodes = setup()
    ring.remove_node('iron man')
    diff = try_many(1000, ring, nodes)
    assert len(diff) == 1, "Were %d key(s) missing, should be only 1" % len(diff)
