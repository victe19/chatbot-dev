import src.dialogue_manager as dialogue_manager
from src.context import Context

def test_next_action_start():
    intent = [None]
    entities = []
    context = Context()

    action, context = dialogue_manager.next_action(intent, entities, context)

    assert action == "ask_degree"
    assert context.status == "start"


def test_next_action_ask_degree():
    intent = ['info']
    entities = []
    context = Context()

    action, context = dialogue_manager.next_action(intent, entities, context)

    assert action == "ask_degree"
    assert context.status == "info_more"


def test_next_action_ask_course():
    intent = [None]
    entities = [
        [["degree", "química"]],
        [["degree", "informàtica"]],
        [["degree", "dades"]],
    ]
    context = Context()

    for entity in entities:
        action, context = dialogue_manager.next_action(intent, entity, context)

    assert action == "ask_course"
    assert context.status == "info_more_degree"
    
    # teardown
    action = ""
    context.status = ""


def test_next_action_ask_degree_without_intent():
    intent = [None]
    entities = [
        [["course", "1"]],
        [["course", "2"]],
        [["course", "3"]],
    ]
    context = Context()

    for entity in entities:
        action, context = dialogue_manager.next_action(intent, entity, context)

    assert action == "ask_degree"
    assert context.status == "info_more_degree"
    
    # teardown
    action = ""
    context.status = ""

