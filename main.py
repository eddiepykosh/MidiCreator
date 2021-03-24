from midiutil.MidiFile import MIDIFile
import os

def pathMaker ():
    home = os.path.expanduser('~')
    # print(home)
    funcDocsHome = os.path.join(home, 'Documents', 'MidiCreator')
    # print(funcDocsHome)
    funcTempHome = os.path.join(funcDocsHome,'temp files')
    folderCheck = os.path.isdir(funcDocsHome)
    folderCheck2 = os.path.isdir(funcTempHome)
    if not folderCheck:
        print("You do not have a MidiCreator folder and the appropriate subfolder. Making one now")
        os.mkdir(funcDocsHome)
        os.mkdir(funcTempHome)
        folderCheck2 = True
    if not folderCheck2:
        print("You are missing a subfolder. Gonna fix that.")
        os.mkdir(funcTempHome)
    print("You can find the output folder at: " + funcDocsHome)
    return funcDocsHome


def midiMaker (tempHome):
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
    funcRawName =input("Give a name for the file: ")
    funcFileName = funcRawName + ".mid"
    outFile = tempHome +"/"+funcFileName
    with open(outFile, 'wb') as outf:
        mf.writeFile(outf)
    return funcRawName

def pdfMaker(rawName, fileName, tempHome, docsHome):

    toLilY = "cd LilyPond/usr/bin/ &&  py midi2ly --output="
    lilyOut = '"' + tempHome + '" '

    lilyIN = ' "' + tempHome + '/' + fileName + '"'

    alterName = rawName + "-midi.ly"

    toPDF = "cd LilyPond/usr/bin/ &&  lilypond --output="

    pdfOut = '"' + docsHome + '" '
    pdfIN = ' "' + tempHome+'/' + alterName + '"'
    # those past ten lines are UGLY but it works

    stream = os.popen(toLilY + lilyOut +lilyIN)
    output = stream.read()
    print(output)

    stream = os.popen(toPDF + pdfOut + pdfIN)
    output = stream.read()
    print(output)

def startup():
    menu = ('(1) Create the default Midi and pdf file\n'
            '(2) Create some random music\n'
            '(3) Covert your mid/midi file into a PDF\n'
            '(4) (nothing)\n'
            '(5) (nothing)\n'
            '(6) Exit.\n\n'
            'Enter Command:')

    userInput = input(menu)


    while userInput != '6':
        if userInput == '1':
            # print('hi')
            docsHome = pathMaker()
            tempHome = os.path.join(docsHome, 'temp files')
            rawName = midiMaker(tempHome)
            fileName = rawName + ".mid"
            pdfMaker(rawName, fileName, tempHome, docsHome)
            print("Done.")
        if userInput == '2':
            print("fuck you")
        if userInput == '3':
            print("fuck you")
        if userInput == '4':
            print("fuck you")
        if userInput == '5':
            print("fuck you")
        userInput = input('\nEnter command: ')
    print('Goodbye')

startup()


# docsHome = pathMaker()
# tempHome = os.path.join(docsHome, 'temp files')
# rawName = midiMaker()
# fileName = rawName + ".mid"
# pdfMaker(rawName, fileName)
