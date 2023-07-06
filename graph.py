# this file should be used to visualize the nfa, dfa and mdfa

import graphviz
from dfa import DFAClean


def visualize_mdfa(mdfa: DFAClean, filename: str):
    g = graphviz.Digraph("MDFA", filename=filename, format="png")
    g.attr(rankdir="LR")
    g.edge("", mdfa.starting_state.label)
    g.node("", shape="none")
    for state, transitions in mdfa.transitions.items():
        for next_state, char in transitions:
            g.edge(state.label, next_state.label, label=char)
    for accepting_state in mdfa.accepting_states:
        g.node(accepting_state.label, peripheries="2")
    g.attr(label=r"\n\nMinimized DFA", fontsize="20", labelloc="b")
    g.view()
