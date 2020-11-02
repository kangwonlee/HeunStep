from typing import Callable, Union, List, Tuple


# x would be in following form
State = Union[float, Union[List[float], Tuple[float]]]

def heun_step(f:Callable[float, State], x0:State, t0:float, t1:float) -> State:
    """
    One time step of Heun's method
    f  : function dx_dt(t0, x0)
    x0 : initial condition
    t0 : this step time
    t1 : next step time
    """

    # time step
    delta_t = t1 - t0

    # slope
    s1 = f(t0, x0)

    # next step by Euler
    x1_euler = x0 + s1 * delta_t

    # slope at next step
    s2 = f(t1, x1_euler)

    # average of two slopes
    s_average = (s1 + s2) * 0.5

    # next step by Heun's method
    x1 = x0 + s_average * delta_t

    return x1


def dx_dt(t:float, x:State) -> State:
  a0 = 1
  a1 = 1
  return (-a1 / a0 * x)
