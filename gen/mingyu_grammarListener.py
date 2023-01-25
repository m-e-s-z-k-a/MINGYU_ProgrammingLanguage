from antlr4 import *

if __name__ is not None and "." in __name__:
    from .mingyu_grammarParser import mingyu_grammarParser
else:
    from mingyu_grammarParser import mingyu_grammarParser


# This class defines a complete listener for a parse tree produced by mingyu_grammarParser.
class mingyu_grammarListener(ParseTreeListener):

    # Enter a parse tree produced by mingyu_grammarParser#piece.
    def enterPiece(self, ctx: mingyu_grammarParser.PieceContext):
        pass

    # Exit a parse tree produced by mingyu_grammarParser#piece.
    def exitPiece(self, ctx: mingyu_grammarParser.PieceContext):
        pass

    # Enter a parse tree produced by mingyu_grammarParser#melody_lines.
    def enterMelody_lines(self, ctx: mingyu_grammarParser.Melody_linesContext):
        pass

    # Exit a parse tree produced by mingyu_grammarParser#melody_lines.
    def exitMelody_lines(self, ctx: mingyu_grammarParser.Melody_linesContext):
        pass

    # Enter a parse tree produced by mingyu_grammarParser#melody_line.
    def enterMelody_line(self, ctx: mingyu_grammarParser.Melody_lineContext):
        pass

    # Exit a parse tree produced by mingyu_grammarParser#melody_line.
    def exitMelody_line(self, ctx: mingyu_grammarParser.Melody_lineContext):
        pass

    # Enter a parse tree produced by mingyu_grammarParser#melody_content.
    def enterMelody_content(self, ctx: mingyu_grammarParser.Melody_contentContext):
        pass

    # Exit a parse tree produced by mingyu_grammarParser#melody_content.
    def exitMelody_content(self, ctx: mingyu_grammarParser.Melody_contentContext):
        pass

    # Enter a parse tree produced by mingyu_grammarParser#clef_preamble.
    def enterClef_preamble(self, ctx: mingyu_grammarParser.Clef_preambleContext):
        pass

    # Exit a parse tree produced by mingyu_grammarParser#clef_preamble.
    def exitClef_preamble(self, ctx: mingyu_grammarParser.Clef_preambleContext):
        pass

    # Enter a parse tree produced by mingyu_grammarParser#modifier_with_note.
    def enterModifier_with_note(self, ctx: mingyu_grammarParser.Modifier_with_noteContext):
        pass

    # Exit a parse tree produced by mingyu_grammarParser#modifier_with_note.
    def exitModifier_with_note(self, ctx: mingyu_grammarParser.Modifier_with_noteContext):
        pass

    # Enter a parse tree produced by mingyu_grammarParser#tacts.
    def enterTacts(self, ctx: mingyu_grammarParser.TactsContext):
        pass

    # Exit a parse tree produced by mingyu_grammarParser#tacts.
    def exitTacts(self, ctx: mingyu_grammarParser.TactsContext):
        pass

    # Enter a parse tree produced by mingyu_grammarParser#tacts_with_repetition.
    def enterTacts_with_repetition(self, ctx: mingyu_grammarParser.Tacts_with_repetitionContext):
        pass

    # Exit a parse tree produced by mingyu_grammarParser#tacts_with_repetition.
    def exitTacts_with_repetition(self, ctx: mingyu_grammarParser.Tacts_with_repetitionContext):
        pass

    # Enter a parse tree produced by mingyu_grammarParser#tact.
    def enterTact(self, ctx: mingyu_grammarParser.TactContext):
        pass

    # Exit a parse tree produced by mingyu_grammarParser#tact.
    def exitTact(self, ctx: mingyu_grammarParser.TactContext):
        pass

    # Enter a parse tree produced by mingyu_grammarParser#notes.
    def enterNotes(self, ctx: mingyu_grammarParser.NotesContext):
        pass

    # Exit a parse tree produced by mingyu_grammarParser#notes.
    def exitNotes(self, ctx: mingyu_grammarParser.NotesContext):
        pass

    # Enter a parse tree produced by mingyu_grammarParser#note.
    def enterNote(self, ctx: mingyu_grammarParser.NoteContext):
        pass

    # Exit a parse tree produced by mingyu_grammarParser#note.
    def exitNote(self, ctx: mingyu_grammarParser.NoteContext):
        pass


del mingyu_grammarParser
