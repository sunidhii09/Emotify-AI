# Speech Emotion Recognition Music System

Welcome to our project repository! This project presents a practical implementation of a music system that utilizes speech emotion recognition to recommend personalized playlists based on the user’s emotional state. Our goal is to enhance the user's mood by providing music that resonates with their current emotions.

## Overview

The core idea behind our system is to leverage Convolutional Neural Networks (ConvNet) for classifying emotions from speech input and an AI-driven playlist generation mechanism to curate music playlists tailored to the recognized emotion class. Specifically, we employ the following components:

- **Speech Emotion Recognition**: We use ConvNet to analyze speech input and classify the underlying emotion. This allows us to understand the user's emotional state based on their voice.
  
- **Playlist Generation**: Utilizing K Means clustering, we organize music tracks into playlists based on similar characteristics such as genre, tempo, and mood. This enables us to create diverse playlists that cater to various emotional states.
  
- **Recommendation System**: Our AI-driven system recommends live playlists to the user based on the recognized emotion class. By aligning the music with the user's emotions, we aim to elevate their mood and enhance their listening experience.

## How It Works

1. **Input**: The user provides speech input, which is processed by the speech emotion recognition model.
  
2. **Emotion Classification**: The ConvNet analyzes the speech input and predicts the user's emotional state, such as happiness, sadness, excitement, etc.
  
3. **Playlist Generation**: Based on the predicted emotion class, our system selects music tracks from the pre-clustered playlists that best match the user's emotional context.
  
4. **Recommendation**: The recommended playlist is presented to the user, offering a tailored music experience designed to uplift their mood and enhance their well-being.

## Getting Started

To get started with using our system, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine.
  
2. **Install Dependencies**: Ensure you have all the necessary dependencies installed. You can find the requirements in the `requirements.txt` file.
  
3. **Run the System**: Execute the main script to start the music system. Follow the instructions for providing speech input, and enjoy the personalized playlists!
