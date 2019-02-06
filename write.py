f = open("examples", "r+")
f.write("line0")
current_position = f.tell()
f.seek(current_position+ 8)
f.write("line 6")
f.seek(0,2)
f.write("\nLine5")
f.close()


