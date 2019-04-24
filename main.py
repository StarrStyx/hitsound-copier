# imports?

# reading the file
# both files, in fact

# print("Please enter directory of .osu file")
in_input = input("Please enter directory of .osu file to copy from:")
out_input = input("Please enter directory of .osu file to copy to:")

print(in_input)
print(out_input)

in_osu = open("testing/one.osu","r")
out_osu = open("testing/two.osu","w")

# determines hitsounds to add

# puts them back in line?

# debug section
print(in_osu.read())

out_osu.write("yea lol")
out_osu.close()
