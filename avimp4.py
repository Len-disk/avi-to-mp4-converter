import ffmpeg
import os

def convert_avi_to_mp4(input_file, output_file):
    try:
        # Comando profesional: Usamos el codec H.264 y audio AAC
        (
            ffmpeg
            .input(input_file)
            .output(output_file, vcodec='libx264', acodec='aac', strict='experimental')
            .overwrite_output()
            .run(capture_stdout=True, capture_stderr=True)
        )
        return True
    except ffmpeg.Error as e:
        print(f"Error en la conversión: {e.stderr.decode()}")
        return False