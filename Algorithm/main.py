
class Class:
    def __init__(self, id, professor, writing_seminar, language):
        self.id = id
        self.professor = professor
        self.writing_seminar = writing_seminar
        self.language = language


def sortClasses(S,C):
    classInterestCount = {}
    for s in S:
        for p in S[s]:
            #and p is not a first year seminar
            if p in classInterestCount.keys():
                classInterestCount[p] = 1
            else:
                #if p first year seminar, classInterestCount[p] = 0
                classInterestCount[p] = 1
    #sort by highest interest, descending order
    sorted_classInterestCount = sorted(classInterestCount.items(), key=lambda x: x[1], reverse=True)
    return sorted_classInterestCount

#I think we should preprocess T such that it is a tuple
def sortClassTimes(T):
    classTimeConflicts = {}
    sortedClassTimes = []
    T.sort(key=lambda x: x[3])
    for t in T:
        classTimeConflicts[t[0]]

def identifyRoomsForClass(R,C):
    sorted_Rooms = sorted(R.items(), key=lambda x: x[1], reverse=True)
    return sorted_Rooms

def setUpAvailabilty(input, sortedClassTimes):
    availability = {}
    for r in input:
        isOpen = {}
        for t in sortedClassTimes:
            isOpen[t] = "True"
