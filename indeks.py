def build_index(documents):
    index = {}
    for i, doc in enumerate(documents):
        words = [''.join(c for c in word if c.isalnum()).lower() for word in doc.split()]
        for word in words:
            if word not in index:
                index[word] = {}
            if i not in index[word]:
                index[word][i] = 0
            index[word][i] += 1
    return index

def process_queries(index, queries):
    results = []
    for query in queries:
        word = query.lower()
        if word in index:
            doc_freq = index[word]
            sorted_docs = sorted(doc_freq.items(), key=lambda x: -x[1])
            results.append([doc_id for doc_id, _ in sorted_docs])
        else:
            results.append([])
    return results

if __name__ == "__main__":
    documents = [
        "Your care set up, do not pluck my care down.",
        "My care is loss of care with old care done.",
        "Your care is gain of care when new care is won."
    ]
    queries = ["care", "is"]
    index = build_index(documents)
    results = process_queries(index, queries)
    for r in results:
        print(r)
