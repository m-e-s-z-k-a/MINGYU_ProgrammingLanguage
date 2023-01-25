import sys

from antlr4 import *

if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4, 1, 14, 81, 2, 0, 7, 0, 2, 1, 7, 1, 2, 2, 7, 2, 2, 3, 7, 3, 2, 4, 7, 4, 2, 5, 7, 5, 2, 6, 7,
        6, 2, 7, 7, 7, 2, 8, 7, 8, 2, 9, 7, 9, 2, 10, 7, 10, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 4, 1,
        29, 8, 1, 11, 1, 12, 1, 30, 1, 2, 1, 2, 1, 2, 1, 2, 1, 3, 1, 3, 1, 3, 1, 4, 1, 4, 4, 4, 42, 8,
        4, 11, 4, 12, 4, 43, 1, 5, 1, 5, 1, 5, 1, 6, 1, 6, 1, 6, 4, 6, 52, 8, 6, 11, 6, 12, 6, 53, 1,
        7, 1, 7, 5, 7, 58, 8, 7, 10, 7, 12, 7, 61, 9, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 8, 1, 8, 1, 8, 1,
        9, 4, 9, 71, 8, 9, 11, 9, 12, 9, 72, 1, 10, 3, 10, 76, 8, 10, 1, 10, 1, 10, 1, 10, 1, 10,
        0, 0, 11, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 0, 0, 76, 0, 22, 1, 0, 0, 0, 2, 28, 1, 0,
        0, 0, 4, 32, 1, 0, 0, 0, 6, 36, 1, 0, 0, 0, 8, 39, 1, 0, 0, 0, 10, 45, 1, 0, 0, 0, 12, 48, 1,
        0, 0, 0, 14, 55, 1, 0, 0, 0, 16, 66, 1, 0, 0, 0, 18, 70, 1, 0, 0, 0, 20, 75, 1, 0, 0, 0, 22,
        23, 5, 9, 0, 0, 23, 24, 5, 6, 0, 0, 24, 25, 3, 2, 1, 0, 25, 26, 5, 13, 0, 0, 26, 1, 1, 0, 0,
        0, 27, 29, 3, 4, 2, 0, 28, 27, 1, 0, 0, 0, 29, 30, 1, 0, 0, 0, 30, 28, 1, 0, 0, 0, 30, 31,
        1, 0, 0, 0, 31, 3, 1, 0, 0, 0, 32, 33, 5, 10, 0, 0, 33, 34, 3, 6, 3, 0, 34, 35, 5, 11, 0, 0,
        35, 5, 1, 0, 0, 0, 36, 37, 3, 8, 4, 0, 37, 38, 3, 12, 6, 0, 38, 7, 1, 0, 0, 0, 39, 41, 5, 3,
        0, 0, 40, 42, 3, 10, 5, 0, 41, 40, 1, 0, 0, 0, 42, 43, 1, 0, 0, 0, 43, 41, 1, 0, 0, 0, 43,
        44, 1, 0, 0, 0, 44, 9, 1, 0, 0, 0, 45, 46, 5, 5, 0, 0, 46, 47, 5, 1, 0, 0, 47, 11, 1, 0, 0,
        0, 48, 51, 5, 12, 0, 0, 49, 52, 3, 14, 7, 0, 50, 52, 3, 16, 8, 0, 51, 49, 1, 0, 0, 0, 51,
        50, 1, 0, 0, 0, 52, 53, 1, 0, 0, 0, 53, 51, 1, 0, 0, 0, 53, 54, 1, 0, 0, 0, 54, 13, 1, 0, 0,
        0, 55, 59, 5, 7, 0, 0, 56, 58, 3, 16, 8, 0, 57, 56, 1, 0, 0, 0, 58, 61, 1, 0, 0, 0, 59, 57,
        1, 0, 0, 0, 59, 60, 1, 0, 0, 0, 60, 62, 1, 0, 0, 0, 61, 59, 1, 0, 0, 0, 62, 63, 3, 18, 9, 0,
        63, 64, 5, 8, 0, 0, 64, 65, 5, 12, 0, 0, 65, 15, 1, 0, 0, 0, 66, 67, 3, 18, 9, 0, 67, 68,
        5, 12, 0, 0, 68, 17, 1, 0, 0, 0, 69, 71, 3, 20, 10, 0, 70, 69, 1, 0, 0, 0, 71, 72, 1, 0, 0,
        0, 72, 70, 1, 0, 0, 0, 72, 73, 1, 0, 0, 0, 73, 19, 1, 0, 0, 0, 74, 76, 5, 5, 0, 0, 75, 74,
        1, 0, 0, 0, 75, 76, 1, 0, 0, 0, 76, 77, 1, 0, 0, 0, 77, 78, 5, 2, 0, 0, 78, 79, 5, 1, 0, 0,
        79, 21, 1, 0, 0, 0, 7, 30, 43, 51, 53, 59, 72, 75
    ]


