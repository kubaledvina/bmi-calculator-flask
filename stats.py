import sqlite3
import matplotlib.pyplot as plt
from collections import defaultdict



def load_data():
    conn = sqlite3.connect("bmi_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT age, bmi FROM users")
    data = cursor.fetchall()
    conn.close()

    return data


def plot_bmi(data, save_path="static/bmi_chart.png"):
    bmi_by_age = defaultdict(list)

    # Seskupení BMI podle věku
    for age, bmi in data:
        bmi_by_age[age].append(bmi)

    # Výpočet průměrného BMI pro každý věk
    ages = sorted(bmi_by_age.keys())
    avg_bmis = [round(sum(bmi_by_age[age]) / len(bmi_by_age[age]), 2) for age in ages]

    # Vykreslení grafu
    plt.bar(ages, avg_bmis, color='green')
    plt.title("Average BMI to age.")
    plt.xlabel("Age")
    plt.ylabel("Average BMI")
    plt.xticks(ages, rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()

    plt.savefig(save_path)
    plt.close()

if __name__ == "__main__":
    data = load_data()
    if data:
        plot_bmi(data)
    else:
        print("No dat in database")