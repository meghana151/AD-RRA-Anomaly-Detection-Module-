def create_windows(data, w_size):
    return np.array([data[i:i+w_size] for i in range(len(data)-w_size+1)])
