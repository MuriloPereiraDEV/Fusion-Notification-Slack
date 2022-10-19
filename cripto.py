#FUNÇÃO QUE RECEBE UMA CHAVE, DECODIFICA E DEVOLVE ELA DECODIFICADA
def cripto(key):
    aux = ""
    for character in key:
        if character in "aA":
            aux += "."
        elif character in "bB":
            aux += "4"
        elif character in "cC":
            aux += "a"
        elif character in "dD":
            aux += "u"
        elif character in "dD":
            aux += "$"
        elif character in "eE":
            aux += "o"
        elif character in "fF":
            aux += "5"
        elif character in "gG":
            aux += "k"
        elif character in "hH":
            aux += "h"
        elif character in "iI":
            aux += "x"
        elif character in "jJ":
            aux += "-"
        elif character in "kK":
            aux += "6"
        elif character in "lL":
            aux += "/"
        elif character in "mM":
            aux += " "
        elif character in "nN":
            aux += "9"
        elif character in "oO":
            aux += "!"
        elif character in "pP":
            aux += "f"
        elif character in "qQ":
            aux += "7"
        elif character in "rR":
            aux += "+"
        elif character in "sS":
            aux += "#"
        elif character in "tT":
            aux += "b"
        elif character in "uU":
            aux += "@"
        elif character in "vV":
            aux += "ç"
        elif character in "wW":
            aux += "8"
        elif character in "xX":
            aux += "e"
        elif character in "yY":
            aux += "."
        elif character in "zZ":
            aux += "3"
        elif character in "0":
            aux += "a"
        elif character in "1":
            aux += "i"
        elif character in "2":
            aux += "f"
        elif character in "3":
            aux += "&"
        elif character in "4":
            aux += "d"
        elif character in "5":
            aux += "b"
        elif character in "6":
            aux += "m"
        elif character in "7":
            aux += "2"
        elif character in "8":
            aux += "y"
        elif character in "9":
            aux += "*"
        elif character in "/":
            aux +="l"
        elif character in "*":
            aux +="n"
        elif character in "-":
            aux +="t"
        elif character in "+":
            aux +="s"
        elif character in "!":
            aux +="r"
        elif character in "@":
            aux +="p"
        elif character in "#":
            aux +="0"
        elif character in "$":
            aux +="S"
    return aux
