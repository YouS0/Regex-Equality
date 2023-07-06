# Regex-Equality
Theory of automata and formal languages Project
This small project gets two Regular expressions and check if they are accepting a same language or not.
This process works with several steps included:  
**1-** Parse the Regex and Create a AST-Tree based on the input Regex.  
**2-** Create an NFA base on the AST-Tree based on Thompson's Algorithm.  
**3-** Create a DFA based on the NFA.  
**4-** Minimize the DFA and check.  
**5-** Check equality of MDFAs for both REs.  
