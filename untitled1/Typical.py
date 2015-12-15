__author__ = 'joe'

class AddrBookEntry(object):
    def __init__(self, nm, ph):
        self.name = nm
        self.phone = ph
        print "create instance for:", self.name
    def update(self, newPh):
        self.phone = newPh
        print "update phone for:", self.name

class EmplAddrBookEntry(AddrBookEntry):
    " employee address book entry class "
    def __init__(self, nm, ph, id, em):
        AddrBookEntry.__init__(self, nm, ph)
        # super(EmplAddrBookEntry, self).__init__(self, nm, ph)
        self.id = id
        self.email = em
    def updateEmail(self, newEmail):
        self.email = newEmail
        print "update email for:", self.name

emp = EmplAddrBookEntry("joe", "200", "12", "www")
print emp