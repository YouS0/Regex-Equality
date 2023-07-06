
import json
from typing import Dict
from dfa import DFAClean

#__mdfa_filename = "MDFA.json"
__mdfa_result: Dict[str, str | Dict[str, str | bool]] = {}


def __build_mdfa_result(mdfa: DFAClean):
    for state, transitions in mdfa.transitions.items():
        __mdfa_result[state.label] = {}
        for next_state, char in transitions:
            __mdfa_result[state.label][char] = next_state.label
        __mdfa_result[state.label]["isTerminatingState"] = state in mdfa.accepting_states


def log_mdfa(mdfa: DFAClean , __mdfa_filename):
    __mdfa_result.update({"startingState": mdfa.starting_state.label})
    __build_mdfa_result(mdfa)
    with open(__mdfa_filename, "w") as f:
        json.dump(__mdfa_result, f, ensure_ascii=False, indent=2)
