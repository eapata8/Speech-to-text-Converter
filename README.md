# Speech to text converter

This Python script allows you to convert a large audio file into text using the OpenAI API. The script divides the audio file into smaller chunks and transcribes each chunk individually, writing the corresponding text to a text file. This can be useful for tasks such as transcription, speech recognition, or generating subtitles for audio content.

## Prerequisites

To use this script, you need to have the following:

- Python installed on your system
- The `pydub` library installed (`pip install pydub`)
- An OpenAI API key
- The `openai` library installed (`pip install openai`)
- An audio or video file in a supported format (e.g., MP3, WAV, MP4)
- install the ffmpeg library

## Setup

1. Install the required Python library by running the following command:
   ```
   pip install pydub
   ```

2. Sign up for an OpenAI account and obtain an API key.

3. Set the `API_KEY` variable in the script to your OpenAI API key.

4. Install the ffmpeg library

5. Install the required openai library by running the following command:
   ```
   pip install openai
   ```
   

## Usage

1. Place the audio file that you want to convert into the same directory as the script.

2. Update the `audio_file_path` variable in the script to the name of your audio file.

3. Run the script. It will divide the audio file into chunks and transcribe each chunk individually. The resulting text will be saved to a text file named `myText.txt`.

4. Once the script finishes, you can find the transcribed text in the `myText.txt` file.

## Note

Please note that the accuracy of the transcription depends on the audio quality and the performance of the underlying speech recognition model. You can experiment with different OpenAI models or adjust the chunk size to improve the results.

Feel free to customize and integrate this script into your own projects as needed.
