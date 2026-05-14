import pandas as pd


def get_country_insight(df, country_col, country):
    filtered = df[df[country_col] == country]
    numeric = filtered.select_dtypes(include='number')

    insights = []

    for col in numeric.columns:
        val = numeric[col].values[0]
        mean_val = df[col].mean()
        if val > mean_val:
            insights.append(f"✅ **{col}**: Above global average ({val:.2f} vs {mean_val:.2f})")
        else:
            insights.append(f"⚠️ **{col}**: Below global average ({val:.2f} vs {mean_val:.2f})")

    return insights


def get_cluster_summary(df, label_col='Cluster'):
    summary = df.groupby(label_col).mean(numeric_only=True)
    return summary
