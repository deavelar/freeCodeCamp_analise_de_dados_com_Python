import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv", header = 0)

# Add 'overweight' column
imc = round(df['weight'] / (df['height'] / 100) **2, 2)
imc = imc.mask(imc <= 25, 0)
imc = imc.mask(imc > 25, 1)
df['overweight'] = imc

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
cholesterol = df['cholesterol']
cholesterol = cholesterol.mask (cholesterol == 1, 0 )
cholesterol = cholesterol.mask (cholesterol > 1, 1)
df['cholesterol'] = cholesterol
gluc = df['gluc']
gluc = gluc.mask (gluc == 1, 0 )
gluc = gluc.mask (gluc > 1, 1)
df['gluc'] = gluc

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat['total'] = 1
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).sum()

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(data=df_cat, x='variable', y='total', col='cardio', kind='bar', hue='value')

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[df['ap_hi'] >= df['ap_lo']]
    df_heat = df_heat[df_heat['height'] >= df_heat['height'].quantile(0.025)]
    df_heat = df_heat[df_heat['height'] <= df_heat['height'].quantile(0.975)]
    df_heat = df_heat[df_heat['weight'] >= df_heat['weight'].quantile(0.025)]
    df_heat = df_heat[df_heat['weight'] <= df_heat['weight'].quantile(0.975)]

    # Calculate the correlation matrix
    corr = df_heat.corr(method='pearson')

    # Generate a mask for the upper triangle
    mask = np.triu(corr)


    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12,12))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, vmin=-0.2, vmax=0.7, annot=True, mask=mask, linewidths= 1)


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
