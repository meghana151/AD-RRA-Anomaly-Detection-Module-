def compute_ensemble_scores(autoencoder, iforest, X_test_windows):
    reconstruction_errors = []
    isolation_scores = []
    
    for window in X_test_windows:
        recon = autoencoder.predict(window[np.newaxis, :, :], verbose=0)
        error = np.mean((recon - window[np.newaxis, :, :])**2)
        reconstruction_errors.append(error)

        score = -iforest.decision_function(window.reshape(1, -1))[0]
        isolation_scores.append(score)

    ensemble_scores = 0.5 * np.array(reconstruction_errors) + 0.5 * np.array(isolation_scores)
    return ensemble_scores