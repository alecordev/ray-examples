"""
@ray.remote(concurrency_groups={"io": 2})
class AsyncIOActor:
    async def f1(self):
        pass

actor = AsyncIOActor.options(max_concurrency=10).remote()

# Setting concurrency at runtime

# Executed in the "io" group (as defined in the actor class).
a.f2.options().remote()

# Executed in the "compute" group.
a.f2.options(concurrency_group="compute").remote()
"""

import ray


@ray.remote(concurrency_groups={"io": 2, "compute": 4})
class AsyncIOActor:
    def __init__(self):
        pass

    @ray.method(concurrency_group="io")
    async def f1(self):
        pass

    @ray.method(concurrency_group="io")
    async def f2(self):
        pass

    @ray.method(concurrency_group="compute")
    async def f3(self):
        pass

    @ray.method(concurrency_group="compute")
    async def f4(self):
        pass

    async def f5(self):
        pass


a = AsyncIOActor.remote()
a.f1.remote()  # executed in the "io" group.
a.f2.remote()  # executed in the "io" group.
a.f3.remote()  # executed in the "compute" group.
a.f4.remote()  # executed in the "compute" group.
a.f5.remote()  # executed in the default group.
