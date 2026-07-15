import re
import librosa
import numpy as np


class SpeechAnalyzer:

    """
    Analyze speech recordings and extract
    useful communication metrics.
    """

    def analyze_audio(self, audio_file, transcript_text):

        try:

            # Load audio recording
            signal_data, sampling_rate = librosa.load(
                audio_file,
                sr=None
            )

            # Measure total recording length
            recording_duration = librosa.get_duration(
                y=signal_data,
                sr=sampling_rate
            )

            # Calculate average signal intensity
            rms_values = librosa.feature.rms(
                y=signal_data
            )[0]

            voice_energy = float(
                np.mean(rms_values)
            )

            # Count words from transcript
            transcript_words = transcript_text.split()

            word_count = len(
                transcript_words
            )

            # Calculate speaking speed
            speaking_speed = 0

            if recording_duration > 0:

                speaking_speed = round(
                    (word_count * 60) /
                    recording_duration
                )

            # Common filler expressions
            filler_words = [
                "um",
                "uh",
                "like",
                "actually",
                "basically",
                "you know",
                "so"
            ]

            transcript_lowercase = (
                transcript_text.lower()
            )

            filler_occurrences = 0

            for expression in filler_words:

                pattern = (
                    r"\b" +
                    re.escape(expression) +
                    r"\b"
                )

                filler_occurrences += len(
                    re.findall(
                        pattern,
                        transcript_lowercase
                    )
                )

            # Estimate silent intervals
            average_word_duration = 0.45

            active_speech_time = (
                word_count *
                average_word_duration
            )

            if recording_duration > 0:

                silence_percentage = max(
                    0,
                    (
                        recording_duration -
                        active_speech_time
                    ) / recording_duration
                )

            else:

                silence_percentage = 0

            silence_percentage = round(
                silence_percentage * 100,
                2
            )

            # Prepare results
            analysis_results = {

                "duration_seconds": round(
                    recording_duration,
                    2
                ),

                "total_words": word_count,

                "words_per_minute": speaking_speed,

                "average_energy": round(
                    voice_energy,
                    4
                ),

                "silence_ratio": silence_percentage,

                "filler_word_count": filler_occurrences
            }

            return analysis_results

        except Exception as error:

            raise Exception(
                f"Speech analysis failed: {str(error)}"
            )
