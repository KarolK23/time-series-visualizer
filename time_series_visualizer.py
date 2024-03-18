import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col='date')

# Clean data
q025 = df['value'].quantile(0.025)
q975 = df['value'].quantile(1-0.025)
df = df[ (df['value'] > q025) & (df['value'] < q975) ]
df.index = pd.to_datetime(df.index)


def draw_line_plot():
    # Draw line plot

    fig = plt.figure(figsize=(12,5))
    plt.plot(df, color = 'red')
    plt.xlabel("Date")
    plt.ylabel("Page Views")

    # Save image and return fig (don't change this part)

    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    df_bar['Years'] = df_bar.index.year
    df_bar['Months'] = df_bar.index.month

    df_bar = df_bar.pivot_table(index='Years',
                columns='Months',
                values='value',
                aggfunc='mean')

    df_bar.columns = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    # Draw bar plot

    fig, ax = plt.subplots(figsize=(10, 6)) 

    df_bar.plot(kind='bar', ax=ax)

    plt.xlabel('Years')
    plt.ylabel('Average Page Views') 

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    months_in_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    fig = plt.figure(figsize=(15,5))
    plt.subplot(1,2,1)
    sns.boxplot(data=df_box, x='year', y='value', hue = "year", palette="muted")
    plt.subplot(1,2,2)
    sns.boxplot(data=df_box, x='month', y='value', hue = "month", palette="muted", order=months_in_order)




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
