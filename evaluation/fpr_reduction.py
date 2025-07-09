def reduce_false_positives(predictions, min_anomaly_length=5):
    smoothed_preds = predictions.copy()
    start = None
    for i in range(len(predictions)):
        if predictions[i] == 1 and start is None:
            start = i
        elif predictions[i] == 0 and start is not None:
            length = i - start
            if length < min_anomaly_length:
                smoothed_preds[start:i] = 0
            start = None
    if start is not None:
        length = len(predictions) - start
        if length < min_anomaly_length:
            smoothed_preds[start:] = 0
    return smoothed_preds