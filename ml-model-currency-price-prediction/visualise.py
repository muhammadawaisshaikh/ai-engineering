import matplotlib.pyplot as plt
import pandas as pd

class Visualiser:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def plot_currency_trend(self):
        """Plot historical USD/EUR exchange rate"""
        plt.figure(figsize=(14, 8))
        plt.plot(self.data['Date'], self.data['USD_EUR'], label='USD to EUR', linewidth=1.5)
        plt.title("USD to EUR Exchange Rate Over Time", fontsize=16, fontweight='bold')
        plt.xlabel("Date", fontsize=12)
        plt.ylabel("Exchange Rate (USD per EUR)", fontsize=12)
        plt.legend(fontsize=12)
        
        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45)
        
        # Format y-axis to show fewer decimal places and avoid overlapping
        plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.3f'))
        
        # Adjust layout to prevent label cutoff
        plt.tight_layout()
        plt.grid(True, alpha=0.3)
        plt.show()