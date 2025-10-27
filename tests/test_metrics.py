from optimizer.metrics import semantic_similarity, combined_score

def test_semantic_similarity_close():
    ref = "Paris"
    cand = "Paris is the capital of France."
    s = semantic_similarity(ref, cand)
    assert s > 0.5, f"expected similarity > 0.5, got {s}"

def test_combined_score_basic():
    ref = "42"
    cand = "42"
    score = combined_score(ref, cand, token_cost=10)
    assert score > 0.7, f"expected score > 0.7, got {score}"

if __name__ == '__main__':
    test_semantic_similarity_close()
    test_combined_score_basic()
    print('Metrics tests passed')
