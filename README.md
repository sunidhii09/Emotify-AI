# EMOTIFY:  LIVE MUSIC RECOMMENDATIONS BASED ON YOUR MOOD

This project presents a practical implementation of a music system using speech emotion recognition (SER) to recommend personalized playlists based on the user’s emotional state. The goal is to enhance the user's mood by providing music that resonates with their current emotions.

## Overview

The core idea behind this system is to leverage Convolutional Neural Networks (ConvNet) with Long Short Term Memory (LSTM) networks for classifying emotions from speech input and an AI-driven playlist generation mechanism to curate music playlists tailored to the recognized emotion class. Specifically, the following components have been employed:

- **Speech Emotion Recognition**: ConvNet with LSTM is used to analyze speech input and classify the underlying emotion. This allows us to understand the user's emotional state based on their voice.
  
- **Playlist Generation**: Utilizing K Means clustering to organize music tracks into playlists based on similar characteristics such as genre, tempo, and danceability. This enables us to create diverse playlists that cater to various emotional states.
  
Our AI-driven system recommends live playlists to the user based on the recognized emotion class. By aligning the music with the user's emotions, we aim to elevate their mood and enhance their listening experience.

## How It Works

1. **Input**: The user provides speech input (.wav) file, which is processed by the speech-emotion recognition model.
  
2. **Emotion Classification**: The ConvNet analyzes the speech input and predicts the user's emotional state, categorized into 8 classes: such as happy, sad, calm, surprise, angry, fearful, disgust and neutral.
  
3. **Playlist Generation**: Based on the predicted emotion class, the system selects music tracks from the pre-clustered playlists (Spotify API used as the soruce) that best match the user's emotional context.

The recommended playlist is presented to the user, offering a tailored music experience designed to uplift their mood and enhance their well-being.

## Getting Started

To get started with using our system, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine.
  
2. **Install Dependencies**: Ensure you have all the necessary dependencies installed.
  
3. **Run the System**: Execute the 'playlist_generation.ipynb' script  to start the music system, input your file and enjoy the personalized playlists!

## Collaborators
https://github.com/Shivanant


