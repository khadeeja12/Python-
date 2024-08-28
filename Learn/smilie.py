def smilie(msg):
    emojis={
        "happy":"😊",
        "sad":"😔"
    }
    words=msg.split(" ")
    ret=""
    for word in words:
        if word in emojis:
            ret+=emojis[word]+" "
        else :
            ret+=word+" "
    return ret

x=input(" ")
print(smilie(x))

               