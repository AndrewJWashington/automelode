import mido

song = mido.MidiFile()

track = mido.MidiTrack()
song.tracks.append(track)

root_note = 69
note = root_note
last_note = root_note
tonality = 'major'

ascending = True
note_in_key = 0  # 0-7

if tonality == 'major':
    notes_in_key = [root_note,
                    root_note + 2,   # whole
                    root_note + 4,   # whole
                    root_note + 5,   # half
                    root_note + 7,   # whole
                    root_note + 9,   # whole
                    root_note + 11,  # whole
                    root_note + 12,  # half\
                    ]


for i in range(15):
    # determine next note to play
    if ascending:
        if note_in_key + 1 < len(notes_in_key):
            note_in_key = note_in_key + 1
            note = notes_in_key[note_in_key]
        else:
            ascending = False
    else:
        if note_in_key - 1 >= 0:
            note_in_key = note_in_key - 1
            note = notes_in_key[note_in_key]
        else:
            ascending = True

    # how loud to play it
    velocity_on = 64
    velocity_off = 127

    # how long to play it
    time_on = 124
    time_off = 4

    # logging
    print('note:', note)
    print('time_on:', time_on)
    print('time_off:', time_off)
    print()

    # write note to track
    track.append(mido.Message('note_on', note=note, velocity=velocity_on, time=time_on))
    track.append(mido.Message('note_off', note=note, velocity=velocity_off, time=time_off))

    # end of loop clean up
    last_note = note

song.save('new_song.mid')
