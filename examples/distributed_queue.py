import ray


@ray.remote
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return None


queue = Queue.remote()
ray.get(queue.enqueue.remote("task1"))
ray.get(queue.enqueue.remote("task2"))
print(ray.get(queue.dequeue.remote()))
print(ray.get(queue.dequeue.remote()))
