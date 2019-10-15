import numpy as np
import scipy.optimize as op
import emcee
import corner
import matplotlib.pyplot as pl
from Astropy import newmodel, intensitydata, iterations, parameters

# Choose the "true" parameters.
ci_true = 7.86
br_true = 6.256
g_true = -0.122
t_true = 1.57
b_true = 1.833
f_true = 0.534

# Generate some synthetic data from the model.
x = iterations
yerr = 0.5*np.random.random()
ys = intensitydata


# A = np.vstack((np.ones_like(x), x)).T
# C = np.diag(yerr * yerr)
# cov = np.linalg.inv(np.dot(A.T, np.linalg.solve(C, A)))
# b_ls, m_ls = np.dot(cov, np.dot(A.T, np.linalg.solve(C, ys)))


def lnlike(theta, x, y, yerr):

    ci, br, g, t, b, lnf = theta
    model = newmodel(ci, br, g, t, b)[0]
    inv_sigma2 = 1.0/(yerr**2 + model**2*np.exp(2*lnf))

    return -0.5*(np.sum((y-model)**2*inv_sigma2 - np.log(inv_sigma2)))


nll = lambda *args: -lnlike(*args)
result = op.minimize(nll, [ci_true, br_true, g_true, t_true, b_true, np.log(f_true)], args=(x, ys, yerr))
ci_ml, br_ml, g_ml, t_ml, b_ml, lnf_ml = result["x"]


def lnprior(theta):

    ci, br, g, t, b, lnf = theta
    if 5 < ci < 10 and 0.0 < br < 10.0 and -1 < g < 1 and 0 < t < 5 and 0 < b < 5 and -10.0 < lnf < 1.0:
        return 0.0

    return -np.inf


def lnprob(theta, x, y, yerr):

    lp = lnprior(theta)
    if not np.isfinite(lp):
        return -np.inf

    return lp + lnlike(theta, x, y, yerr)


ndim, nwalkers = 6, 100
pos = [result["x"] + 1e-4*np.random.randn(ndim) for i in range(nwalkers)]

sampler = emcee.EnsembleSampler(nwalkers, ndim, lnprob, args=(x, ys, yerr))
sampler.run_mcmc(pos, 500)
samples = sampler.chain[:, 50:, :].reshape((-1, ndim))
fig = corner.corner(samples, labels=["$I0$", "$rb$", "$g$", "$t$", "$b$", "$\ln\,f$"],
                    truths=[ci_true, br_true, g_true, t_true, b_true, np.log(f_true)])

pl.figure()
for ci, br, g, t, b, lnf in samples[np.random.randint(len(samples), size=100)]:
    pl.plot(x, newmodel(ci, br, g, t, b)[0], color="k", alpha=0.1)
pl.plot(x, newmodel(ci_true, br_true, g_true, t_true, b_true)[0], color="r", lw=2, alpha=0.8)
pl.errorbar(x, ys, yerr=yerr, fmt=".k")
pl.show()
samples[:, 2] = np.exp(samples[:, 2])
ci_mcmc, br_mcmc, g_mcmc, t_mcmc, b_mcmc, f_mcmc = map(lambda v: (v[1], v[2]-v[1], v[1]-v[0]),
                                                       zip(*np.percentile(samples, [16, 50, 84], axis=0)))

