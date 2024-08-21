import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_excel('citizenship-datasets.xlsx', sheet_name='Data - Cit_D02', skiprows=1)


df.columns = df.iloc[0]  # Set the first row as the header
df = df[1:]  # Remove the first row which is now the header

# Drop any columns with all NaN values (if necessary)
df = df.dropna(axis=1, how='all')

filtered_df = df[(df['Year'] == 2024) & (df['Nationality'] == 'Sweden')]

result_df = filtered_df[['Year', 'Application type group', 'Nationality', 'Grants']]

# Set a Seaborn style for the plot
sns.set(style="whitegrid")

# Create a color palette
palette = sns.color_palette("coolwarm", len(result_df['Application type group'].unique()))

# Create the bar plot
plt.figure(figsize=(12, 8))
ax = sns.barplot(x='Application type group', y='Grants', data=result_df, 
                 estimator=sum, palette=palette, edgecolor='black', ci=None)

# Annotate the total grants on each bar with advanced formatting
for p in ax.patches:
    height = p.get_height()
    ax.annotate(f'{int(height):,}',  # Format numbers with commas
                (p.get_x() + p.get_width() / 2., height),
                ha='center', va='center',
                xytext=(0, 12),  # Move text slightly above the bar
                textcoords='offset points',
                fontsize=12, color='black', fontweight='bold')

# Add a title with custom font properties
plt.title('British citizenship grants by Application Type for Sweden citizen in 2024', 
          fontsize=18, fontweight='bold', color='darkblue', pad=20)

# Customize the x and y axis labels
plt.xlabel('Application Type Group', fontsize=14, fontweight='bold')
plt.ylabel('Total Grants', fontsize=14, fontweight='bold')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, fontsize=12)

# Add grid lines
ax.yaxis.grid(True, color='gray', linestyle='--', linewidth=0.7)
ax.xaxis.grid(False)

# Remove top and right spines for a cleaner look
sns.despine()

# Display the plot
plt.tight_layout()
plt.show()