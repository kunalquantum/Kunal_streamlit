import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, GradientBoostingClassifier, GradientBoostingRegressor
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.svm import SVC, SVR
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, r2_score
from sklearn.preprocessing import LabelEncoder
import joblib

# Header Section
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader('Model Trainer')
with col2:
    st.image("assets/automated.jpeg", width=250)
    st.caption("We visualize, predict, and test")
with col3:
    st.write('')
# File upload
uploaded_file = st.file_uploader("Upload your dataset (CSV file)", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.header("Dataset Preview")
    st.write(data.head())

    # Choose target and dependent columns
    target_column = st.selectbox("Select the target column", data.columns)
    dependent_column = st.selectbox("Select the dependent column", data.columns)

    if target_column and dependent_column:
        st.header("Data Preprocessing")
        categorical_columns = data.select_dtypes(include=['object']).columns
        data = pd.get_dummies(data, columns=categorical_columns)
        data.fillna(0, inplace=True)
        unwanted_columns = st.multiselect("Select columns to drop", data.columns)
        data.drop(unwanted_columns, axis=1, inplace=True)

        preprocessed_data_file = "preprocessed_data.csv"
        data.to_csv(preprocessed_data_file, index=False)
        st.write(f"Preprocessed data saved to {preprocessed_data_file}")
        st.markdown(f"Download Preprocessed Data: [preprocessed_data.csv](./{preprocessed_data_file})")

        # Split data into X and y
        X = data.drop(target_column, axis=1)
        y = data[target_column]

        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Models for classification and regression
        models = {
            "RandomForestClassifier": RandomForestClassifier(),
            "GradientBoostingClassifier": GradientBoostingClassifier(),
            "LogisticRegression": LogisticRegression(max_iter=200),
            "SVC": SVC(),
            "DecisionTreeClassifier": DecisionTreeClassifier(),
            "KNeighborsClassifier": KNeighborsClassifier(),
            "GaussianNB": GaussianNB(),
            "RandomForestRegressor": RandomForestRegressor(),
            "GradientBoostingRegressor": GradientBoostingRegressor(),
            "LinearRegression": LinearRegression(),
            "SVR": SVR(),
            "DecisionTreeRegressor": DecisionTreeRegressor(),
            "KNeighborsRegressor": KNeighborsRegressor()
        }

        # Results storage
        results = []

        # Model Training and Evaluation
        st.header("Model Training and Evaluation")
        for name, model in models.items():
            with st.spinner(f"Training {name}..."):
                try:
                    # Classifier
                    if 'Classifier' in name or isinstance(model, GaussianNB):
                        model.fit(X_train, y_train)
                        y_pred = model.predict(X_test)
                        accuracy = accuracy_score(y_test, y_pred)
                        results.append({"Model": name, "Metric": "Accuracy", "Score": accuracy})
                    else:
                        # Regressor
                        model.fit(X_train, y_train)
                        y_pred = model.predict(X_test)
                        r2 = r2_score(y_test, y_pred)
                        results.append({"Model": name, "Metric": "R² Score", "Score": r2})
                except ValueError as e:
                    st.warning(f"{name} failed: {e}")
                    continue
                st.success(f"{name} training and evaluation complete!")

                # Feature Importance (if applicable)
                if hasattr(model, "feature_importances_"):
                    st.write(f"Feature Importance for {name}:")
                    importances = model.feature_importances_
                    feature_names = X.columns
                    feat_importances = pd.Series(importances, index=feature_names)
                    feat_importances.nlargest(10).plot(kind='barh')
                    st.pyplot()

        # Display results in a table
        st.header("Model Performance Summary")
        results_df = pd.DataFrame(results)
        st.table(results_df)

        # Visualizations for Target and Dependent Variable
        st.header("Distribution Visualizations")
        
        # Box Plot for Target Variable
        st.write("Box Plot of Target Variable:")
        plt.figure(figsize=(8, 6))
        sns.boxplot(y)
        st.pyplot()

        # Box Plot for Dependent Variable
        st.write(f"Box Plot of Dependent Variable ({dependent_column}):")
        plt.figure(figsize=(8, 6))
        sns.boxplot(data[dependent_column])
        st.pyplot()
