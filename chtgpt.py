import numpy as np

class KalmanFilter:
    def __init__(self, initial_state, observation_matrix, process_noise, observation_noise, transition_matrix):
        self.state = initial_state
        self.observation_matrix = observation_matrix
        self.process_noise = process_noise
        self.observation_noise = observation_noise
        self.transition_matrix = transition_matrix
        self.covariance = np.zeros((len(initial_state), len(initial_state)))
    
    def predict(self):
        self.state = np.dot(self.transition_matrix, self.state)
        self.covariance = np.dot(np.dot(self.transition_matrix, self.covariance), self.transition_matrix.T) + self.process_noise
        
    def update(self, measurement):
        kalman_gain = np.dot(np.dot(self.covariance, self.observation_matrix.T), np.linalg.inv(np.dot(np.dot(self.observation_matrix, self.covariance), self.observation_matrix.T) + self.observation_noise))
        self.state = self.state + np.dot(kalman_gain, (measurement - np.dot(self.observation_matrix, self.state)))
        self.covariance = np.dot((np.identity(len(self.state)) - np.dot(kalman_gain, self.observation_matrix)), self.covariance)

# Define initial state, observation matrix, process noise, observation noise, and transition matrix
initial_state = np.array([0, 0])
observation_matrix = np.array([[1, 0], [0, 1]])
noise = 0.4
process_noise = np.eye(2) * noise
observation_noise = np.eye(2) * noise
transition_matrix = np.array([[1, 0.1], [0, 1]])

# Create the filter
filter = KalmanFilter(initial_state, observation_matrix, process_noise, observation_noise, transition_matrix)

# Generate some measurements
measurements = np.array([[1, 1], [2, 2], [3, 3]])

# Run the filter on the measurements
for measurement in measurements:
    filter.predict()
    filter.update(measurement)
    print(filter.state)
