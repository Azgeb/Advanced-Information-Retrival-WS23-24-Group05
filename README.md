
# Out-of-the-box performance  Compare a pretrained DPR model vs. fine-tuning a model  (Group 5)  
- Luke Leimbach (Role: Dataset Selection / Preparation)  
- Raphael Kandler (Role: Response Analysis )  
- Joseph Juri (Role: Fine-tuning)

## Abstract
To leverage pre-trained models with solid 'world knowledge,' we decided to compare the performance of a pre-trained DPR model against a fine-tuned variant. 
We opted to specify our fine-tuned model within the medical question and answer domain, enabling users of either model to inquire about a diagnosis based on their described symptoms.
For our base model, we chose the [facebook/dpr-ctx\_encoder-single-nq-base](https://huggingface.co/facebook/dpr-ctx_encoder-single-nq-base) model, and we plan to fine-tune it using the [medalpaca/medical\_meadow\_medqa](https://huggingface.co/datasets/medalpaca/medical_meadow_medqa)  dataset.

The base model was trained on approximately 80 thousand rows of data, and we will be fine-tuning this model with around 10 thousand rows of Medical QA data. Due to the substantial contribution of new training data to be base model, we expect a significant increase in accuracy in the fine-tuned model.

In order to thoughtfully verify the accuracy of the models' responses, we will decide on a final method of analysis after completing the fine-tuning step. One preliminary metric we are investigating is the use of a training dataset in the format of 'description of symptom - correct diagnosis' to ascertain the validity of the responses.
### Schematic
![](https://github.com/Azgeb/Advanced-Information-Retrival-WS23-24-Group05/blob/main/design_doc_diagram.png)

## Correction - Change of Base Model and Architecture
After facing several difficulties with the initial proposed DPL model and Dataset preparation/ availability, we decided to do a comparison of a LLM model with focus on question answering, namely the [vilsonrodrigues/falcon-7b-instruct-sharded](https://huggingface.co/vilsonrodrigues/falcon-7b-instruct-sharded) Model and compare the results on the base model against the fine-tuned model trained on the initially planned dataset. 
### Schematic - Corrected
![](https://github.com/Azgeb/Advanced-Information-Retrival-WS23-24-Group05/blob/main/design_doc_diagram_correction.png)
