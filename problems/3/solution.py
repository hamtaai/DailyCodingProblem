import json


def do_serialize(root):
    item = {
        'val': root.val,
    }

    if hasattr(root, 'left') and isinstance(root.left, Node):
        item['left'] = do_serialize(root.left)

    if hasattr(root, 'right') and isinstance(root.right, Node):
        item['right'] = do_serialize(root.right)

    return item


def serialize(root):
    return json.dumps(do_serialize(root))


def do_deserialize(s):
    if 'val' not in s:
        return None

    return Node(
        s['val'],
        do_deserialize(s['left']) if 'left' in s else None,
        do_deserialize(s['right']) if 'right' in s else None
    )


def deserialize(s):
    return do_deserialize(json.loads(s))


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
