import os
import sys

import antlr4

from gen.mingyu_grammarLexer import mingyu_grammarLexer
from gen.mingyu_grammarParser import mingyu_grammarParser
from gen.mingyu_grammarVisitor import mingyu_grammarVisitor


def main():
    if len(sys.argv) != 2 or not (input_file_name := sys.argv[1]):
        print("Incorrect arguments")
        return

    with open(input_file_name, 'r') as file:
        data = antlr4.InputStream(file.read())

    lexer = mingyu_grammarLexer(data)
    stream = antlr4.CommonTokenStream(lexer)
    parser = mingyu_grammarParser(stream)
    tree = parser.piece()
    visitor = mingyu_grammarVisitor()
    visitor.visit(tree)
    os.remove("output.ly")

if __name__ == '__main__':
    main()
