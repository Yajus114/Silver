# simply exit

def main(self, args):
    if len(args) > 0 or "--h" in args:
        self.cout("///USAGE///\nlogout or exit")
        return
    self.cout("---SYSTEM EXIT AUTHORISED---")
    exit()
