# 🧠 Customer Segmentation using K-Means Clustering

This project applies unsupervised machine learning (K-Means Clustering) to group customers based on purchasing behavior using the popular Mall Customers dataset.

## 📌 Problem Statement

Companies need to segment customers to personalize marketing strategies. This project helps identify distinct customer groups based on Annual Income and Spending Score.

## 🔧 Technologies Used

- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- Streamlit (for interactive web app)

## 🚀 How It Works

1. Load customer data (Mall_Customers.csv)
2. Visualize the data distribution
3. Apply K-Means clustering
4. Determine optimal number of clusters using Elbow Method
5. Visualize clusters and their insights
6. Deploy an interactive web app with Streamlit

## 💻 Run Locally

```bash
git clone https://github.com/meenakshirathod11/customer-segmentation.git
cd customer-segmentation
pip install -r requirements.txt
streamlit run app.py
