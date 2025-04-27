from pydub import AudioSegment
import csv
import os

# setting frequency size (in milliseconds)
freq = 10

#folderNot = os.listdir('/Users/zoeakpan/wav to csv/not')
#print(folderNot)

# folder im gonna iterate through
folderScreaming = os.listdir('/Users/zoeakpan/wav to csv/screaming')

for file in folderScreaming:
    print(file)
    # convert to audio object 
    filePath = os.path.join('/Users/zoeakpan/wav to csv/screaming', file)
    audio = AudioSegment.from_wav(filePath)

    csv_filename = file.replace('.wav', '.csv')
    output_csv = os.path.join('/Users/zoeakpan/wav to csv/screamingCSV', csv_filename)

    with open(output_csv, mode='w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(['seconds_elapsed', 'dBFS'])  # header

# just going over an interval from 0 to 10s in intervals of 0.1 seconds (10 ms)
        for i in range(0, len(audio), freq):
            audioWindow = audio[i:i + freq]
            secondsElapsed = i / 1000.0  # ms to seconds
            dBFS = audioWindow.dBFS if audioWindow.dBFS != float('-inf') else -100 # p sure this is in the case where it's silent
            # writing row to file 
            writer.writerow([secondsElapsed, dBFS])

print("finished w/not")
