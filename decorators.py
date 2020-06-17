from time import perf_counter
from functools import wraps
from datetime import datetime, timezone

def timed(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        args_ = [str(a) for a in args]
        kwargs_ = [f"{k}={v}" for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ", ".join(all_args)

        print(f"{fn.__name__}({args_str}) took {elapsed:.6f}s to run.")

        return result
    return inner


def timed_avg(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        elapsed_total = 0
        elapsed_count = 0

        for i in range(10):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            elapsed = end - start
            elapsed_total += elapsed
            elapsed_count += 1

        args_ = [str(a) for a in args]
        kwargs_ = [f"{k}={v}" for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ", ".join(all_args)

        elapsed_avg = elapsed_total / elapsed_count
        print(f"{fn.__name__}({args_str}) took on average",
              f"{elapsed_avg:.6f}s to run.",
              f"Averaged over {elapsed_count} times")

        return result
    return inner


# TODO: Functionality to log to disk instead of prompt
# TODO: Log called parameters
def logged(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print(f"{run_dt} - Running {fn.__name__}")
        return result
    return inner
