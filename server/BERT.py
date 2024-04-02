import dataset as doc
import torch
from transformers import BertModel, BertTokenizer, AutoTokenizer
import numpy as np
from transformers import GPT2Tokenizer, GPT2LMHeadModel

import numpy as np
import torch
from sklearn.metrics.pairwise import cosine_similarity

from keybert import KeyBERT

import heapq


class Bert:
    def __init__(self) -> None:
        # Load the pre-trained BERT model and tokenizer
        self.model = BertModel.from_pretrained("bert-base-uncased")
        self.tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
        self.max_len = 512
        self.documents = doc.documents
        self.doc_to_vector()

    def tokenize_query(self, query):
        # Truncate the query to the maximum number of tokens
        truncated_query = query[: self.max_len - 2]
        # Encode the truncated query as a sequence of tokens
        input_ids = self.tokenizer.encode(truncated_query, add_special_tokens=True)
        # Pad the input sequence to the same length as the document vectors
        padded_input_ids = input_ids + [0] * (self.max_len - len(input_ids))
        # Convert the input sequence to a tensor
        input_tensor = torch.tensor(padded_input_ids).unsqueeze(0).long()
        return input_tensor

        # Define a function to truncate and tokenize a document

    def tokenize_document(self, doc, tokenizer, max_len):
        # Truncate the document to the maximum number of tokens
        truncated_doc = doc[: max_len - 2]
        # Encode the truncated document as a sequence of tokens
        input_ids = tokenizer.encode(truncated_doc, add_special_tokens=True)
        return input_ids

    # Define a function to convert a document to a BERT embedding vector
    def convert_to_vector(self, document, model, tokenizer, max_len):
        # Tokenize the document
        document = document[:512]
        tokens = self.tokenize_document(document, tokenizer, max_len)
        # Convert the tokens to their corresponding BERT embeddings
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        input_ids = torch.tensor([tokens]).to(device)
        # Use the BERT model to generate the embeddings
        with torch.no_grad():
            embeddings = model(input_ids)[0]
        # Take the average of the embeddings to get a single vector representation of the document
        vector = torch.mean(embeddings, dim=1)
        return vector.to("cpu")

    def doc_to_vector(self):
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = self.model.to(device)
        self.model = self.model.eval()

        self.vectors = []
        for i in range(len(self.documents)):
            vector = self.convert_to_vector(
                self.documents[i], self.model, self.tokenizer, self.max_len
            )
            self.vectors.append(vector)

    def process_query(self, query):
        self.query = query
        self.query_vector = self.convert_to_vector(
            self.query, self.model, self.tokenizer, self.max_len
        )
        self.cosaine_sim()

    def cosaine_sim(self):
        similarities = []
        top_similarities = []

        for idx, doc in enumerate(self.vectors):
            sim = cosine_similarity(self.query_vector, doc)
            similarities.append(sim)

            # Keep track of the top 5 highest similarities and their indices
            if len(top_similarities) < 5:
                heapq.heappush(top_similarities, (sim, idx))
            else:
                heapq.heappushpop(top_similarities, (sim, idx))

        # Extract the top 5 highest similarities and their indices
        top_similarities = sorted(top_similarities, reverse=True)
        self.top_5_similarities = [similarity[0] for similarity in top_similarities]
        self.top_5_indices = [similarity[1] for similarity in top_similarities]

    def keybert(self):
        kw_model = KeyBERT()
        keywords = []
        # Maximal Marginal Relevance
        for idx in self.top_5_indices:
            phrase = kw_model.extract_keywords(
                self.documents[idx],
                keyphrase_ngram_range=(1, 4),
                stop_words="english",
                use_mmr=True,
                diversity=0.2,
            )
            keywords.append(phrase)

        highest_keywords = []
        result = []
        if keywords:
            for phrase in keywords:
                if phrase:
                    highest_keyword = max(phrase, key=lambda x: x[1])
                    highest_keywords.append(highest_keyword)

                    result = [query[0] for query in highest_keywords]

                else:
                    # Handle case when no keywords are found
                    # You can choose to set some default value or perform any other desired action
                    result = ["I need more training to expand that!"]

            return result

    def get_query(self, query):
        self.process_query(query)
        # return result
        self.result = self.keybert()
        return self.result
        # print(self.top_5_indices)
        # print(self.top_5_similarities)
