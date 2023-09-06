import requests

SEARCHKEY = "tap:"
SWIPESEARCH = "swipe:"

class IDProcesser:
    def scan_to_800(scan: str):
        if(scan[:2] == "80"):
            return scan
        try:
            idStart = scan.index(SEARCHKEY) + len(SEARCHKEY)
        except:
            idStart = scan.index(SWIPESEARCH) + len(SWIPESEARCH)
        
        cardID = scan[idStart:idStart + 16]
        print(f"cardID {cardID}")
        return IDProcesser.getNinerID(cardID)

    
    def getNinerID(cardID) -> int:
        request = requests.get(f"https://careerapps.charlotte.edu/checkin/fair/getID.php?ID={cardID}")
        content = request.json()
        print(f"content {content}")
        NinerID = content['UNCC_ID']
        return int(NinerID)