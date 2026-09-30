import matplotlib.pyplot as plt
from function import delivery_delay, quality_defects, completeness, price_deviation, payment_delay, reliability

def plot_membership():
    fig, axes = plt.subplots(3, 2, figsize=(14, 12))
    axes = axes.flatten()
    
    vars_list = [
        (delivery_delay, 'Задержка поставки'),
        (quality_defects, 'Дефекты'),
        (completeness, 'Полнота'),
        (price_deviation, 'Отклонение цены'),
        (payment_delay, 'Просрочка оплаты'),
        (reliability, 'Надежность (выход)')
    ]
    
    for ax, (var, title) in zip(axes, vars_list):
        for term_name in var.terms:
            ax.plot(var.universe, var[term_name].mf, label=term_name)
        ax.set_title(title)
        ax.legend()
        
    axes[-1].axis('off')
    plt.tight_layout()
    plt.savefig('membership.png')
    plt.show()

def plot_distribution(df):
    plt.figure(figsize=(10, 5))
    plt.hist(df['reliability_score'], bins=30, color='skyblue', edgecolor='black')
    plt.title('Распределение индекса надежности')
    plt.xlabel('Индекс (0-100)')
    plt.ylabel('Количество')
    plt.axvline(40, color='red', linestyle='--')
    plt.axvline(70, color='green', linestyle='--')
    plt.savefig('distribution.png')
    plt.show()