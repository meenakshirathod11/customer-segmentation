import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load Data
df = pd.read_csv('mall_customers.csv')
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# Streamlit UI
st.title("Customer Segmentation using K-Means Clustering")

# Choose number of clusters
k = st.slider('Choose number of clusters (K)', 1, 10, 5)

# Train model
model = KMeans(n_clusters=k, random_state=42)
df['Cluster'] = model.fit_predict(X)

# Show results
st.subheader("Clustered Data")
st.write(df.head())

# Plot
fig, ax = plt.subplots()
scatter = ax.scatter(X['Annual Income (k$)'], X['Spending Score (1-100)'], 
                     c=df['Cluster'], cmap='viridis')
centers = model.cluster_centers_
ax.scatter(centers[:, 0], centers[:, 1], c='red', s=200, marker='X')
ax.set_xlabel("Annual Income (k$)")
ax.set_ylabel("Spending Score (1-100)")
ax.set_title("Customer Segments")
st.pyplot(fig)
