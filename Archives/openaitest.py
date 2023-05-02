import os
import openai



def GPT3_syns(key_word, context):

    openai.api_key = "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"
    prompt = "return a python list of synonyms and related words of" + key_word + "in the context of" + context

    response = openai.Completion.create(
        engine = "text-davinci-002",
        prompt = prompt,
    )
   
    generated_text = response.choices[0].text

    print(generated_text)


GPT3_syns("retail", "supply chain management")
