import sys

pairs = [["x","خ"],["a","ا"],["b","ب"],["c","ج"],["ç","چ"],["d","د"],["e","ە"],["ê","ێ"],["f","ف"],
        ["hh","ح"],["gh","غ"],["g","گ"],["h","ه"],["i",""],["3","ع"],
        ["î","ی"],["j","ژ"],["k","ک"],["ll","ڵ"],["l","ل"],["m","م"],
        ["n","ن"],["o","ۆ"],["p","پ"],["q","ق"],["rr","ڕ"],["r","ر"],["sh","ش"],["ş","ش"],["s","س"],["t","ت"],
        ["û","وو"],["u","وو"],["w","و"],["v","ڤ"],["y","ی"],["z","ز"]]

def translit(word):
    out = word.strip()
    if " " in out:
        o = ""
        for item in out.split(" "):
            o += translit(item) + " "
        return o.strip()
    if len(out) == 0:
        return ""
    if out[0] == "u":
        out = "ئو" + out[1:]
    if out[0] == "î":
        out = "ئی" + out[1:]
    if out[0] == "e":
        out = "ئە" + out[1:]
    if out[0] == "o":
        out = "ئۆ" + out[1:]
    if out[0] == "a":
        out = "ئا" + out[1:]
    if out[0] == "ê":
        out = "ئێ" + out[1:]
    if out[-1] == "i":
        out = out[:-1] + "ی"
    if out[-1] == "e":
        out = out[:-1] + "ە"
    out.replace("ye","یە")
    for pair in pairs:
        out = out.replace(pair[0],pair[1])
    return out


if __name__ == "__main__":
    for line in sys.stdin:
        sys.stdout.write(translit(line) + "\n")
