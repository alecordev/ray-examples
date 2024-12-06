from collections import Counter
import socket
import time

import ray

ray.init()

print(
    """This cluster consists of
    {} nodes in total
    {} CPU resources in total
""".format(
        len(ray.nodes()), ray.cluster_resources()["CPU"]
    )
)
