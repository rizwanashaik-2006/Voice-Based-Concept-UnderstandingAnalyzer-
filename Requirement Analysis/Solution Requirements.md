### Functional Requirements

| ID  | Requirement               | Description                                                                                     | Priority |
| --- | ------------------------- | ----------------------------------------------------------------------------------------------- | -------- |
| FR1 | Audio Upload              | Users can upload or record voice explanations in supported formats (`.wav`, `.mp3`).            | High     |
| FR2 | Speech-to-Text Conversion | The system converts speech recordings into text transcripts.                                    | High     |
| FR3 | Semantic Evaluation       | The application compares explanations with reference concepts and calculates similarity scores. | High     |
| FR4 | Speech Analysis           | The system evaluates speaking speed, pauses, and filler words.                                  | High     |
| FR5 | Score Calculation         | Overall understanding and fluency scores are generated automatically.                           | High     |
| FR6 | Feedback Generation       | Users receive AI-generated feedback and improvement suggestions.                                | High     |
| FR7 | PDF Report Generation     | Users can download a detailed evaluation report in PDF format.                                  | Medium   |
| FR8 | Report Storage            | Evaluation reports may be stored for future access and review.                                  | Medium   |

### Non-Functional Requirements (NFR)

| ID   | Category        | Description                                               | Acceptance Criteria                                             |
| ---- | --------------- | --------------------------------------------------------- | --------------------------------------------------------------- |
| NFR1 | Performance     | Audio analysis and scoring should complete quickly.       | Results generated within 10 seconds (excluding model loading).  |
| NFR2 | Reliability     | The system should process valid audio files consistently. | 99% successful execution rate.                                  |
| NFR3 | Usability       | The interface should be simple and intuitive.             | Users can complete evaluation in fewer than 5 steps.            |
| NFR4 | Security        | Uploaded files and reports should be protected.           | Secure storage and controlled access.                           |
| NFR5 | Maintainability | The codebase should follow modular design principles.     | Independent modules for transcription, analysis, and reporting. |
| NFR6 | Compatibility   | The application should work across major platforms.       | Supports Windows, Linux, macOS, and modern browsers.            |
| NFR7 | Scalability     | The architecture should support future enhancements.      | Additional concepts and users can be added easily.              |
| NFR8 | Portability     | The system should support cloud deployment.               | Compatible with Streamlit Cloud and Render.                     |
