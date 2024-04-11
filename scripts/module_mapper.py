class Registry:
    def __init__(self):
        self.module_dict = {}

    def register_module(self, name, module):
        self.module_dict[name] = module

    def build_module(self, name, *args, **kwargs):
        module_class = self.module_dict[name]
        return module_class(*args, **kwargs)

registry = Registry()

class ResNet:
    def __init__(self, layers):
        self.layers = layers

    def forward(self):
        return f'ResNet with {self.layers} layers'

class SEResNet:
    def __init__(self, layers):
        self.layers = layers

    def forward(self):
        return f'SEResNet with {self.layers} layers'

registry.register_module('ResNet', ResNet)
registry.register_module('SE-ResNet', SEResNet)

resnet = registry.build_module('ResNet', layers=50)
seresnet = registry.build_module('SE-ResNet', layers=101)

print(resnet.forward())
print(seresnet.forward())
