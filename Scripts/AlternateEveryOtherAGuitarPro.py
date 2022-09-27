from hashlib import new
import guitarpro
demo = guitarpro.parse("C:\\temp\C Major Scales 3s.gp5")
measures = demo.tracks[0].measures

for measure in demo.tracks[0].measures: 
    try:
        newl = list()
        newl.insert(0,measure.voices[0].beats[0])
        newl.insert(1,measure.voices[0].beats[1])
        newl.insert(2,measure.voices[0].beats[2])

        newl.insert(3,measure.voices[0].beats[5])
        newl.insert(4,measure.voices[0].beats[4])
        newl.insert(5,measure.voices[0].beats[3])

        newl.insert(6,measure.voices[0].beats[6])
        newl.insert(7,measure.voices[0].beats[7])
        newl.insert(8,measure.voices[0].beats[8])

        newl.insert(9,measure.voices[0].beats[11])
        newl.insert(10,measure.voices[0].beats[10])
        newl.insert(11,measure.voices[0].beats[9])

        measure.voices[0].beats = newl
    except: 
        print("opps")

#measures.reverse()

guitarpro.write(demo,"C:\\temp\C Major Scales 3s - EveryOther.gp5")