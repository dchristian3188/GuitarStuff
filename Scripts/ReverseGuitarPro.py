import guitarpro
demo = guitarpro.parse("D:\GuitarPro\C Major Scales 3s.gp5")
measures = demo.tracks[0].measures

for measure in demo.tracks[0].measures: 
    measure.voices[0].beats.reverse()

measures.reverse()

guitarpro.write(demo,"D:\GuitarPro\C Major Scales 3s -reversed.gp5")