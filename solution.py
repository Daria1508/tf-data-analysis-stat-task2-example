import pandas as pd
import numpy as np
import scipy.stats as st

from scipy.stats import gamma

chat_id = 1307537098 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n=len(x)
    a1 =(1+p)/2
    a2=(1-p)/2
    z1=st.gamma.ppf(a1, a=n, scale=1/n)
    z2=st.gamma.ppf(a2, a=n, scale=1/n)
    s=sum(x)/n
    left = 2*s/(14**2) - 2/(2*14*14) + 2*z2/(14**2)
    right = 2*s/(14**2) - 2/(2*14*14) + 2*z1/(14**2)
    return left, \
           right
