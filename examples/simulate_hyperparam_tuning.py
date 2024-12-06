import ray


@ray.remote
def evaluate_hyperparameter(param):
    return param**2


params = [1, 2, 3, 4, 5]
results = ray.get([evaluate_hyperparameter.remote(p) for p in params])
print(results)
