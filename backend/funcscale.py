from abc import ABC

from matplotlib import rcParams
from matplotlib import scale as scale
from matplotlib.ticker import (
    Formatter, NullFormatter, NullLocator, AutoLocator, AutoMinorLocator)


def forward(x):
    return x / 1000


def inverse(x):
    return x * 1000


class FuncTransform(scale.Transform, ABC):
    """
    A simple transform that takes and arbitrary function for the
    forward and inverse transform.
    """

    input_dims = 1
    output_dims = 1
    is_separable = True
    has_inverse = True

    def __init__(self, forward_fun, inverse_fun):
        """
        Parameters
        ----------

        forward_fun : callable
            The forward function for the transform.  This function must have
            an inverse and, for best behavior, be monotonic.
            It must have the signature::

               def forward(values: array-like) -> array-like

        inverse_fun : callable
            The inverse of the forward function.  Signature as ``forward``.
        """
        super().__init__()
        if callable(forward_fun) and callable(inverse_fun):
            self._forward = forward_fun
            self._inverse = inverse_fun
        else:
            raise ValueError('arguments to FuncTransform must '
                             'be functions')

    def transform_non_affine(self, values):
        return self._forward(values)

    def inverted(self):
        return FuncTransform(self._inverse, self._forward)


class FuncFormatter(Formatter):
    """
    Use a user-defined function for formatting.

    The function should take in two inputs (a tick value ``x`` and a
    position ``pos``), and return a string containing the corresponding
    tick label.
    """

    def __init__(self, func):
        self.func = func

    def __call__(self, x, pos=None):
        """
        Return the value of the user defined function.

        `x` and `pos` are passed through as-is.
        """
        return int(self.func(x))


class FuncScale(scale.ScaleBase):
    """
    Provide an arbitrary scale with user-supplied function for the axis.
    """

    name = 'user_function'

    def __init__(self, axis, functions):
        """
        Parameters
        ----------

        axis: the axis for the scale

        functions : (callable, callable)
            two-tuple of the forward and inverse functions for the scale.
            The forward function must be monotonic.

            Both functions must have the signature::

               def forward(values: array-like) -> array-like
        """
        forward_fun, inverse_fun = functions
        transform = FuncTransform(forward_fun, inverse_fun)
        self._transform = transform

    def get_transform(self):
        """
        The transform for arbitrary scaling
        """
        return self._transform

    def set_default_locators_and_formatters(self, axis):
        """
        Set the locators and formatters to the same defaults as the
        linear scale.
        """
        axis.set_major_locator(AutoLocator())
        axis.set_major_formatter(FuncFormatter(self._transform._forward))
        axis.set_minor_formatter(NullFormatter())
        # update the minor locator for x and y axis based on rcParams
        if (axis.axis_name == 'x' and rcParams['xtick.minor.visible']
                or axis.axis_name == 'y' and rcParams['ytick.minor.visible']):
            axis.set_minor_locator(AutoMinorLocator())
        else:
            axis.set_minor_locator(NullLocator())


class FuncScale1000(FuncScale):
    name = 'funcscale1000'

    def __init__(self, axis):
        functions = (forward, inverse)
        super().__init__(axis, functions)
