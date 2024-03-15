import pandas as pd
import torch
# import pytorch
def tapaxmodel(question_list):
    df = pd.read_excel('company21with date.xlsx')
    df.rename(columns={"index": "Quarter"}, inplace=True)



    from transformers import TapexTokenizer, BartForConditionalGeneration, pipeline
    tokenizer = TapexTokenizer.from_pretrained("microsoft/tapex-large-finetuned-wtq")
    model = BartForConditionalGeneration.from_pretrained("microsoft/tapex-large-finetuned-wtq")
    df = df.sample(frac=1).reset_index(drop=True)
    # df = df.sort_values(by='Quarter', ascending=True)

    df = df.astype(str)
    # Adjust the maximum sequence length
    max_length = 1023  # Adjust as needed

    # Process data in chunks to avoid memory errors
    chunk_size = 100  # Adjust as needed
    chunks = [df[i:i+chunk_size] for i in range(0, len(df), chunk_size)]

    # question_list = [
    #     "which company has better solvency ratio?",
    #     "which is best private company among all companies?",
    #     "Highest premium earned by which company ?",
    #     "Which Quarter has the Highest Premium Earned?",
    #     "Total premium earned by LIC?",
    #     "best company in year 2020?"
    #                 ]


    results=[]
    for chunk in chunks:
        encoding = tokenizer(table=chunk, query=question_list, return_tensors="pt", padding=True, truncation=True, max_length=max_length)
        outputs = model.generate(**encoding)
        result = tokenizer.batch_decode(outputs, skip_special_tokens=True)
        results.append(result[0])
            
        print('For the question :')
        for result in results:
            print(result)
        print('sending the',results)
    return(results)
