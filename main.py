from typing import Callable, Union

import numpy as np


# x would be in following form
State = Union[float, np.ndarray]
# Slope function would be in the following form
# Would take two arguments and return one argument
SlopeFunction = Callable[[float, State], State]


# Following function would calculate x of the next step
def heun_step(f:SlopeFunction, x0:State, t0:float, t1:float) -> State:
    """
    One time step of Heun's method
    f  : function dx_dt(t0, x0)
    x0 : initial condition
    t0 : this step time
    t1 : next step time
    """
    print(f"x at the current step = {x0}")
    print(f"t at the current step t0 = {t0}")
    print(f"t at the next step t1 = {t1}")

    # time step
    delta_t = t1 - t0
    print(f"delta_t = {delta_t}")

    # slope
    s1 = f(t0, x0)
    print(f"slope at t0 = {s1}")

    # next step by Euler
    x1_euler = x0 + s1 * delta_t
    print(f"estimated x at the next step by Euler's method = {x1_euler}")

    # slope at next step
    s2 = f(t1, x1_euler)
    print(f"estimated slope at t1 using x1 from Euler's method = {s1}")

    # average of two slopes
    s_average = (s1 + s2) * 0.5
    print(f"average of two slopes (({s1}) + ({s2})) / 2 = {s_average}")

    # next step by Heun's method
    x1 = x0 + s_average * delta_t

    return x1


def dx_dt(t:float, x:State) -> State:
  """
  a0 x_dot + a1 x = 0
  a0 x_dot = -a1 x
  x_dot = - (a1 * x) / a0
  """
  a0 = 1
  a1 = 0.5
  return (-a1 / a0 * x)


def main():
  t0_sec = 0.0
  t1_sec = 1.0

  x0 = 4

  x1_heun = heun_step(dx_dt, x0, t0_sec, t1_sec)
  print(f"x of Next step by Heun's method = {x1_heun}")


if "__main__" == __name__:
  main()
