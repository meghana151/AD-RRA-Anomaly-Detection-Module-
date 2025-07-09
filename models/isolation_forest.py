def train_isolation_forest(X_train_flat, contamination=0.05):
    model = IsolationForest(contamination=contamination, random_state=42)
    model.fit(X_train_flat)
    return model