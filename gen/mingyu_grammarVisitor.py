from antlr4 import *

from mingyu_printer import mingyuPrinter

if __name__ is not None and "." in __name__:
    from gen.mingyu_grammarParser import mingyu_grammarParser
else:
    from mingyu_grammarParser import mingyu_grammarParser


# This class defines a complete generic visitor for a parse tree produced by mingyu_grammarParser.
class mingyu_grammarVisitor(ParseTreeVisitor):
    printer = mingyuPrinter()
    melody_index = 0

    # Visit a parse tree produced by mingyu_grammarParser#piece.
    def visitPiece(self, ctx: mingyu_grammarParser.PieceContext):
        self.printer.meter = str(ctx.getToken(mingyu_grammarParser.METER, 0))
        result = self.visitChildren(ctx)
        self.printer.generate_piece()
        return result

    # Visit a parse tree produced by mingyu_grammarParser#melody_lines.
    def visitMelody_lines(self, ctx: mingyu_grammarParser.Melody_linesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by mingyu_grammarParser#melody_line.
    def visitMelody_line(self, ctx: mingyu_grammarParser.Melody_lineContext):
        self.printer.voice_strings.append("")
        self.printer.keys.append("n")
        self.printer.key_signs.append(0)
        self.printer.number_of_notes_per_voice.append(0)
        self.printer.repetitions.append([])
        result = self.visitChildren(ctx)
        self.melody_index += 1
        return result

    # Visit a parse tree produced by mingyu_grammarParser#melody_content.
    def visitMelody_content(self, ctx: mingyu_grammarParser.Melody_contentContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by mingyu_grammarParser#clef_preamble.
    def visitClef_preamble(self, ctx: mingyu_grammarParser.Clef_preambleContext):
        self.printer.clefs.append(str(ctx.getToken(mingyu_grammarParser.CLEF, 0)))
        result = self.visitChildren(ctx)
        return result

    # Visit a parse tree produced by mingyu_grammarParser#modifier_with_note.
    def visitModifier_with_note(self, ctx: mingyu_grammarParser.Modifier_with_noteContext):
        self.printer.key_signs[self.melody_index] += 1
        self.printer.keys[self.melody_index] = str(ctx.getToken(mingyu_grammarParser.MODIFIER, 0))
        result = self.visitChildren(ctx)
        return result

    # Visit a parse tree produced by mingyu_grammarParser#tacts.
    def visitTacts(self, ctx: mingyu_grammarParser.TactsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by mingyu_grammarParser#tacts_with_repetition.
    def visitTacts_with_repetition(self, ctx: mingyu_grammarParser.Tacts_with_repetitionContext):
        self.printer.start_repetition(self.melody_index)
        result = self.visitChildren(ctx)
        self.printer.end_repetition(self.melody_index)
        return result

    # Visit a parse tree produced by mingyu_grammarParser#tact.
    def visitTact(self, ctx: mingyu_grammarParser.TactContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by mingyu_grammarParser#notes.
    def visitNotes(self, ctx: mingyu_grammarParser.NotesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by mingyu_grammarParser#note.
    def visitNote(self, ctx: mingyu_grammarParser.NoteContext):
        self.printer.add_note(self.melody_index, str(ctx.getToken(mingyu_grammarParser.SOUND_LENGTH, 0)),
                              str(ctx.getToken(mingyu_grammarParser.SOUND_HEIGHT, 0)),
                              str(ctx.getToken(mingyu_grammarParser.MODIFIER, 0)))
        result = self.visitChildren(ctx)
        return result

# del mingyu_grammarParser
