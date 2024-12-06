import ray

# ray.init()


@ray.remote
def mapper(chunk):
    return sum(chunk)


@ray.remote
def reducer(results):
    return sum(results)


chunks = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mapped_results = [mapper.remote(chunk) for chunk in chunks]
resolved_results = ray.get(mapped_results)
final_result = ray.get(reducer.remote(resolved_results))
print(final_result)  # Output: 45
