# Music Metadata Extractor

-> Overview
This project extracts metadata from audio files (specifically .mp3 files) and generates a report containing the following details:

1) Artist Name
2) Album Name
3) Track Number
4) Duration
5) Release Year
- The extracted metadata is saved in a text file (music_metadata.txt). The script works by scanning all .mp3 files in the specified directory and processes each one individually.

# Features
- Extract metadata from multiple .mp3 files in a directory.
- Handle missing metadata gracefully (e.g., "Not Found" or "Unknown").
- Outputs a report in a .txt file for easy access and analysis.
- Handles basic errors such as file not found or permission issues.

# Requirements
1) Python 3.x
2) mutagen library (used for handling audio file metadata)

# How It Works
The script will scan all .mp3 files in the music/ directory.
For each file, it attempts to extract the following metadata:
Artist Name, Album Name, Track Number, Duration, Release Year
The metadata is written to a file called music_metadata.txt, with each file's metadata clearly separated for easy reading.
