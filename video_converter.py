import os
import tempfile
import moviepy.editor
import click

from pathlib import Path

BASE_DIR = os.getcwd()


@click.command()
@click.option("--input", default=BASE_DIR, help="path of the input file")
@click.option("--output", default=BASE_DIR, help="path of the output file")
def convert(input, output):
    try:
        video_path = open(input, 'rb')  # open video media as binary
    except OSError:
        print(OSError.strerror)

    tf = tempfile.NamedTemporaryFile()  # create a temporary file
    tf.write(video_path.read())  # store the binary file in temp file
    audio = moviepy.editor.VideoFileClip(tf.name).audio  # extra audio media
    tf.close()  # close the temp file to free memory

    audio_file = input.split('.')  # remove all '.' in video file name
    audio_file.pop()  # move the last element(mp4 or avi etc...) in my list
    audio_file.append('mp3')  # add mp3 like last element in my list
    audio_file = ".".join(elt for elt in audio_file)  # build the audio name
    audio_path = Path("%s/%s" % (output, audio_file))  # buid audio path

    audio.write_audiofile(audio_path)  # write audio media to audio_path


if __name__ == '__main__':
    convert()


# e.g: python script_name.py --input=path/to/video/file.mp4
# .      --output=path/to/audio/file.mp3
