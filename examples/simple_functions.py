import ray

ray.init()


@ray.remote
def square(x):
    return x * x


results = ray.get([square.remote(i) for i in range(10)])
print(results)
