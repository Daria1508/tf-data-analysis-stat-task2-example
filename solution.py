import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1307537098 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n=len(x)
    a1=(1-p)/2
    a2=(1+p)/2
    left = (2*(-np.log(a1)+min(x)-1/2))/(14**2)
    right = (2*(-np.log(a2)+max(x)-1/2))/(14**2)
    return left, \
           right
