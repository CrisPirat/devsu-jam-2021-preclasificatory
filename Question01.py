def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

def isLowercase(s):
    return s.islower()

def isSizeConstraints(s):
    if 1 <= len(s) <= 2147483647:
        return True
    else :
        return False

def isSizeSubtextMinor(t,sT):
    if len(sT) <=  len(t) :
        return True
    else :
        return False

def findLastMatch(t, sT):
    findIndex = list(find_all(t,sT))
    if len(findIndex) >= 1:
       return findIndex[len(findIndex)-1]
    return -1
        
def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

def maximumDistance(text, subText):
    if isEnglish(text) and isEnglish(subText) and isLowercase(text) and isLowercase(subText):
        if isSizeConstraints(text) and isSizeConstraints(subText) and isSizeSubtextMinor(text,subText):
            return findLastMatch(text,subText)
    return -1

if __name__ == "__main__":
    
    #Examples
    print(maximumDistance("abcdefgci","de")) #output 3
    print(maximumDistance("abcdefgci","c")) #output 7
   
    #Test
    test01_text = "wmsbexxcherystodmtfvldoaazzwrcbnoxtrprmoxapcdtkedzyxebdeazzadueyvpudeinbzshoprybjgkaxyyajybslslcnlitdcfzoebcnnqlckjpwihmleezgtbrqmygdlqmabcwmjuzulgxfbimebehakskuptbizbnxepezlfujlkdtwpmweppkbqgymrepinn"
    test01_subText = "kasasdkydwg"
    print(maximumDistance(test01_text,test01_subText)) #output -1

    test02_text = "axucgrzqebtbuxpiyuavccltqwcmpzmmfaakncabbbdxepyevkswxhlellrfobyufmyumrorcgmjilzogezuggtxotzukeifvybxkacmwvkhswcoabmgwknminltbdqexopvysobpautmkmiuipuzfqpmwhwiyzdprxnadedrquxzassyfgrrjmgfenwmynehqnabgajrnfgdfvftghczetmhcakgnvjuuctufjgoqowhwtozkskaszvfpijugitoextqibynisnfbenweojapwtclszycusagzwbgavxawzfnuhmpddgzyymuxurdqkfkejsqdesmmzlxuokmloduolwyslonilvhjlqtftyxfoaopmvvomiddncnwqmxozqbmhuqpksuydcwwwuxvdfwrfiizcccktmfxcpdtunnknagsgntpnccgimnqketezhsbyrofjvwoqvturvwzttugivywdnqtzjnkyfdzkqcabyinwsowecczjgwwcgomuoogaxmbxcwjbjqozjxrzcyojylanjlpcdzgeraxhbaybxsuhcuvlsshmeblbdfaziubugweeckkvxqgtdrrsbxparablqpypqtenytfbntudlyakehtwhbbtngusmjaudcbazjfeqjufbileiwtylkkfkdmtertqzayaohzkuokkuplcwqrcwzxeqlzbhlubycufmwbvsbcseggwpmezxxnxmjcabibhjlurjtzuxxjartfgqogmrgpjigfazhpoaqggwpakbcxnghxhddcydmzqgsejyrstktdpcaeqpiqnzyebaioirhvlckxamorbriylesbwszzletemgyfcjyhpsmjandcxdrsjvfzuswuoxybtxzmhjqhbcxbhxdhbxjbrecpuvutlfyamkltfogwklisxhscgvwufckkszpejndjxzsaiuxengwgbpdssryllxmzgejtwmqyehdtymzivyygtqqbcu"
    test02_subText = "ggwp"
    print(maximumDistance(test02_text,test02_subText)) #output 770
    
    test03_text = "uepnzleaiogoxbvdcwalayckdzfzxdvddexcofcjlujrzofzolxmigtogtslkwwuxdilwmdjlpaqufnvuuufvhcmwpjqhlchtmqzrijwajbqzwrtzcmbwjvzfdhgunizgddehprykgvbpohccigzyvhintlpwotuvvlzrqicnavvnxfteduomtdjlwqyxbridegazizo"
    test03_subText = "egazizo"
    print(maximumDistance(test03_text,test03_subText)) #output 193 
    
