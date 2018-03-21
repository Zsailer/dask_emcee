from dask.distributed import Client


class DaskPool(object):
    """Imitate the MPIPool class using Dask to distribute calculations.

    This will only speed up scenarios where the lnlikelihood
    function is really slow/expensive to compute. This pool distributes
    this calculation for each walker. There is a small cost for distributing
    using Dask. In cases where the likelihood calculation is fast (or the
    number of steps is high), this pool will perform significantly slower
    running in series.
    """
    def __init__(self, client):
        if isinstance(client, Client):
            self.client = client
        else:
            raise Exception("`client` must be an instance of "
                            "`dask.distributed.Client`.")

    def map(self, func, iterable):
        A = self.client.map(func, iterable)
        return self.client.gather(A)
