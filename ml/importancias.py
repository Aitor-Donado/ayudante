import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def grafica_importancias(model):
    # Get feature importances from the model
    importances = model.feature_importances_

    # Get feature names from X.columns
    # feature_names = X.columns
    feature_names = model.get_feature_names_out() if hasattr(model, 'get_feature_names_out') else model.get_feature_names()

    # Create a DataFrame for better visualization
    feature_importance_df = pd.DataFrame({
        'Feature': feature_names,
        'Importance': importances
    })

    # Sort the features by importance in descending order
    feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

    # Create the bar plot
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Importance', y='Feature', data=feature_importance_df, palette='viridis', hue='Feature')
    plt.title('Importancia de las Características en el modelo entrenado')
    plt.xlabel('Importancia')
    plt.ylabel('Características')
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.show()