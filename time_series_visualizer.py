import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
# Use Pandas to import the data from "fcc-forum-pageviews.csv". Set the index to the date column
df = pd.read_csv("fcc-forum-pageviews.csv")

# Clean data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset
df = df[(df['value'] > df['value'].quantile(0.025)) &
        (df['value'] < df['value'].quantile(0.975))]


def draw_line_plot():
    """
    Create a draw_line_plot function that uses Matplotlib:
    The title should be Daily freeCodeCamp Forum Page Views 5/2016-12/2019.
    The label on the x axis should be Date.
    The label on the y axis should be Page Views.
    :return: fig
    """
    fig, ax = plt.subplots()
    ax.plot(df.index, df['value'])
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    """
    Create a draw_bar_plot show average daily page views for each month grouped by year:
    The legend should show month labels and have a title of Months.
    The label on the x axis should be Years.
    The label on the y axis should be Average Page Views.
    :return: fig
    """
    df['date'] = pd.to_datetime(df['date'])
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_bar = df_box.groupby(['year', 'month'])['value'].mean().unstack()

    # Draw bar plot
    fig, ax = plt.subplots()
    df_bar.plot(kind='bar', ax=ax)
    ax.set_title('Average Daily Page Views per Month')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    plt.legend(title='Months',
               labels=['January', 'February', 'March', 'April',
                       'May', 'June', 'July', 'August',
                       'September', 'October', 'November', 'December'])

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    """
    Create a draw_box_plot that show how values are distributed within a given year/month and how it compares over time:
    The title of the 1st chart should be Year-wise Box Plot (Trend)
    The title of the 2nd chart should be Month-wise Box Plot (Seasonality).
    Make sure the month labels on bottom start at Jan and the x and y axis are labeled correctly.
    :return: fig
    """
    df['date'] = pd.to_datetime(df['date'])
    df['value'] = df['value'].astype(float)

    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')

    # Draw box plots (using Seaborn)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"] 
    
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(4, 12))
    
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0]) 
    axes[0].set_title('Year-wise Box Plot (Trend)') 
    axes[0].set_xlabel('Year') 
    axes[0].set_ylabel('Page Views') 
    
    sns.boxplot(x='month', y='value', data=df_box, ordered=months, ax=axes[1]) 
    axes[1].set_title('Month-wise Box Plot (Seasonality)') 
    axes[1].set_xlabel('Month') 
    axes[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
