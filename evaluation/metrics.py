def get_true_labels(df_channel, window_size):
    true_labels = []
    for i in range(len(df_channel) - window_size + 1):
        window = df_channel['anomaly'].iloc[i:i+window_size]
        true_labels.append(int(window.mode()[0]))
    return true_labels

def evaluate_predictions(true_labels, preds, scores):
    print("Classification Report:")
    print(classification_report(true_labels, preds))
    print("Confusion Matrix:")
    print(confusion_matrix(true_labels, preds))
    
    auc = roc_auc_score(true_labels, scores)
    print(f"ROC AUC Score: {auc:.4f}")
    
    precision, recall, _ = precision_recall_curve(true_labels, scores)
    ap = average_precision_score(true_labels, scores)
    
    plt.figure(figsize=(8, 6))
    plt.plot(recall, precision, label=f'AP={ap:.3f}')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall Curve')
    plt.legend()
    plt.show()

    return auc, ap
