import marshal


file_org = input ("Your File 'py' >> : ")
open_read = open(file_org).read()
compi =compile(open_read, "", "exec" )
dumps_marsh = marshal.dumps(compi)
end_fil = open("eencrypt-"+ file_org,"w")

end_fil.write("import marshal\n")

end_fil.write("exec(marshal.loads("+repr(dumps_marsh)+"))")
end_fil.close()

print("Done !")

