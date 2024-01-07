# Dataset Preparation

## Original Dataset

For the dataset in our fine-tuning pipeline, we use the [medalpaca/medical_meadow_medqa](https://huggingface.co/datasets/medalpaca/medical_meadow_medqa) dataset as the base since it already contains answers to given medical questions.

## Dataset Transformation

The dataset undergoes transformation to remove possible answers, leaving only the correct answers to each question, which are then written into a separate column. Columns for the question and the answer are also included.

## Usage of preparation.py

To utilize the provided Python script, place the original dataset in the same directory as the script itself. The original dataset should be named "data.json"; otherwise, the Python script will need modification.
