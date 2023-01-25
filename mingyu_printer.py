import abjad


class mingyuPrinter:
    length_translator = {
        "whole_dot": "1.",
        "whole": "1",
        "half_dot": "2.",
        "half": "2",
        "quarter_dot": "4.",
        "quarter": "4",
        "eighth_dot": "8.",
        "eighth": "8",
        "sixteenth_dot": "16.",
        "sixteenth": "16",
        "thirtysecond_dot": "32.",
        "thirtysecond": "32",
        "sixtyfourth_dot": "64.",
        "sixtyfourth": "64"
    }

    octave_translator = {
        1: ",,",
        2: ",",
        3: "",
        4: "\'",
        5: "\'\'",
        6: "\'\'\'",
        7: "\'\'\'\'",
        8: "\'\'\'\'\'"
    }

    sharps_keys = ["g", "d", "a", "e", "b", "fs"]
    flats_keys = ["f", "bf", "ef", "af", "df", "gf"]

    def __init__(self):
        self.meter = ""
        self.voice_strings = []
        self.clefs = []
        self.key_signs = []
        self.keys = []
        self.repetitions = []
        self.number_of_notes_per_voice = []

    def add_note(self, index, length, height, modifier):
        # translating note name to abjad library format
        self.voice_strings[index] += height[0].lower()
        # translating modifier
        if modifier is not None:
            if modifier == "sharp":
                self.voice_strings[index] += "s"
            if modifier == "flat":
                self.voice_strings[index] += "f"
        # translating height of a note to abjad library format
        octave_height = int(height[1])
        self.voice_strings[index] += mingyuPrinter.octave_translator[octave_height]

        # translating note length to abjad library format
        self.voice_strings[index] += mingyuPrinter.length_translator[length]
        self.voice_strings[index] += " "
        self.number_of_notes_per_voice[index] += 1

    def start_repetition(self, index):
        self.repetitions[index].append(self.number_of_notes_per_voice[index] - 1)

    def end_repetition(self, index):
        self.repetitions[index].append(self.number_of_notes_per_voice[index] - 1)

    def get_key(self, index):
        if self.key_signs[index] == 0:
            return "c"
        elif self.keys[index] == "sharp":
            return mingyuPrinter.sharps_keys[self.key_signs[index] - 1]
        elif self.keys[index] == "flat":
            return mingyuPrinter.flats_keys[self.key_signs[index] - 1]

    def get_clef(self, index):
        if self.clefs[index] == "violin":
            return "treble"
        else:
            return "bass"

    def generate_piece(self):
        time_signature = abjad.TimeSignature((int(self.meter[0]), int(self.meter[2])))
        staves = []
        for voice_string in self.voice_strings:
            staves.append(abjad.Staff(voice_string[:-1]))
        for i in range(0, len(staves), 1):
            for j in range(0, len(self.repetitions[i]), 1):
                if j % 2 == 0:
                    abjad.attach(abjad.BarLine(".|:"), staves[i][self.repetitions[i][j]])
                else:
                    abjad.attach(abjad.BarLine(":|."), staves[i][self.repetitions[i][j]])
            abjad.attach(abjad.KeySignature(abjad.NamedPitchClass(self.get_key(i)), abjad.Mode("major")),
                         abjad.select.note(staves[i], 0))
            abjad.attach(time_signature, abjad.select.note(staves[i], 0))
            abjad.attach(abjad.Clef(self.get_clef(i)), abjad.select.note(staves[i], 0))
        piece_staff = abjad.StaffGroup(staves)
        score = abjad.Score([piece_staff])
        abjad.persist.as_pdf(score, "output.pdf")