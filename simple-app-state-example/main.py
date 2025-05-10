import writer as wf

initial_state = wf.init_state(
    {
        "selectable_values": {
            "joe_is_great": "Joe is Great",
            "joe_is_bad": "Joe is Bad",
        },
        "value_currently_selected": "<nothing selected>",
        "auto_key_currently_selected": "<nothing selected>",
    },
)


def update_value_currently_selected(state, payload):
    state["value_currently_selected"] = state["selectable_values"][payload]
