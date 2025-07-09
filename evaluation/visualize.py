def plot_anomaly_scores(scores, preds):
    plt.figure(figsize=(15, 5))
    plt.plot(scores, label='Anomaly Score')
    plt.plot(preds, label='Predicted Anomaly', alpha=0.6)
    plt.xlabel("Window Index")
    plt.ylabel("Anomaly Score")
    plt.title("Anomaly Scores & Predictions")
    plt.legend()
    plt.show()

def plot_overlay(true_labels, preds):
    plt.figure(figsize=(15, 4))
    plt.plot(true_labels, label='True Anomaly', alpha=0.7)
    plt.plot(preds, label='Predicted Anomaly', alpha=0.7)
    plt.xlabel("Window Index")
    plt.ylabel("Anomaly Label")
    plt.title("True vs Predicted Anomalies")
    plt.legend()
    plt.show()