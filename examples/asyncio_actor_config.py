import asyncio
import ray


@ray.remote
class AsyncActor:
    async def run_task(self):
        print("started")
        await asyncio.sleep(1)  # Network, I/O task here
        print("ended")


actor = AsyncActor.options(max_concurrency=2).remote()

# Only 2 tasks will be running concurrently. Once 2 finish, the next 2 should run.
ray.get([actor.run_task.remote() for _ in range(8)])
