import tensorflow as tf
from tensorflow import keras
import librosa
import numpy as np

# Load the trained model
model = keras.models.load_model('my_model.keras')

# Preprocess the audio
def preprocess_audio():
    # Load the audio file
    audio_data, sr = librosa.load(audio_file, sr=None)
    # Compute the mel spectrogram 
    spectrogram = librosa.feature.melspectrogram(y=audio_data, sr=sr)
    # Resize the spectrogram to match the input shape of the model
    resized_spectrogram = np.resize(spectrogram, (model.input_shape[1], 1))
    return np.expand_dims(resized_spectrogram, axis=0)

# Make predictions
audio_file = 'Recording2.wav'
def make_predictions():
    preprocessed_audio = preprocess_audio()
    predictions = model.predict(preprocessed_audio)
    predicted_class = np.argmax(predictions)
    return predicted_class

# Test on a .wav file
make_predictions()