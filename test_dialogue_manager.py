import dialogue_manager
from context import Context

def test_next_action_start():
    intent = None
    entities = []
    context = Context()

    action, context = dialogue_manager.next_action(intent, entities, context)

    assert action == "ask_degree"
    assert context.status == "start"


def test_next_action_ask_degree():
    intent = 'info'
    entities = []
    context = Context()

    action, context = dialogue_manager.next_action(intent, entities, context)

    assert action == "ask_degree"
    assert context.status == "info_more"


def test_next_action_ask_course():
    intent = None
    entities = [("degree", "química")]
    context = Context()


    action, context = dialogue_manager.next_action(intent, entities, context)

    assert action == "ask_course"
    assert context.status == "info_more_degree"
    
