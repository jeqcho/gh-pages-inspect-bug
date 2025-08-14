from inspect_ai import Task, task
from inspect_ai.dataset import example_dataset
from inspect_ai.scorer import match
from inspect_ai.solver import generate
from inspect_ai import eval


@task
def theory_of_mind():
    return Task(
        dataset=example_dataset("theory_of_mind"),
        solver=[generate()],
        scorer=match(),
    )


eval(
    tasks=[theory_of_mind()],
    model="mockllm/model",
    limit=1,
)
