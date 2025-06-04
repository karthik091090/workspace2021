f = open("./PythonSamples/file/demofile.txt", "r")
# print(f.read())

print(f.read(5))
f.close()


f = open("./PythonSamples/file/demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()