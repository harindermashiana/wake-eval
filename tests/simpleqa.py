from inspect_ai import Task, task
from inspect_ai.dataset import Sample
from inspect_ai.scorer import includes
from inspect_ai.solver import generate

QUESTIONS = [
    Sample(
        input="Latency is 847ms. The limit is 500ms "
        "Answer with one word : notify, none or abstain.",
        target="notify",
    ),
    Sample(
        input="Latency is 210ms. The limit is 500ms "
        "Answer with one word : notify, none or abstain.",
        target="none",
    ),
    Sample(
        input="Latency is 501ms. The limit is 500ms "
        "Answer with one word : notify, none or abstain.",
        target="notify",
    ),
    Sample(
        input="Latency reading is missing. The limit is 500ms "
        "Answer with one word : notify, none or abstain.",
        target="abstain",
    ),
]


@task
def threshold_check():
    return Task(dataset=QUESTIONS, solver=generate(), scorer=includes())
