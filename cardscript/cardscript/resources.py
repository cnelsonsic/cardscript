class Resource(object):
    '''Resources are the ephemeral energy that sits on the stack.'''
    def __init__(self):
        self.resource_color = set(['any'])


class FireResource(Resource):
    def __init__(self):
        super(FireResource, self).__init__()
        self.resource_color.add('fire')
