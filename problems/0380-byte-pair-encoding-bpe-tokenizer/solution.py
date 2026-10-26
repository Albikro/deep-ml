def byte_pair_encoding(corpus: dict, num_merges: int) -> list:
    """
    Train a BPE tokenizer on the given corpus.
    
    Args:
        corpus: Dictionary mapping space-separated token sequences to their frequencies.
                Example: {"l o w </w>": 5, "n e w </w>": 6}
        num_merges: Number of merge operations to perform.
    
    Returns:
        List of tuples, where each tuple contains the two tokens that were merged.
        Example: [('l', 'o'), ('lo', 'w')]
    """
    vocab = {}
    for key,value in corpus.items():
        vocab[tuple(key.split())] = value
    
    merges = []
    for merge in range(num_merges):
        pairs = {}
        for key,value in vocab.items():
            for i in range(len(key) - 1):
                pair = (key[i], key [i + 1])
                if pair in pairs:
                    pairs[pair] += value
                else:
                    pairs[pair] = value
        if len(pairs) == 0:
            break
        else: 
            best_pair = max(pairs, key = pairs.get)
            merges.append(best_pair)
        
        new_vocab = {}
        for key,value in vocab.items():
            i = 0
            new_key = []
            while i < len(key):
                if i != len(key) -1 and(key[i],key[i + 1]) == best_pair:
                    new_key.append(key[i] + key[i + 1])
                    i += 2
                else:
                    new_key.append(key[i])
                    i += 1
            new_vocab[tuple(new_key)] = value
        vocab = new_vocab

    return merges
        

