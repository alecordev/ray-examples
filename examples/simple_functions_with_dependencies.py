import ray


@ray.remote
def add(x, y):
    return x + y


@ray.remote
def multiply(x, y):
    return x * y


a = add.remote(1, 2)
b = multiply.remote(a, 10)
result = ray.get(b)
print(result)
