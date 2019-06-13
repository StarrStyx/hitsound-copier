# yea idk wot Im doing
import os

# input for osu filename
# mapfile = input("Target .osu filename: ")
# mapfile = input("Hitsounded .osu filename: ")

###########################################################################

# reading the file: testing with .osu
mapfileinput = "testfiles\\bios_hs.osu"
mapfilehitsound = "testfiles\\bios_nohs.osu"
mapfilebackup = mapfileinput + ".bak"
asdf = "testfiles\\debug.txt"

# reading the file: testing with .txt
# mapfileinput = "testfiles\\in.txt"
# mapfilehitsound = "testfiles\\original.txt"
# mapfilebackup = mapfileinput + ".bak"

##########################################################################

# read mode for specified files
input = open(mapfileinput, "r")
hitsound = open(mapfilehitsound, "r")

# write mode for specified files
backup = open(mapfilebackup, "w")
debug_timingpoints = open(asdf, "w")

##########################################################################

# takes in .osu as string
mapdata_input = input.read()
mapdata_hitsound = hitsound.read()

# print(mapdata)

# backup input .osu
backup.write(mapdata)

##########################################################################

# takes timing points
timingpoints_input = mapdata_input.partition("[TimingPoints]")[2].partition("[HitObjects]")[0]
timingpoints_hitsound = mapdata_hitsound.partition("[TimingPoints]")[2].partition("[HitObjects]")[0]

# takes hitobjects
hitobjects_input = mapdata_input.partition("[HitObjects]")[2]
hitobjects_hitsound = mapdata_hitsound.partition("[HitObjects]")[2]

##########################################################################

for line in timingpoints_input:
    if line in ['\n', '\r\n']:
        print("blank line aaa")

##########################################################################

debug_timingpoints.write(timingpoints_input)

print(timingpoints_input)
print(hitobjects_input)

# debug
print(mapfileinput)
print(mapfilebackup)
print(os.path.basename(mapfilebackup))

print(input.name)
# print(info)

# replaces original osu
# output = open(mapfileinput, "w")
# aaaa = debug_timingpoints.write(timingpoints)