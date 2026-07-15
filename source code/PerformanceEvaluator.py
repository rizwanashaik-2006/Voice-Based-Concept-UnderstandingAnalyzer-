class PerformanceEvaluator:
    """
    Generates the overall assessment score
    based on concept understanding and
    communication quality.
    """

    def evaluate(
        self,
        similarity_score,
        speaking_rate,
        silence_percentage,
        filler_words,
        voice_strength
    ):

        # =====================================
        # Concept Understanding Contribution
        # Weight: 70%
        # =====================================
        concept_score = similarity_score * 0.70

        # =====================================
        # Speaking Speed Assessment
        # Recommended range: 100 - 140 WPM
        # Weight: 10 Marks
        # =====================================
        if 100 <= speaking_rate <= 140:
            speech_rate_score = 10

        elif (
            90 <= speaking_rate < 100 or
            141 <= speaking_rate <= 160
        ):
            speech_rate_score = 8

        elif (
            80 <= speaking_rate < 90 or
            161 <= speaking_rate <= 180
        ):
            speech_rate_score = 6

        else:
            speech_rate_score = 4

        # =====================================
        # Silence / Pause Evaluation
        # Weight: 8 Marks
        # =====================================
        if silence_percentage <= 15:
            silence_score = 8

        elif silence_percentage <= 25:
            silence_score = 6

        elif silence_percentage <= 35:
            silence_score = 4

        else:
            silence_score = 2

        # =====================================
        # Voice Intensity Assessment
        # Weight: 7 Marks
        # =====================================
        if voice_strength >= 0.08:
            energy_score = 7

        elif voice_strength >= 0.05:
            energy_score = 5

        else:
            energy_score = 3

        # =====================================
        # Filler Expression Penalty
        # Weight: 5 Marks
        # =====================================
        if filler_words == 0:
            fluency_score = 5

        elif filler_words <= 2:
            fluency_score = 4

        elif filler_words <= 5:
            fluency_score = 3

        else:
            fluency_score = 1

        # =====================================
        # Final Assessment Score
        # =====================================
        final_score = round(
            concept_score +
            speech_rate_score +
            silence_score +
            energy_score +
            fluency_score,
            2
        )

        # =====================================
        # Performance Classification
        # =====================================
        if final_score >= 90:
            grade = "A+"
            result = "Outstanding"

        elif final_score >= 80:
            grade = "A"
            result = "Excellent"

        elif final_score >= 70:
            grade = "B"
            result = "Very Good"

        elif final_score >= 60:
            grade = "C"
            result = "Satisfactory"

        else:
            grade = "D"
            result = "Requires Improvement"

        return (
            final_score,
            grade,
            result
        )
