dask_emcee
----------

**Emcee in parallel using Dask.**

This package defines a ``DaskPool`` object that distributes the walker
lnlikelihood calculations in emcee using a Dask client.

.. code-block:: python

  import numpy as np
  import emcee

  # Import relevant Dask objects
  from dask_emcee import DaskPool, Client

  def lnprob(x, ivar):
      return -0.5 * np.sum(ivar * x ** 2)

  ndim, nwalkers = 10, 100
  ivar = 1. / np.random.rand(ndim)
  p0 = [np.random.rand(ndim) for i in range(nwalkers)]

  # Initialize a Dask client and Pool to pass to emcee.
  client = Client()
  pool = DaskPool(client)

  # Run sampler with the pool argument.
  sampler = emcee.EnsembleSampler(nwalkers, ndim, lnprob, args=[ivar], pool=pool)
  sampler.run_mcmc(p0, 1000)


This is just a concept piece. I'm planning to put thought into making this more
efficient and effective.
