import pandas as pd
import numpy as np


chat_id = 784664358 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    
    
    mean = x.mean()
    var = x.var()
    return 0.5*np.log((mean-743)**4 / (var+(mean-743)**2)) # Ваш ответ
