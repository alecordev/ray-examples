import ray


@ray.remote
def long_running_task():
    import time

    time.sleep(5)
    return "Done"


result_id = long_running_task.remote()
print("Task started...")
print(ray.get(result_id))
