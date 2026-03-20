def is_similar(text1, text2):
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())

    common = words1.intersection(words2)

    return len(common) / max(len(words1), len(words2)) > 0.3