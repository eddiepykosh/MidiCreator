from midiutil.MidiFile import MIDIFile
import os

home = os.path.expanduser('~')
print(home)
docsHome = os.path.join(home, 'Documents')

folderCheck = os.path.isdir(docsHome)
if not (folderCheck):
    print("You do not have a documents folder")
    exit(-4)

#def export()
# create your MIDI object
mf = MIDIFile(1)     # only 1 track
track = 0   # the only track

time = 0    # start at the beginning
mf.addTrackName(track, time, "Sample Track")
mf.addTempo(track, time, 120)

# add some notes
channel = 0
volume = 100

pitch = 60           # C4 (middle C)
time = 0             # start on beat 0
duration = 0.5       # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)

pitch = 64           # E4
time = 2             # start on beat 2
duration = 1         # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)

pitch = 67           # G4
time = 4             # start on beat 4
duration = 1        # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)

pitch = 67           # G4
time = 5             # start on beat 5
duration = 1        # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)


# write it to disk
rawName =input("Give a name for the file: ")
fileName = rawName + ".mid"
outFile = "processing/"+fileName
with open(outFile, 'wb') as outf:
    mf.writeFile(outf)

toLY = "cd LilyPond/usr/bin/ &&  py midi2ly --output="
lyOut = '"C:/Users/Eddie/PycharmProjects/MidiCreator/processing" ' #need universal
lyIN = '"' "C:/Users/Eddie/PycharmProjects/MidiCreator/processing/" + fileName + '"' #need universal

alterName = rawName + "-midi.ly"

toPDF = "cd LilyPond/usr/bin/ &&  lilypond --output="
pdfOut = '"C:/Users/Eddie/PycharmProjects/MidiCreator/Final PDFs" ' #need universal
pdfIN = '"' "C:/Users/Eddie/PycharmProjects/MidiCreator/processing/" + alterName + '"' #need universal

stream = os.popen(toLY + lyOut +lyIN)
output = stream.read()
print (output)

stream = os.popen(toPDF + pdfOut + pdfIN)
output = stream.read()
print (output)

