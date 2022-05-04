from src.context import Context

def test_setup_context():
    entity_list = [["course", "1"]]
    context = Context()

    Context.setup_context(context, entity_list)

    assert  context.course == "1"


def test_setup_context():
    entity_list = [["schedule", True], ["course", "1"], ["degree", "informàtica"]]
    context = Context()

    Context.setup_context(context, entity_list)

    assert  context.schedule == True
    assert  context.course == "1"
    assert  context.degree == "informàtica"
