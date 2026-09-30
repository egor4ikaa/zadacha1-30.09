import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

delivery_delay = ctrl.Antecedent(np.arange(0, 31, 1), 'delivery_delay')
quality_defects = ctrl.Antecedent(np.arange(0, 21, 0.5), 'quality_defects')
completeness = ctrl.Antecedent(np.arange(70, 101, 1), 'completeness')
price_deviation = ctrl.Antecedent(np.arange(-15, 16, 1), 'price_deviation')
payment_delay = ctrl.Antecedent(np.arange(0, 61, 1), 'payment_delay')

reliability = ctrl.Consequent(np.arange(0, 101, 1), 'reliability')

delivery_delay['low'] = fuzz.trimf(delivery_delay.universe, [0, 0, 10])
delivery_delay['medium'] = fuzz.trimf(delivery_delay.universe, [5, 15, 25])
delivery_delay['high'] = fuzz.trimf(delivery_delay.universe, [15, 30, 30])

quality_defects['low'] = fuzz.trimf(quality_defects.universe, [0, 0, 5])
quality_defects['medium'] = fuzz.trimf(quality_defects.universe, [2, 10, 18])
quality_defects['high'] = fuzz.trimf(quality_defects.universe, [10, 20, 20])

completeness['low'] = fuzz.trimf(completeness.universe, [70, 70, 85])
completeness['medium'] = fuzz.trimf(completeness.universe, [80, 90, 95])
completeness['high'] = fuzz.trimf(completeness.universe, [90, 100, 100])

price_deviation['favorable'] = fuzz.trimf(price_deviation.universe, [-15, -15, -2])
price_deviation['agreed'] = fuzz.trimf(price_deviation.universe, [-5, 0, 5])
price_deviation['overpriced'] = fuzz.trimf(price_deviation.universe, [2, 15, 15])

payment_delay['low'] = fuzz.trimf(payment_delay.universe, [0, 0, 20])
payment_delay['medium'] = fuzz.trimf(payment_delay.universe, [10, 30, 50])
payment_delay['high'] = fuzz.trimf(payment_delay.universe, [30, 60, 60])

reliability['low'] = fuzz.trimf(reliability.universe, [0, 0, 45])
reliability['medium'] = fuzz.trimf(reliability.universe, [30, 55, 75])
reliability['high'] = fuzz.trimf(reliability.universe, [60, 100, 100])

