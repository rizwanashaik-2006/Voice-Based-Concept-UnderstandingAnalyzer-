# Data Flow Diagram

## Introduction

The Data Flow Diagram (DFD) demonstrates how information travels through the Voice-Based Concept Understanding Analyser system. It illustrates the interaction between users, AI processing modules, storage components, and report generation services from voice submission to final evaluation.

The diagram provides a clear representation of how spoken explanations are transformed into meaningful insights, analyzed using AI techniques, and presented as performance reports to users.

---

# DFD Symbol Legend

| Symbol               | Name             | Description                                                                                                     |
| -------------------- | ---------------- | --------------------------------------------------------------------------------------------------------------- |
| Oval / Rounded Shape | External Actor   | Represents users or external systems that interact with the application by providing input or receiving output. |
| Numbered Rectangle   | Processing Unit  | Represents operations such as speech recognition, semantic evaluation, fluency analysis, and report creation.   |
| Open Rectangle       | Data Repository  | Stores uploaded audio recordings, transcripts, and generated evaluation reports.                                |
| Directed Arrow       | Information Flow | Indicates the movement of information between modules, users, and storage units.                                |

---

# DFD Description

The process begins when a learner records or uploads an explanation through the application interface. The Speech Recognition Module transforms the audio into textual content for further processing.

The generated transcript is forwarded to the Concept Evaluation Module, where it is compared against reference concepts to determine semantic similarity and conceptual accuracy.

At the same time, the Audio Processing Engine extracts speech-related characteristics such as speaking rate, pauses, filler words, and energy levels to evaluate communication quality and fluency.

The Assessment Engine combines conceptual understanding metrics and speech quality measurements to compute an overall performance score and classify the learner's understanding level.

Finally, the Reporting Module creates a detailed feedback report containing transcripts, scores, recommendations, and improvement suggestions, which is then delivered to the learner and optionally stored for future review.

---

# Suggested DFD Components

### External Entities

* Student / Learner
* AI Evaluation Service

### Processes

1. Voice Input Processing
2. Transcript Generation
3. Concept Similarity Analysis
4. Speech Feature Analysis
5. Performance Evaluation
6. Feedback Report Generation

### Data Stores

* D1: Audio Repository
* D2: Transcript Storage
* D3: Evaluation Records
* D4: Generated Reports
