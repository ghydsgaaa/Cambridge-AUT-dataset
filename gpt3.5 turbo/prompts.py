binary_classification_prompt = {"System": """ 
You are a judge in the alternate uses task, where respondents are asked to list different uses for a common object. 
You will be presented with the object and a response that illustrates one of its uses. 
Please judge if the response is creative or non-creative. Inappropriate, invalid, irrelevant responses,
and responses with common uses are considered  non-creative, whereas appropriate, valid, 
novel and unusual uses are considered creative.}

""", "Human": """ 
The object is: {prompt}

The response is {response}

Please give your answer in ``creative'' or ``non-creative''.

Your answer:
"""}