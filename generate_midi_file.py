import mido

ticks_per_beat = 96   # one quarter note is 96 ticks
# at 120 bpm, this is 96*120=11,520 ticks per minute
song = mido.MidiFile(ticks_per_beat=ticks_per_beat)

track = mido.MidiTrack()
song.tracks.append(track)

root_note = 50
note = root_note
last_note = root_note
tonality = 'major'

ascending = True
note_in_key = -1  # 0-7 typically, -1 since the loop increments

if tonality == 'major':
    notes_in_key = [root_note,
                    root_note + 2,   # whole
                    root_note + 4,   # whole
                    root_note + 5,   # half
                    root_note + 7,   # whole
                    root_note + 9,   # whole
                    root_note + 11,  # whole
                    ]


for i in range(11):
    # determine next note to play
    if ascending:
        if note_in_key < len(notes_in_key) - 2:
            note_in_key = note_in_key + 1
            note = notes_in_key[note_in_key]
        else:
            ascending = False
            note_in_key = note_in_key - 1
            note = notes_in_key[note_in_key]
    else:
        if note_in_key - 1 >= 0:
            note_in_key = note_in_key - 1
            note = notes_in_key[note_in_key]
        else:
            ascending = True
            note_in_key = note_in_key + 1
            note = notes_in_key[note_in_key]

    # how loud to play it
    velocity_on = 64
    velocity_off = 127

    # how long to play it
    time_between_notes = 2
    note_duration = 1 * ticks_per_beat - time_between_notes

    # logging
    print('note:', note)
    print('note_duration:', note_duration)
    print('time_between_notes:', time_between_notes)
    print()

    # write note to track
    track.append(mido.Message('note_on', note=note, velocity=velocity_on, time=time_between_notes))
    track.append(mido.Message('note_off', note=note, velocity=velocity_off, time=note_duration))

    # end of loop clean up
    last_note = note

song.save('new_song.mid')
