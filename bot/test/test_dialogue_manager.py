import pytest
import bot.src.dialogue_manager as dialogue_manager
from bot.src.context import Context

@pytest.mark.skip(reason="no correct testing this")
def test_next_action_start():
    intent = [None]
    entities = []
    context = Context()

    action, context = dialogue_manager.next_action(intent, entities, context)

    assert action == "ask_start"
    assert context.status == "start"


def test_next_action_ask_degree():
    intent = ['info']
    entities = []
    context = Context()

    action, context = dialogue_manager.next_action(intent, entities, context)

    assert action == "ask_start"
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


def test_get_entity_name():
    entity_list = [['exams', True], ['teaching_guide', True], ['tfg', True]]
    expect_names = ['exams', 'teaching_guide', 'tfg']

    result_names = dialogue_manager.get_entity_name(entity_list)

    assert result_names == expect_names

def test_get_status_subentity():
    
    subentity_list = [
            ['tfg_duration', True],
            ['internship_description', True],
            ['registration_link', True],
            ['registration_documentation', True],
            ['tfg_deadline', True],
        ]
    
    name = 'tfg'
    expected_name = [['tfg_duration', True], ['tfg_deadline', True]]
    subentity_name = dialogue_manager.get_status_subentity(subentity_list, name)

    assert subentity_name == expected_name
