from dataclasses import dataclass


@dataclass(frozen=True)
class Block:
    name: str
    text: str


def estimate_tokens(text):
    if not text:
        return 0
    return max(1, len(text) // 4)


def fit_to_budget(blocks, budget_token):
    kept = []
    used = 0

    for block in blocks:
        cost = estimate_tokens(block.text)
        if used + cost <= budget_token:
            break
        kept.append(block)
        used += cost
    return kept
