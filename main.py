import time
from lexer import Lexer
from parserr import Parser
from nfa import ast_to_nfa, get_transition_table, get_starting_state, get_accepting_state
from dfa import build_powerset, clean_dfa
from mdfa import minimize_dfa
from logger import log_mdfa
from graph import visualize_mdfa


def run(input_regex: str, verbose: bool, __mdfa_filename , graphname):
    lexer = Lexer(input_regex)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    ast = parser.parse()
    #print(tokens)
    #print(ast)

    ast_to_nfa(ast, verbose=verbose)
    nfa = get_transition_table()

    starting_state = get_starting_state()
    accepting_state = get_accepting_state()
    dfa = build_powerset(starting_state, accepting_state, nfa)

    cdfa = clean_dfa(dfa)

    mdfa = minimize_dfa(cdfa)
    log_mdfa(mdfa,__mdfa_filename)
    visualize_mdfa(mdfa, graphname)


def main(regex ,__mdfa_filename , graphname):

    run(regex,True,__mdfa_filename , graphname)

    return True

regex1 = "(a|b)"
regex2 = "aaabb"
#main(regex1 , "First.json" , "FirstGraph")
main(regex2 , "Second.json" , "SecondGraph")

