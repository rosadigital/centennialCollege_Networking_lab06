import numpy as np
import matplotlib.pyplot as plt

class SensorSimulator:
    def __init__(self, high_value=21, low_value=18, noise_factor=0.1, peak_variation=0.5):
        """
        Simulates a sensor reading values between a given range.
        
        Args:
            high_value (float): The maximum realistic sensor value.
            low_value (float): The minimum realistic sensor value.
            noise_factor (float): Controls the random noise added to values.
            peak_variation (float): Controls the variation of peaks and valleys.
        """
        self.high_value = high_value
        self.low_value = low_value
        self.noise_factor = noise_factor
        self.peak_variation = peak_variation
        self._step = 0

    def generate_value(self):
        """
        Generates a single float value in the range [0, 1) with peaks and variations.
        """
        base_wave = (np.sin(self._step / 20) + 1) / 2  # Smooth wave
        peaks = np.sin(self._step / 50) * np.random.uniform(0.5, 1)  # Randomized peaks
        noise = np.random.uniform(-self.noise_factor, self.noise_factor)  # Small noise

        generated_value = base_wave * (1 - self.peak_variation) + peaks * self.peak_variation + noise
        generated_value = np.clip(generated_value, 0, 1)  # Ensure within [0,1)
        
        self._step += 1
        return generated_value

    def get_transformed_value(self):
        """
        Transforms the generated value into the realistic sensor range.
        """
        raw_value = self.generate_value()
        return raw_value * (self.high_value - self.low_value) + self.low_value


# Instantiate SensorSimulator
sensor = SensorSimulator()

# Generate 500 sensor readings
data_points = [sensor.get_transformed_value() for _ in range(500)]

# Plot the sensor data
plt.figure(figsize=(10, 2))
plt.plot(data_points, color='green', linewidth=1)
plt.title("Simulated Sensor Readings")
plt.xlabel("Time (arbitrary units)")
plt.ylabel("Sensor Value")
plt.show()
