import os
import time
import ray


@ray.remote
def process_file(filename):
    time.sleep(5)
    return f"Processed {filename}"


files = [f"file_{i}.txt" for i in range(10)]
results = ray.get([process_file.remote(file) for file in files])
print(results)
