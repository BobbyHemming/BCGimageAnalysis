import numpy as np
import scipy.optimize as op
import emcee
import corner
import matplotlib.pyplot as pl
from Astropy import newmodel, m, rarcsecs, parameters

# Choose the "true" parameters.
ci_true = 7.86
br_true = 6.256
b_true = 1.91
f_true = 0.1

# Generate some synthetic data from the model.
x = rarcsecs
yerr = 0.5*np.random.random()
ys = m


# A = np.vstack((np.ones_like(x), x)).T
# C = np.diag(yerr * yerr)
# cov = np.linalg.inv(np.dot(A.T, np.linalg.solve(C, A)))
# b_ls, m_ls = np.dot(cov, np.dot(A.T, np.linalg.solve(C, ys)))


def lnlike(theta, x, y, yerr):

    ci, br, b, lnf = theta
    model = newmodel(ci, br, parameters[2], parameters[3], parameters[4])[0]
    inv_sigma2 = 1.0/(yerr**2 + model**2*np.exp(2*lnf))

    return -0.5*(np.sum((y-model)**2*inv_sigma2 - np.log(inv_sigma2)))


nll = lambda *args: -lnlike(*args)
result = op.minimize(nll, [ci_true, br_true, b_true, np.log(f_true)], args=(x, ys, yerr))
ci_ml, br_ml, b_ml, lnf_ml = result["x"]


def lnprior(theta):

    ci, br, b, lnf = theta
    if -5.0 < ci < 0.5 and 0.0 < br < 10.0 and 0.0 < b < 10 -10.0 < lnf < 1.0:
        return 0.0

    return -np.inf


def lnprob(theta, x, y, yerr):

    lp = lnprior(theta)
    if not np.isfinite(lp):
        return -np.inf

    return lp + lnlike(theta, x, y, yerr)


ndim, nwalkers = 4, 3000
pos = [result["x"] + 1e-4*np.random.randn(ndim) for i in range(nwalkers)]

sampler = emcee.EnsembleSampler(nwalkers, ndim, lnprob, args=(x, ys, yerr))
sampler.run_mcmc(pos, 500)
samples = sampler.chain[:, 50:, :].reshape((-1, ndim))
fig = corner.corner(samples, labels=["$I0$", "$rb$", '$b$', "$\ln\,f$"], truths=[ci_true, br_true, b_true, np.log(f_true)])

pl.figure()
for ci, br, b, lnf in samples[np.random.randint(len(samples), size=100)]:
    pl.plot(x, newmodel(ci, br, parameters[2], parameters[3], b)[0], color="k", alpha=0.1)
pl.plot(x, newmodel(ci_true, br_true, parameters[2], parameters[3], b_true)[0], color="r", lw=2, alpha=0.8)
pl.errorbar(x, ys, yerr=yerr, fmt=".k")
pl.show()
samples[:, 2] = np.exp(samples[:, 2])
ci_mcmc, br_mcmc, b_mcmc, f_mcmc = map(lambda v: (v[1], v[2]-v[1], v[1]-v[0]), zip(*np.percentile(samples, [16, 50, 84], axis=0)))

