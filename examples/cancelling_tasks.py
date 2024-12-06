import time
import ray


@ray.remote
def blocking_operation():
    time.sleep(10e6)


obj_ref = blocking_operation.remote()
ray.cancel(obj_ref)

try:
    ray.get(obj_ref)
except ray.exceptions.TaskCancelledError:
    print("Object reference was cancelled.")
