from pydub import AudioSegment
import openai

API_KEY = 'yourAPI_KEY'

model_id = 'whisper-1'

# Load the audio file
audio_file_path = 'audio_Name.mp3'
audio_extention = audio_file_path.split('.')[-1]
audio_file = AudioSegment.from_file(audio_file_path, format=audio_extention)

# Defining time
one_second = 1000
one_minute = 60 * one_second
chunk_unit = one_minute

# Calculate the total duration of the audio file in milliseconds
total_duration_seconds = round(audio_file.duration_seconds + 5)

# Define the length of each chunk in milliseconds
total_duration_milliseconds = total_duration_seconds * 1000

#chunks counter
j=0

# Specify the path and name of the text file to create
chemin_fichier = 'myText.txt'

# Iterate over the audio file, segment by segment
for i in range(0, total_duration_milliseconds, chunk_unit):
    # Calculate the start and end positions of the current chunk
    start_time =i
    end_time = min(i + chunk_unit, total_duration_milliseconds)

    # Extract the current chunk from the audio file
    chunk = audio_file[start_time:end_time]

    #Increment j 
    j=j+1

    #file Path of the chunk audios 
    media_file_path = "Mychunk"+ str(j)+'.mp3'

    # Save the current chunk as a separate audio file
    chunk.export(media_file_path, format="mp3") 

    media_file = open(media_file_path, 'rb')

    response = openai.Audio.transcribe(
        api_key=API_KEY,
        model=model_id,
        file=media_file,
        response_format='text'
    )

   

    # Open the file in write mode
    with open(chemin_fichier, 'a') as fichier:
        # Write the text to the file
        fichier.write(response)

    # Display a confirmation message
    print("Partie "+str(j)+" créée avec succès")  

