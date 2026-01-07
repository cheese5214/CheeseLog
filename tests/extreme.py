import concurrent.futures, os, time

import __init__
from CheeseLog import CheeseLogger

def task(logger: CheeseLogger):
    for _ in range(100000):
        logger.debug('Extreme stress test log message.')

if __name__ == '__main__':
    now = time.time()

    if os.path.exists('logs/extreme.log'):
        os.remove('logs/extreme.log')
    logger = CheeseLogger('logs/extreme.log')

    max_workers = os.cpu_count()
    # with concurrent.futures.ProcessPoolExecutor(max_workers = max_workers) as executor:
    with concurrent.futures.ThreadPoolExecutor(max_workers = max_workers) as executor:
        for future in concurrent.futures.as_completed([executor.submit(task, logger) for i in range(max_workers)]):
            future.result()
