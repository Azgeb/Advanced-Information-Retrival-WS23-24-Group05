import pandas as pd

'''
Whats going on here:

The data is first cleaned to get rid of question/answer format turning this
from a classification set to a generative set. 

Second, the input section is changed from being the whole input to two secitons: input (context basically) and question.
This can be removed if not necessary.

Finally, its moved to a csv file with format:
[,instruction,input,output,question]

There are a few spots where the question and context did not get split correctly, but the overwhelming
majority of it is correctly separated. Could be good to have some random poorly formatted questions for
robustness.
'''

df = pd.read_json('data.json')

df['question'] = str

for index, row in df.iterrows():
    
    text = row['input']

    # Remove choices from question
    split_loc = text.rfind('?')
    text = text[2:split_loc]

    text = text.replace('\n', ' | ')
    text = text.lower()
    text = text.replace('which of the following', 'what')

    # Split context from questions
    split_text = text.split('.')
    question = split_text[-1]
    if len(split_text) > 2:
        # Remove 'Q:' and the answers from input
        input = ' '.join(split_text[:-2])
    elif len(split_text) == 2:
        input = split_text[0]
    else:
        input = question  # Imperfect fix, the whole line is one sentence with no context.

    df.at[index, 'input'] = input
    df.at[index, 'question'] = question

    # Remove '[a,b,c,d,e]:' from correct output
    text = row['output']
    df.at[index, 'output'] = text[3:].lower()

    # Change instruction
    df.at[index, 'instruction'] = 'please answer the question based on the given information'

df.to_csv('processed_data.csv')