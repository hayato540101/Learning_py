from contextlib import contextmanager

class SimpleRegistry:
    def __init__(self):
        self.default_scope = 'global'
        self.scopes = {'global': {}}

    def set(self, key, value, scope=None):
        if scope is None:
            scope = self.default_scope
        if scope not in self.scopes:
            self.scopes[scope] = {}
        self.scopes[scope][key] = value

    def get(self, key, scope=None):

        if scope is None:
            scope = self.default_scope
        return self.scopes[scope].get(key, None)

    @contextmanager
    def switch_scope(self, new_scope):

        original_scope = self.default_scope
        self.default_scope = new_scope
        if new_scope not in self.scopes:
            self.scopes[new_scope] = {}
        yield
        self.default_scope = original_scope


registry = SimpleRegistry()

registry.set('setting1', 'value1')

with registry.switch_scope('scopeA'):
    registry.set('setting1', 'valueA')
    print(f"In scopeA: {registry.get('setting1')}")

with registry.switch_scope('scopeB'):
    registry.set('setting1', 'valueB')
    print(f"In scopeB: {registry.get('setting1')}")

print(f"In global scope: {registry.get('setting1')}")
