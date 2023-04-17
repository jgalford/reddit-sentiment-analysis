import torch
from datasets import Dataset, DatasetDict
import pandas as pd
from transformers import DataCollatorWithPadding, AutoTokenizer, AutoModelForSequenceClassification


df = pd.read_csv("Reddit_Data.csv")
print(df.head())


#tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

