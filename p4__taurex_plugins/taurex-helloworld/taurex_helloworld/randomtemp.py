from taurex.temperature import TemperatureProfile
from taurex.core import fitparam
import numpy as np


class RandomTemperature(TemperatureProfile):
    def __init__(self, base_temp=1500.0, random_scale=10.0):
        super().__init__(self.__class__.__name__)

        self._base_temp = base_temp
        self._random_scale = random_scale

    # -----Fitting Parameters--------------

    @fitparam(param_name="rand_scale", param_latex="rand")
    def randomScale(self):
        return self._random_scale

    @randomScale.setter
    def randomScale(self, value):
        self._random_scale = value

    @fitparam(param_name="base_T", param_latex="$T_{base}$")
    def baseTemperature(self):
        return self._base_temp

    @baseTemperature.setter
    def baseTemperature(self, value):
        self._base_temp = value

    # -------Actual calculation -----------

    @property
    def profile(self):
        return self._base_temp + np.random.rand(self.nlayers) * self._random_scale

    BIBTEX_ENTRIES = [
        """
        @article{myart,
            title={School of Life},
        """
    ]

    # -----Plugin related------------------

    @classmethod
    def input_keywords(cls):
        return [
            "helloworld",
            "hello-earth",
        ]
