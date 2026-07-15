import os
import tempfile

import librosa
import librosa.display
import matplotlib.pyplot as plt


class WaveformGenerator:

    def generate_preview(self, file_object):

        # Create temporary storage for uploaded audio
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav"
        ) as temporary_file:

            temporary_file.write(
                file_object.getbuffer()
            )

            temporary_audio_path = (
                temporary_file.name
            )

        # Read audio signal
        audio_signal, sample_rate = librosa.load(
            temporary_audio_path,
            sr=None
        )

        # Build waveform figure
        figure, axis = plt.subplots(
            figsize=(12, 3)
        )

        librosa.display.waveshow(
            audio_signal,
            sr=sample_rate,
            ax=axis,
            color="#1f77b4"
        )

        axis.set_title(
            "Speech Signal Visualization"
        )

        axis.set_xlabel(
            "Time Duration (seconds)"
        )

        axis.set_ylabel(
            "Signal Strength"
        )

        plt.tight_layout()

        return figure


    def export_waveform(self, source_audio):

        # Create output folder if missing
        os.makedirs(
            "assets",
            exist_ok=True
        )

        image_location = os.path.join(
            "assets",
            "speech_waveform.png"
        )

        # Load recording
        signal, sr = librosa.load(
            source_audio,
            sr=None
        )

        plt.figure(
            figsize=(10, 3)
        )

        librosa.display.waveshow(
            signal,
            sr=sr,
            color="#2a9df4"
        )

        plt.title(
            "Speech Waveform Analysis"
        )

        plt.xlabel(
            "Time"
        )

        plt.ylabel(
            "Amplitude"
        )

        plt.tight_layout()

        plt.savefig(
            image_location,
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        return image_location
