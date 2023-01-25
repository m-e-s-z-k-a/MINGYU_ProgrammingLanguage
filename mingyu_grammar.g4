grammar mingyu_grammar;

piece:
    PIECE_BEGIN METER melody_lines PIECE_END
    ;

melody_lines:
    melody_line+
    ;

melody_line:
    MELODY_BEGIN melody_content MELODY_END
    ;

melody_content:
    clef_preamble tacts
    ;

clef_preamble:
    CLEF modifier_with_note+
    ;

modifier_with_note:
    MODIFIER SOUND_HEIGHT
    ;

tacts:
    TACT_BEGIN_END (tacts_with_repetition | tact)+
    ;

tacts_with_repetition:
    REPEAT_START tact* notes REPEAT_END TACT_BEGIN_END
    ;

tact:
    notes  TACT_BEGIN_END
    ;

notes:
    note+
    ;

note:
    MODIFIER? SOUND_LENGTH SOUND_HEIGHT
    ;

SOUND_HEIGHT:
	('C'|'D'|'E'|'F'|'G'|'A'|'B')
	('is'|'es')?
	('1'|'2'|'3'|'4'|'5'|'6'|'7'|'8')
	;

SOUND_LENGTH:
    ('whole' | 'half' | 'quarter' | 'eighth' | 'sixteenth' | 'thirtysecond' | 'sixtyfourth')
    '_dot'?
    ;

CLEF:
    ('violin' | 'bass')
    ;

PAUSE:
    ('whole' | 'half' | 'quarter' | 'eighth' | 'sixteenth' | 'thirtysecond' | 'sixtyfourth')
    '_pause'
    ;

MODIFIER:
    ('sharp' | 'flat' | 'natural')
    ;

METER:
    ('2/4' | '3/4' | '4/4' | '5/4' | '6/4' | '3/8' | '6/8' | '9/8' | '12/8')
    ;

REPEAT_START:
    '|:'
    ;

REPEAT_END:
    ':|'
    ;

PIECE_BEGIN:
    '{'
    ;

MELODY_BEGIN:
    '['
    ;

MELODY_END:
    ']'
    ;

TACT_BEGIN_END:
    '|'
    ;

PIECE_END:
    '}'
    ;

WS
   : [ \t\n\r]+ -> skip
   ;
