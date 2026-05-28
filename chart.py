import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("Untitled spreadsheet - Sheet1.csv")
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Keep only relevant columns
df_clean = df[['Vuosi', 'Muu', 'Pro-eheytyshoito, anti-trans']]


# Define colors
colors = ['#1f77b4', '#ff7f0e']  # blue and orange

# Create stacked bar chart with wider bars
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.8  # default is 0.8, increase for wider bars (0.9–1.0 looks good)

bars_muu = ax.bar(df_clean['Vuosi'], df_clean['Muu'], color=colors[0], width=bar_width)
bars_anti = ax.bar(df_clean['Vuosi'], df_clean['Pro-eheytyshoito, anti-trans'],
                   bottom=df_clean['Muu'], color=colors[1], width=bar_width)

# Add larger numeric labels inside bars
for bar in bars_muu:
    height = bar.get_height()
    if height > 0:
        ax.text(bar.get_x() + bar.get_width() / 2, height / 2,
                f'{int(height)}', ha='center', va='center',
                color='white', fontsize=12, fontweight='bold')

for bar_muu, bar_anti in zip(bars_muu, bars_anti):
    height_muu = bar_muu.get_height()
    height_anti = bar_anti.get_height()
    if height_anti > 0:
        ax.text(bar_muu.get_x() + bar_muu.get_width() / 2,
                height_muu + height_anti / 2,
                f'{int(height_anti)}', ha='center', va='center',
                color='white', fontsize=18, fontweight='bold')

# Titles and labels
ax.set_title('Tapausten jakautuminen vuosittain', fontsize=14)
ax.set_xlabel('Vuosi', fontsize=10)
ax.set_ylabel('Lukumäärä', fontsize=10)
ax.set_xticks(df_clean['Vuosi'])
ax.set_xticklabels(df_clean['Vuosi'].astype(str), fontsize=12)

# Remove all spines (frame)
for spine in ax.spines.values():
    spine.set_visible(False)

# Remove tick marks
ax.tick_params(left=False, bottom=False)

# Light background
ax.set_facecolor('#fafafa')
fig.patch.set_facecolor('white')

plt.tight_layout()
plt.savefig("P2.PNG")
plt.show()
