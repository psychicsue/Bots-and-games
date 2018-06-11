from nltk import word_tokenize, pos_tag, ne_chunk
from nltk import Tree

def get_chunks(text, label):
    text = text.title()
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    print(chunked)
    current_chunk = []

    for subtree in chunked:
        if type(subtree) == Tree and subtree.label() == label:
            current_chunk.append(
                " ".join([token for token, pos in subtree.leaves()]))

    return current_chunk
