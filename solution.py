import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1307537098 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n=len(x)
    alpha = 1 - p
    left = (-min(-x) - 1 / 2) / (14**2 / 2)
    right = (-np.log(alpha) / n -min(-x) - 1 / 2) / (14**2 / 2)
    return left, \
           right
