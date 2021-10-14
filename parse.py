#!/usr/bin/env python3

def parse_note(string, note_search, note_dict):
    note = get_note(string,note_search,note_dict)
    return(note, get_chord(string, note).lower())

def get_note(string, note_search, note_dict):
    for n in note_search:
            if n == string[:len(n)].capitalize():
                return note_dict[n]


def get_chord(string, note):
    return string[len(note):]

note_dict = {}
note_dict["C"] = "C"
note_dict["C#"] = "C#"
note_dict["Db"] = "C#"
note_dict["D"] = "D"
note_dict["D#"] = "D#"
note_dict["Eb"] = "D#"
note_dict["E"] = "E"
note_dict["F"] = "F"
note_dict["F#"] = "F#"
note_dict["Gb"] = "F#"
note_dict["G"] = "G"
note_dict["G#"] = "G#"
note_dict["Ab"] = "G#"
note_dict["A"] = "A"
note_dict["A#"] = "A#"
note_dict["Bb"] = "A#"
note_dict["B"] = "B"

notes_search_order = ["C#", "Db", "D#", "Eb", "F#", "Gb", "G#", "Ab", "A#", "Bb", "C", "D", "E", "F", "G", "A", "B"]

def main():
    note = ""
    pattern = ""
    user_input = input("Skriv ackord: ")

    print(parse_note(user_input, notes_search_order, note_dict))


if __name__ == "__main__":
    main()
