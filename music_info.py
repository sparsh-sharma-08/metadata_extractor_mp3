import os
from mutagen import File 

def meta_extractor(file_path, output_file):
    try:
        music_file = File(file_path)
        if music_file:
            output_file.write(f"\nProcessing: {file_path}\n")  

            # Artist Name
            if "TPE1" in music_file:
                artist_name = music_file["TPE1"]
                print(f"Artist Name: {artist_name[0]}")
                output_file.write(f"Artist Name: {artist_name[0]}\n")
            else:
                print("Artist Name: Unknown")
                output_file.write("Artist Name: Not Found\n")

            # Album Name
            if "TALB" in music_file:
                album_name = music_file["TALB"]
                print(f"Album Name: {album_name[0]}")
                output_file.write(f"Album Name: {album_name[0]}\n")
            else:
                print("Album Name: Unknown")
                output_file.write("Album Name: Not Found\n")

            # Track Number
            if "TRCK" in music_file:
                track_number = music_file["TRCK"]
                track_number = track_number[0].split("/")[0] 
                print(f"Track Number: {track_number}")
                output_file.write(f"Track Number: {track_number}\n")
            else:
                print("Track Number: Unknown")
                output_file.write("Track Number: Not Found\n")

            # Duration
            if hasattr(music_file, 'info') and hasattr(music_file.info, 'length'):
                duration = music_file.info.length
                print(f"Duration: {duration/60:.2f} minutes")
                output_file.write(f"Duration: {duration/60:.2f} minutes\n")
            else:
                print("Duration not found")
                output_file.write("Duration not found!\n")
            
            # Release Year
            if "TDRC" in music_file:
                release_year = music_file["TDRC"]
                print(f"Release Year: {release_year}")
                output_file.write(f"Release Year: {release_year[0]}\n")
            else:
                print("Release Year: Unknown")
                output_file.write("Release Year: Not Found\n")

        else:
            print(f"Could not read metadata from: {file_path}")

    except FileNotFoundError:
        print(f"No such file found: {file_path}")

    except PermissionError:
        print(f"Not enough permissions to access the file: {file_path}")

    except Exception as e:
        print(f"An error occurred while processing {file_path}: {e}")
    else:
        output_file.write("\n")  

# Define the directory containing music files
directory = "music"
# List all .mp3 files in the directory
files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(".mp3")]

# Open the output file in append mode to add metadata for each file
with open("music_metadata.txt", 'a') as output_file:
    for file_path in files:
        meta_extractor(file_path, output_file)

print("Metadata extraction complete. Data stored in 'music_metadata.txt'")
