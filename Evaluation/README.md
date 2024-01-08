
# Evaluation
In order to evaluate the improvement of our Model, we choose to use another subset of the [medalpaca/medical_meadow_medqa](https://huggingface.co/datasets/medalpaca/medical_meadow_medqa) dataset (other than the 3000 rows used to fine-tune the Model) in order to generate the responses from the LLM Models (fine-tuned and original)

## responses_original.csv
The results of the generation of responses based on the Question within the dataset rows of the **original** Model.

## responses_tuned.csv
The results of the generation of responses based on the Question within the dataset rows of the **fine-tuned** Model.

# Results
## F1 Score and Sentence similarity
![](https://github.com/Azgeb/Advanced-Information-Retrival-WS23-24-Group05/blob/main/Evaluation/F1_and_Sentence_Sim.png)
## ROUGE Unigram and ROUGE Bigram 
![](https://github.com/Azgeb/Advanced-Information-Retrival-WS23-24-Group05/blob/main/Evaluation/ROUGE_Unigram_Bigram.png)
