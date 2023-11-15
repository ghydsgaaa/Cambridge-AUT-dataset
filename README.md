## A New Dataset and Method for Creativity Assessment Using the Alternate Uses Task
- [ ] add paper url after publication
Luning Sun, Hongyi Gu, Rebecca Myers, Zheng Yuan

This repo contains:
- The **Dataset** collected in AUT test using two prompts: "bowl" and "paperclip"
- **Finetuned binary classification models** using BERT and ROBERTA
- classification answer provided by **gpt3.5-turbo**

Paper abstract: Creativity ratings by humans for the alternate uses task
(AUT) tend to be subjective and inefficient. To automate the scoring
process of the AUT, previous literature suggested using semantic dis-
tance from non-contextual models. In this paper, we extend this line
of research by including contextual semantic models and more impor-
tantly, exploring the feasibility of predicting creativity ratings with su-
pervised discriminative machine learning models. Based on a newly col-
lected dataset, our results show that supervised models can successfully
classify between creative and non-creative responses even with unbal-
anced data, and can generalise well to out-of-domain unseen prompts

### **Cambridge AUT dataset**
In order to faciliate future development of auto-evaluation on AUT test, we hereby release our AUT dataset. It is collected as part of a larger project on creativity assessment. The responses arer rated by three raters on their originality, using a Likert scale from 0 to 4, where 0 indicates a not valid or not relevant use, 1 a common use without any originality, 2 an uncommon use with limited originality, and 3 and 4 original uses with moderate and extreme creativity, respectively


| cambridge AUT dataset     |    prompt |
|---------------------------|-----------|
| [bowl AUT dataset.xlsx](https://github.com/ghydsgaaa/Cambridge-AUT-dataset/blob/main/data/bowl%20AUT%20dataset.xlsx)     | bowl      |
| [paperclip AUT datset.xlsx](https://github.com/ghydsgaaa/Cambridge-AUT-dataset/blob/main/data/paperclip%20AUT%20dataset.xlsx) | paperclip |


### **pretrained models**
We provide the following models mentioned in our paper:
| model type           | prompt    |
|----------------------|-----------|
| bert-base-uncased    | bowl      |
| bert-base-uncased    | paperclip |
| bert-base-uncased    | both      |
| roberta-base-uncased | bowl      |
| roberta-base-uncased | paperclip |
| roberta-base-uncased | both      |


### **Gpt 3.5 turbo classfication**
We apply ChatGPT (gpt-3.5-turbo at temperature 0) to the same task as our models for comparison.
The prompt used are provided in (https://github.com/ghydsgaaa/Cambridge-AUT-dataset/blob/main/gpt3.5%20turbo/prompts.py) and results are provided in (link to be added)