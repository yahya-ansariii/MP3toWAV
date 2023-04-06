import sys
import os
from pydub import AudioSegment

# Get the MP3 and WAV folder paths from the command line arguments
mp3_folder = sys.argv[1]
wav_folder = sys.argv[2]

# Create the output folder if it doesn't exist
if not os.path.exists(wav_folder):
    os.makedirs(wav_folder)

# Iterate over all the files in the MP3 folder
for file_name in os.listdir(mp3_folder):
    if file_name.endswith(".mp3"):
        # Set the paths for the MP3 and WAV files
        mp3_path = os.path.join(mp3_folder, file_name)
        wav_path = os.path.join(wav_folder, os.path.splitext(file_name)[0] + ".wav")

        # Load the MP3 file and export it as WAV
        sound = AudioSegment.from_mp3(mp3_path)
        sound.export(wav_path, format="wav")