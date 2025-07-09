def scale_values(values):
    scaler = StandardScaler()
    scaled = scaler.fit_transform(values.reshape(-1, 1)).flatten()
    return scaled, scaler