import plotly.express as px
import pandas as pd


def plot_correlation_heatmap(df):
    numeric = df.select_dtypes(include='number')
    fig = px.imshow(
        numeric.corr(),
        color_continuous_scale='RdBu_r',
        title='Correlation Heatmap'
    )
    return fig


def plot_histogram(df, column, nbins=30):
    fig = px.histogram(
        df, x=column, nbins=nbins,
        color_discrete_sequence=['cyan'],
        title=f'Distribution of {column}'
    )
    return fig


def plot_boxplot(df, column):
    fig = px.box(df, y=column, title=f'Boxplot of {column}')
    return fig


def plot_scatter_clusters(plot_df, hover_col):
    fig = px.scatter(
        plot_df,
        x='PCA1',
        y='PCA2',
        color='Cluster',
        hover_name=hover_col,
        size_max=20,
        title='Cluster Visualization (PCA)'
    )
    return fig


def plot_choropleth(df, color_col):
    fig = px.choropleth(
        df,
        locations='Country',
        locationmode='country names',
        color=color_col,
        hover_name='Country',
        color_continuous_scale='Viridis',
        title=f'Global Map: {color_col}'
    )
    return fig
