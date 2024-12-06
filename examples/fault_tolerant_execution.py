import ray


@ray.remote(max_retries=3)
def unstable_task(x):
    if x % 2 == 0:
        raise ValueError("Simulated failure!")
    return x


results = [unstable_task.remote(i) for i in range(5)]
print(ray.get(results))