class mingyu_grammarParser(Parser):
    grammarFileName = "mingyu_grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                    "<INVALID>", "<INVALID>", "<INVALID>", "'|:'", "':|'",
                    "'{'", "'['", "']'", "'|'", "'}'"]

    symbolicNames = ["<INVALID>", "SOUND_HEIGHT", "SOUND_LENGTH", "CLEF",
                     "PAUSE", "MODIFIER", "METER", "REPEAT_START", "REPEAT_END",
                     "PIECE_BEGIN", "MELODY_BEGIN", "MELODY_END", "TACT_BEGIN_END",
                     "PIECE_END", "WS"]

    RULE_piece = 0
    RULE_melody_lines = 1
    RULE_melody_line = 2
    RULE_melody_content = 3
    RULE_clef_preamble = 4
    RULE_modifier_with_note = 5
    RULE_tacts = 6
    RULE_tacts_with_repetition = 7
    RULE_tact = 8
    RULE_notes = 9
    RULE_note = 10

    ruleNames = ["piece", "melody_lines", "melody_line", "melody_content",
                 "clef_preamble", "modifier_with_note", "tacts", "tacts_with_repetition",
                 "tact", "notes", "note"]

    EOF = Token.EOF
    SOUND_HEIGHT = 1
    SOUND_LENGTH = 2
    CLEF = 3
    PAUSE = 4
    MODIFIER = 5
    METER = 6
    REPEAT_START = 7
    REPEAT_END = 8
    PIECE_BEGIN = 9
    MELODY_BEGIN = 10
    MELODY_END = 11
    TACT_BEGIN_END = 12
    PIECE_END = 13
    WS = 14

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class PieceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PIECE_BEGIN(self):
            return self.getToken(mingyu_grammarParser.PIECE_BEGIN, 0)

        def METER(self):
            return self.getToken(mingyu_grammarParser.METER, 0)

        def melody_lines(self):
            return self.getTypedRuleContext(mingyu_grammarParser.Melody_linesContext, 0)

        def PIECE_END(self):
            return self.getToken(mingyu_grammarParser.PIECE_END, 0)

        def getRuleIndex(self):
            return mingyu_grammarParser.RULE_piece

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterPiece"):
                listener.enterPiece(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitPiece"):
                listener.exitPiece(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitPiece"):
                return visitor.visitPiece(self)
            else:
                return visitor.visitChildren(self)

    def piece(self):

        localctx = mingyu_grammarParser.PieceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_piece)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(mingyu_grammarParser.PIECE_BEGIN)
            self.state = 23
            self.match(mingyu_grammarParser.METER)
            self.state = 24
            self.melody_lines()
            self.state = 25
            self.match(mingyu_grammarParser.PIECE_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Melody_linesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def melody_line(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(mingyu_grammarParser.Melody_lineContext)
            else:
                return self.getTypedRuleContext(mingyu_grammarParser.Melody_lineContext, i)

        def getRuleIndex(self):
            return mingyu_grammarParser.RULE_melody_lines

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterMelody_lines"):
                listener.enterMelody_lines(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitMelody_lines"):
                listener.exitMelody_lines(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMelody_lines"):
                return visitor.visitMelody_lines(self)
            else:
                return visitor.visitChildren(self)

    def melody_lines(self):

        localctx = mingyu_grammarParser.Melody_linesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_melody_lines)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 27
                self.melody_line()
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la == 10):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Melody_lineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MELODY_BEGIN(self):
            return self.getToken(mingyu_grammarParser.MELODY_BEGIN, 0)

        def melody_content(self):
            return self.getTypedRuleContext(mingyu_grammarParser.Melody_contentContext, 0)

        def MELODY_END(self):
            return self.getToken(mingyu_grammarParser.MELODY_END, 0)

        def getRuleIndex(self):
            return mingyu_grammarParser.RULE_melody_line

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterMelody_line"):
                listener.enterMelody_line(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitMelody_line"):
                listener.exitMelody_line(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMelody_line"):
                return visitor.visitMelody_line(self)
            else:
                return visitor.visitChildren(self)

    def melody_line(self):

        localctx = mingyu_grammarParser.Melody_lineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_melody_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(mingyu_grammarParser.MELODY_BEGIN)
            self.state = 33
            self.melody_content()
            self.state = 34
            self.match(mingyu_grammarParser.MELODY_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Melody_contentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def clef_preamble(self):
            return self.getTypedRuleContext(mingyu_grammarParser.Clef_preambleContext, 0)

        def tacts(self):
            return self.getTypedRuleContext(mingyu_grammarParser.TactsContext, 0)

        def getRuleIndex(self):
            return mingyu_grammarParser.RULE_melody_content

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterMelody_content"):
                listener.enterMelody_content(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitMelody_content"):
                listener.exitMelody_content(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMelody_content"):
                return visitor.visitMelody_content(self)
            else:
                return visitor.visitChildren(self)

    def melody_content(self):

        localctx = mingyu_grammarParser.Melody_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_melody_content)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.clef_preamble()
            self.state = 37
            self.tacts()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Clef_preambleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLEF(self):
            return self.getToken(mingyu_grammarParser.CLEF, 0)

        def modifier_with_note(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(mingyu_grammarParser.Modifier_with_noteContext)
            else:
                return self.getTypedRuleContext(mingyu_grammarParser.Modifier_with_noteContext, i)

        def getRuleIndex(self):
            return mingyu_grammarParser.RULE_clef_preamble

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterClef_preamble"):
                listener.enterClef_preamble(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitClef_preamble"):
                listener.exitClef_preamble(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitClef_preamble"):
                return visitor.visitClef_preamble(self)
            else:
                return visitor.visitChildren(self)

    def clef_preamble(self):

        localctx = mingyu_grammarParser.Clef_preambleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_clef_preamble)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(mingyu_grammarParser.CLEF)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 40
                self.modifier_with_note()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la == 5):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Modifier_with_noteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MODIFIER(self):
            return self.getToken(mingyu_grammarParser.MODIFIER, 0)

        def SOUND_HEIGHT(self):
            return self.getToken(mingyu_grammarParser.SOUND_HEIGHT, 0)

        def getRuleIndex(self):
            return mingyu_grammarParser.RULE_modifier_with_note

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterModifier_with_note"):
                listener.enterModifier_with_note(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitModifier_with_note"):
                listener.exitModifier_with_note(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitModifier_with_note"):
                return visitor.visitModifier_with_note(self)
            else:
                return visitor.visitChildren(self)

    def modifier_with_note(self):

        localctx = mingyu_grammarParser.Modifier_with_noteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_modifier_with_note)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(mingyu_grammarParser.MODIFIER)
            self.state = 46
            self.match(mingyu_grammarParser.SOUND_HEIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TactsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TACT_BEGIN_END(self):
            return self.getToken(mingyu_grammarParser.TACT_BEGIN_END, 0)

        def tacts_with_repetition(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(mingyu_grammarParser.Tacts_with_repetitionContext)
            else:
                return self.getTypedRuleContext(mingyu_grammarParser.Tacts_with_repetitionContext, i)

        def tact(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(mingyu_grammarParser.TactContext)
            else:
                return self.getTypedRuleContext(mingyu_grammarParser.TactContext, i)

        def getRuleIndex(self):
            return mingyu_grammarParser.RULE_tacts

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterTacts"):
                listener.enterTacts(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitTacts"):
                listener.exitTacts(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitTacts"):
                return visitor.visitTacts(self)
            else:
                return visitor.visitChildren(self)

    def tacts(self):

        localctx = mingyu_grammarParser.TactsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tacts)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(mingyu_grammarParser.TACT_BEGIN_END)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 51
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [7]:
                    self.state = 49
                    self.tacts_with_repetition()
                    pass
                elif token in [2, 5]:
                    self.state = 50
                    self.tact()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 164) != 0):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Tacts_with_repetitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REPEAT_START(self):
            return self.getToken(mingyu_grammarParser.REPEAT_START, 0)

        def notes(self):
            return self.getTypedRuleContext(mingyu_grammarParser.NotesContext, 0)

        def REPEAT_END(self):
            return self.getToken(mingyu_grammarParser.REPEAT_END, 0)

        def TACT_BEGIN_END(self):
            return self.getToken(mingyu_grammarParser.TACT_BEGIN_END, 0)

        def tact(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(mingyu_grammarParser.TactContext)
            else:
                return self.getTypedRuleContext(mingyu_grammarParser.TactContext, i)

        def getRuleIndex(self):
            return mingyu_grammarParser.RULE_tacts_with_repetition

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterTacts_with_repetition"):
                listener.enterTacts_with_repetition(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitTacts_with_repetition"):
                listener.exitTacts_with_repetition(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitTacts_with_repetition"):
                return visitor.visitTacts_with_repetition(self)
            else:
                return visitor.visitChildren(self)

    def tacts_with_repetition(self):

        localctx = mingyu_grammarParser.Tacts_with_repetitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_tacts_with_repetition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(mingyu_grammarParser.REPEAT_START)
            self.state = 59
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 4, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 56
                    self.tact()
                self.state = 61
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 4, self._ctx)

            self.state = 62
            self.notes()
            self.state = 63
            self.match(mingyu_grammarParser.REPEAT_END)
            self.state = 64
            self.match(mingyu_grammarParser.TACT_BEGIN_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TactContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def notes(self):
            return self.getTypedRuleContext(mingyu_grammarParser.NotesContext, 0)

        def TACT_BEGIN_END(self):
            return self.getToken(mingyu_grammarParser.TACT_BEGIN_END, 0)

        def getRuleIndex(self):
            return mingyu_grammarParser.RULE_tact

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterTact"):
                listener.enterTact(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitTact"):
                listener.exitTact(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitTact"):
                return visitor.visitTact(self)
            else:
                return visitor.visitChildren(self)

    def tact(self):

        localctx = mingyu_grammarParser.TactContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_tact)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.notes()
            self.state = 67
            self.match(mingyu_grammarParser.TACT_BEGIN_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NotesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def note(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(mingyu_grammarParser.NoteContext)
            else:
                return self.getTypedRuleContext(mingyu_grammarParser.NoteContext, i)

        def getRuleIndex(self):
            return mingyu_grammarParser.RULE_notes

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterNotes"):
                listener.enterNotes(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitNotes"):
                listener.exitNotes(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitNotes"):
                return visitor.visitNotes(self)
            else:
                return visitor.visitChildren(self)

    def notes(self):

        localctx = mingyu_grammarParser.NotesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_notes)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 69
                self.note()
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la == 2 or _la == 5):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NoteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SOUND_LENGTH(self):
            return self.getToken(mingyu_grammarParser.SOUND_LENGTH, 0)

        def SOUND_HEIGHT(self):
            return self.getToken(mingyu_grammarParser.SOUND_HEIGHT, 0)

        def MODIFIER(self):
            return self.getToken(mingyu_grammarParser.MODIFIER, 0)

        def getRuleIndex(self):
            return mingyu_grammarParser.RULE_note

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterNote"):
                listener.enterNote(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitNote"):
                listener.exitNote(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitNote"):
                return visitor.visitNote(self)
            else:
                return visitor.visitChildren(self)

    def note(self):

        localctx = mingyu_grammarParser.NoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_note)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 5:
                self.state = 74
                self.match(mingyu_grammarParser.MODIFIER)

            self.state = 77
            self.match(mingyu_grammarParser.SOUND_LENGTH)
            self.state = 78
            self.match(mingyu_grammarParser.SOUND_HEIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
