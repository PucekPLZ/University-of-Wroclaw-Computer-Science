def eval_string(w):
    z = w
    czy = False
    while czy != True:
        l = z.split()
        t = z.split()
        czy = True

        e = False

        for j in range(len(l)):
            if l[j] == "*" or l[j] == "//":
                e = True

        for j in range(len(l)):
            if e:
                if l[j] == "*":
                    x = int(l[j-1]) * int(l[j+1])
                    t[j-1] = ""
                    t[j+1] = ""
                    for i in range(len(t)):
                        if t[i] == "*":
                            t[i] = str(x)
                            break
                    break
            
                if l[j] == "//":
                    x = int(l[j-1]) // int(l[j+1])
                    t[j-1] = ""
                    t[j+1] = ""
                    for i in range(len(t)):
                        if t[i] == "//":
                            t[i] = str(x)
                            break
                    break
            else:
                if l[j] == "+":
                    x = int(l[j-1]) + int(l[j+1])
                    t[j-1] = ""
                    t[j+1] = ""
                    for i in range(len(t)):
                        if t[i] == "+":
                            t[i] = str(x)
                            break
                    break
            
                if l[j] == "-":
                    x = int(l[j-1]) - int(l[j+1])
                    t[j-1] = ""
                    t[j+1] = ""
                    for i in range(len(t)):
                        if t[i] == "-":
                            t[i] = str(x)
                            break
                    break

        z = " ".join(t)

        for j in range(len(z)):
            if z[j] == "*" or z[j] == "//" or z[j] == "-" or z[j] == "+":
                czy = False
    return z
                
        


w = "7 // 3 + 2 * 2 * 6 + 2 - 10"

print(eval_string(w))
print(eval(w))