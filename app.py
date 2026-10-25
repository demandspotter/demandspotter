import streamlit as st
import sqlite3
import pandas as pd

# Page Configuration
st.set_page_config(page_title="TrendScout SaaS MVP", page_icon="📈", layout="wide")

# Connect to database
def load_data():
    conn = sqlite3.connect('products.db')
    df = pd.read_sql_query("SELECT * FROM trending_products", conn)
    conn.close()
    return df

st.title("📈 TrendScout - Winning Product Discovery")
st.markdown("Find your next high-margin e-commerce product before it goes viral.")

try:
    df = load_data()
except Exception as e:
    st.error("Database not found. Please run database_seeder.py first.")
    st.stop()

# Sidebar Filters
st.sidebar.header("Filter Products")
selected_category = st.sidebar.selectbox("Select Niche", ["All Categories"] + list(df['category'].unique()))
min_margin = st.sidebar.slider("Minimum Profit Margin ($)", 0, 50, 10)

# Filter Data
filtered_df = df if selected_category == "All Categories" else df[df['category'] == selected_category]
filtered_df = filtered_df[filtered_df['profit_margin'] >= min_margin]

# Main Dashboard Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Products Found", len(filtered_df))
col2.metric("Highest Profit Margin", f"${filtered_df['profit_margin'].max()}" if not filtered_df.empty else "$0")
col3.metric("Top Trend Score", f"{filtered_df['trend_score'].max()}/100" if not filtered_df.empty else "0/100")

st.divider()

# Display Products
st.subheader("🔥 Today's Trending Products")

if filtered_df.empty:
    st.warning("No products match your current filters.")
else:
    for index, row in filtered_df.iterrows():
        with st.container():
            col_a, col_b, col_c = st.columns([3, 1, 1])
            with col_a:
                st.markdown(f"### {row['product_name']}")
                st.caption(f"Category: {row['category']} | Trend Score: {row['trend_score']}/100")
            with col_b:
                st.markdown(f"**Supplier Price:** ${row['supplier_price']:.2f}")
                st.markdown(f"**Suggested Retail:** ${row['selling_price']:.2f}")
            with col_c:
                st.success(f"Profit: ${row['profit_margin']:.2f}")
                if st.button("Export to Shopify", key=row['id']):
                    st.toast(f"Exported {row['product_name']} (Premium Feature Mockup)")
            st.divider()

# Premium Gate (Mockup)
st.sidebar.divider()
st.sidebar.markdown("### Upgrade to Pro")
st.sidebar.markdown("Unlock live AliExpress scraping, TikTok ad analytics, and 1-click store integration for just **$15/mo**.")
st.sidebar.button("Upgrade Now")
