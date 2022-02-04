import socket
import time
from collections import Counter

import ray
from fire import Fire


@ray.remote
def get_ip():
    time.sleep(0.001)
    # Return IP address.
    return socket.gethostbyname(socket.gethostname())


def run():
    ray.init(address='ray://127.0.0.1:10001')

    print('''This cluster consists of
        {} nodes in total
        {} CPU resources in total
    '''.format(len(ray.nodes()), ray.cluster_resources()['CPU']))

    object_ids = [get_ip.remote() for _ in range(10000)]
    ip_addresses = ray.get(object_ids)

    print('Tasks executed')
    for ip_address, num_tasks in Counter(ip_addresses).items():
        print('    {} tasks on {}'.format(num_tasks, ip_address))


if __name__ == '__main__':
    Fire(run)
