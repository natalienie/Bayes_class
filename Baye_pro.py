import matplotlib.pyplot as pyplot
import numpy as np


class SortedDictionary(object):
    def __init__(self, keys, values):
        self._keys = keys
        self._values = values
    def __getitem__(self, key):
        try:
            return self._values[self._keys.index(key)]
        except ValueError:
            print(key)
            raise KeyError('This value is not in the SortedDictionary')
    def __setitem__(self, key, value):
        try:
            self._values[self._keys.index(key)] = Value
        except ValueError:
            self._keys.append(key)
            self._values.append(value)
    def keys(self):
        return self._keys

    def values(self):
        return self._values

    def __iter__(self):
        for val in self.keys():
            yield val

    def max_value(self):
        return max(self.values())

    def __repr__(self):
        return str(['%s : %s' % (k,v) for k,v in zip(self.keys(), self.values())]).replace(']', '}')


class Bayes(object):
    def __init__(self, prior=SortedDictionary([], [])):
        assert isinstance(prior, SortedDictionary)
        self.counter = 0
        self.prior = prior
        self.normalize()

    def normalize(self):
        possibility_sum = sum(self.prior.values())
        for possibility in self.prior.keys():
            self.prior[possibility] /= possibility_sum

    def likelihood(self, outcome, hypothesis):
        raise Exception('Not Implemented')

    def update(self, outcome):
        self.counter += 1
        for hypothesis in self.prior:
            self.prior[hypothesis] *= self.likelihood(outcome, hypothesis)
        self.normalize()

    def plot(self, loc=2):
        plt.plot(self.prior.keys(),
                 self.prior.values(),
                 label='Iteration: %s' % self.counter)
        plt.legend(loc=loc)
        plt.xlabel('Hypothesis for Probability of Heads')
        plt.ylabel('Likelihood of Hypothesis being True')

    def max_likelihood(self):
        return self.prior.keys()[self.prior.values().index(self.prior.max_value())]

class BayeUniform(Bayes):
    def __init__(self):
        points = list(np.linspace(0, 1, 100))
        self.points = list(np.linspace(0, 1, 100))
        prior = SortedDictionary(points, [1.0] * 100)
        super(BayeUniform, self).__init__(prior)
