from unittest.mock import Mock
m = Mock()
print(m.any_attribute())
print(m.foo)
print(m.any_method())
print(m.foo())
print(m.called)
print(m.foo.called)
m.bar.return_value = 1
print(m.bar())