rule1 = ctrl.Rule(delivery_delay['low'] & quality_defects['low'] & completeness['high'] & price_deviation['agreed'] & payment_delay['low'], reliability['high'])
rule2 = ctrl.Rule(delivery_delay['low'] & quality_defects['low'] & completeness['high'] & price_deviation['favorable'] & payment_delay['low'], reliability['high'])
rule3 = ctrl.Rule(delivery_delay['low'] & quality_defects['low'] & completeness['medium'] & price_deviation['agreed'] & payment_delay['low'], reliability['high'])
rule4 = ctrl.Rule(delivery_delay['medium'] & quality_defects['medium'] & completeness['medium'] & price_deviation['agreed'] & payment_delay['medium'], reliability['medium'])
rule5 = ctrl.Rule(delivery_delay['medium'] & quality_defects['medium'] & completeness['medium'] & price_deviation['favorable'] & payment_delay['low'], reliability['medium'])
rule6 = ctrl.Rule(delivery_delay['medium'] & quality_defects['low'] & completeness['medium'] & price_deviation['agreed'] & payment_delay['low'], reliability['medium'])
rule7 = ctrl.Rule(delivery_delay['high'] & quality_defects['high'] & completeness['low'] & price_deviation['overpriced'] & payment_delay['high'], reliability['low'])
rule8 = ctrl.Rule(delivery_delay['high'] & quality_defects['high'] & completeness['low'] & price_deviation['agreed'] & payment_delay['high'], reliability['low'])
rule9 = ctrl.Rule(delivery_delay['high'] & quality_defects['medium'] & completeness['low'] & price_deviation['overpriced'] & payment_delay['high'], reliability['low'])
rule10 = ctrl.Rule(delivery_delay['high'] & quality_defects['medium'] & completeness['low'] & price_deviation['agreed'] & payment_delay['medium'], reliability['low'])
rule11 = ctrl.Rule(delivery_delay['medium'] & quality_defects['low'] & completeness['high'] & price_deviation['agreed'] & payment_delay['low'], reliability['high'])
rule12 = ctrl.Rule(delivery_delay['medium'] & quality_defects['medium'] & completeness['medium'] & price_deviation['overpriced'] & payment_delay['medium'], reliability['low'])
rule13 = ctrl.Rule(delivery_delay['high'] & quality_defects['low'] & completeness['medium'] & price_deviation['agreed'] & payment_delay['low'], reliability['medium'])
rule14 = ctrl.Rule(delivery_delay['low'] & quality_defects['medium'] & completeness['medium'] & price_deviation['agreed'] & payment_delay['medium'], reliability['medium'])
rule15 = ctrl.Rule(delivery_delay['high'] & quality_defects['high'] & completeness['medium'] & price_deviation['overpriced'] & payment_delay['medium'], reliability['low'])
rule16 = ctrl.Rule(delivery_delay['low'] & quality_defects['medium'] & completeness['high'] & price_deviation['agreed'] & payment_delay['low'], reliability['high'])
rule17 = ctrl.Rule(delivery_delay['low'] & quality_defects['high'] & completeness['medium'] & price_deviation['agreed'] & payment_delay['low'], reliability['medium'])
rule18 = ctrl.Rule(delivery_delay['medium'] & quality_defects['high'] & completeness['medium'] & price_deviation['agreed'] & payment_delay['medium'], reliability['low'])
rule19 = ctrl.Rule(delivery_delay['high'] & quality_defects['low'] & completeness['low'] & price_deviation['agreed'] & payment_delay['medium'], reliability['low'])
rule20 = ctrl.Rule(delivery_delay['low'] & quality_defects['low'] & completeness['low'] & price_deviation['agreed'] & payment_delay['high'], reliability['medium'])
rule21 = ctrl.Rule(delivery_delay['medium'] & quality_defects['low'] & completeness['high'] & price_deviation['favorable'] & payment_delay['low'], reliability['high'])
rule22 = ctrl.Rule(delivery_delay['high'] & quality_defects['medium'] & completeness['medium'] & price_deviation['agreed'] & payment_delay['low'], reliability['medium'])
rule23 = ctrl.Rule(delivery_delay['low'] & quality_defects['medium'] & completeness['medium'] & price_deviation['favorable'] & payment_delay['low'], reliability['medium'])
rule24 = ctrl.Rule(delivery_delay['medium'] & quality_defects['medium'] & completeness['high'] & price_deviation['agreed'] & payment_delay['low'], reliability['high'])
rule25 = ctrl.Rule(delivery_delay['high'] & quality_defects['high'] & completeness['high'] & price_deviation['overpriced'] & payment_delay['high'], reliability['low'])

reliability_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
    rule20, rule21, rule22, rule23, rule24, rule25])
reliability_sim = ctrl.ControlSystemSimulation(reliability_ctrl)

def calculate_reliability(dd, qd, comp, pd, payd):
    reliability_sim.input['delivery_delay'] = dd
    reliability_sim.input['quality_defects'] = qd
    reliability_sim.input['completeness'] = comp
    reliability_sim.input['price_deviation'] = pd
    reliability_sim.input['payment_delay'] = payd
    
    try:
        reliability_sim.compute()
        # Безопасное получение результата
        score = reliability_sim.output.get('reliability', None)
        
        # Если система не смогла вычислить — ставим 0
        if score is None:
            score = 0.0
    except Exception as e:
        print(f"  [!] Ошибка вычисления для входов ({dd}, {qd}, {comp}, {pd}, {payd}): {e}")
        score = 0.0
    
    if score < 40:
        level = 'низкая'
    elif score < 70:
        level = 'средняя'
    else:
        level = 'высокая'
        
    return round(score, 2), level