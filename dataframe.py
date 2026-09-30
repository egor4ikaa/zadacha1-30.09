import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl



def generate_data(n=850, seed=42):
    rng = np.random.default_rng(seed)

    delivery_delay = rng.integers(0, 31, n)
    quality_defects = rng.integers(0, 21, n)
    completeness = rng.integers(70, 101, n)
    price_deviation = rng.integers(-15, 16, n)
    payment_delay = rng.integers(0, 61, n)

    data = pd.DataFrame({
        'delivery_delay': delivery_delay,
        'quality_defects': quality_defects, 
        'completeness': completeness,
        'price_deviation': price_deviation, 
        'payment_delay': payment_delay
    })
    data.to_csv("suppliers.csv", index=False)
    print("Файл suppliers.csv сохранен")
    return data

def get_test_suppliers():
    data = pd.DataFrame({
        'delivery_delay': [2, 12, 25, 8, 18],
        'quality_defects': [1, 7, 15, 3, 12], 
        'completeness': [98, 92, 75, 95, 80],
        'price_deviation': [-2, 0, 10, 3, 5], 
        'payment_delay': [5, 20, 50, 10, 35]
    }, index=['Поставщик_A', 'Поставщик_B', 'Поставщик_C', 'Поставщик_D', 'Поставщик_E'])
    return data




