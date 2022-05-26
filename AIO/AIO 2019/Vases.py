vasesin = open("vasesin.txt","r")
vasesout = open("vasesout.txt","w")
input = int(vasesin.read());
output = ' '

if input < 6:
    vasesout.write("0 0 0");
    vasesin.close();
    vasesout.close();
    exit()

input = [str((input - 3)), "1", "2"];
output = output.join(input);

vasesout.write(str(output));
vasesin.close();
vasesout.close();