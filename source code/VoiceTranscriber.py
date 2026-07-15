import os
import tempfile
import whisper


class VoiceTranscriber:
    """
    Handles conversion of speech recordings
    into textual transcripts using Whisper.
    """

    def __init__(self):
        """
        Initialize the speech recognition model.
        """
        self.whisper_model = whisper.load_model(
            "tiny"
        )

    def convert_to_text(
        self,
        audio_file
    ):
        """
        Parameters
        ----------
        audio_file : UploadedFile
            Audio file uploaded through Streamlit.

        Returns
        -------
        tuple
            (generated_text, saved_audio_path)
        """

        try:

            # Preserve original extension
            file_extension = os.path.splitext(
                audio_file.name
            )[1]

            # Store file temporarily
            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=file_extension
            ) as temp_audio:

                temp_audio.write(
                    audio_file.read()
                )

                saved_path = (
                    temp_audio.name
                )

            # Generate transcript
            transcription_result = (
                self.whisper_model.transcribe(
                    saved_path
                )
            )

            generated_text = (
                transcription_result[
                    "text"
                ].strip()
            )

            return (
                generated_text,
                saved_path
            )

        except Exception as error:

            raise Exception(
                f"Transcription failed: {str(error)}"
            )
