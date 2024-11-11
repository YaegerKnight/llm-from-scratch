import re

with open('the-verdict.txt', encoding='utf-8') as f: sample_text = f.read()
tokens = re.split(r'([,.?!_():;"\']|--|\s)', sample_text)
tokens = [items.strip() for items in tokens if items.strip()]
tokens.extend(["<|endoftext|>", "<|unk|>"])
tokens = set(tokens)
token_map = dict()
for id,token in enumerate(tokens):
    if token not in token_map.keys():
        token_map[token] = id


class TestTokenizer:

    def __init__(self, token_map):
        self.str_to_int = token_map
        self.int_to_str = {i:s for s,i in token_map.items()}
    
    def encode(self, text):
        tokens = re.split(r'([,.?!_():;"\']|--|\s)', text)
        tokens = [items.strip() for items in tokens if items.strip()]
        
        tokens = [item if item in self.str_to_int else "<|unk|>" for item in tokens]
        ids = [self.str_to_int[i] for i in tokens]
        return ids
    
    def decode(self, ids):
        ids = [item if item in self.int_to_str else self.str_to_int["<|unk|>"] for item in ids]
        text = " ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r'\s+([,.?!"() \'])', r'\1', text)

        return text


tokenizer = TestTokenizer(token_map)
text1 = "Hello, do you like tea?"
text2 = "In the sunlit terraces of the palace."
text = " <|endoftext|> ".join((text1, text2))
print(text)
print(tokenizer.decode(tokenizer.encode(text)))
