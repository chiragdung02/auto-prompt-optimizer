from sentence_transformers import SentenceTransformer, util

EMB_MODEL = SentenceTransformer('all-MiniLM-L6-v2')

def semantic_similarity(reference: str, candidate: str) -> float:
    if reference is None or candidate is None:
        return 0.0
    try:
        emb_ref = EMB_MODEL.encode(reference, convert_to_tensor=True)
        emb_cand = EMB_MODEL.encode(candidate, convert_to_tensor=True)
        score = util.pytorch_cos_sim(emb_ref, emb_cand).item()
        if score < 0:
            score = 0.0
        return float(score)
    except Exception:
        return 0.0

def length_penalty(candidate: str) -> float:
    if not candidate:
        return 0.0
    length = len(candidate.split())
    if length <= 50:
        return 1.0
    penalty = max(0.2, 1.0 - ((length - 50) / 500))
    return penalty

def combined_score(reference: str, candidate: str, token_cost: int, alpha: float = 0.7) -> float:
    sim = semantic_similarity(reference, candidate)
    brev = length_penalty(candidate)
    token_factor = max(0.0, 1.0 - (token_cost / 2000))
    score = alpha * sim + (1 - alpha) * (0.5 * brev + 0.5 * token_factor)
    return float(score)
