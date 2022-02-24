class Token:
    def saveToken(token):
        f = open("./static/data/token.dat", "w")
        f.write(token)
        f.close()

    def deleteToken():
        f = open("./static/data/token.dat", "w")
        f.write('')
        f.close()
    
    def getToken():
        f = open("./static/data/token.dat", "r")
        return f.read()


