import pandas as pd
from dataframe import generate_data, get_test_suppliers
from function import calculate_reliability
from grafic import plot_membership, plot_distribution

def process_dataframe(df):
    scores = []
    levels = []
    
    for index, row in df.iterrows():
        s, l = calculate_reliability(
            row['delivery_delay'],
            row['quality_defects'],
            row['completeness'],
            row['price_deviation'],
            row['payment_delay']
        )
        scores.append(s)
        levels.append(l)
        
    df['reliability_score'] = scores
    df['reliability_level'] = levels
    return df

def menu():
    while True:
        print("\n1. Графики функций принадлежности")
        print("2. Тест 5 поставщиков")
        print("3. Генерация 850 поставщиков + график")
        print("4. Ввод нового поставщика")
        print("5. Выход")
        
        choice = input("Выбор: ")
        
        if choice == '1':
            plot_membership()
            
        elif choice == '2':
            df = get_test_suppliers()
            df = process_dataframe(df)
            print(df[['reliability_score', 'reliability_level']])
            
        elif choice == '3':
            df = generate_data(850)
            df = process_dataframe(df)
            print(f"Средний индекс: {df['reliability_score'].mean():.2f}")
            print(df['reliability_level'].value_counts())
            plot_distribution(df)
            
        elif choice == '4':
            dd = float(input("Задержка (0-30): "))
            qd = float(input("Дефекты (0-20): "))
            comp = float(input("Полнота (70-100): "))
            pd_val = float(input("Цена (-15..15): "))
            payd = float(input("Оплата (0-60): "))
            
            score, level = calculate_reliability(dd, qd, comp, pd_val, payd)
            print(f"Результат: {score} ({level})")
            
        elif choice == '5':
            break

if __name__ == '__main__':
    menu()