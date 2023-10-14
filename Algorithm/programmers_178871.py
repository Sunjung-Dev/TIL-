def solution(players, callings):
    answer = []
    
    for i in range(len(callings)):
        idx = players.index(callings[i])
        players[idx], players[idx-1] = players[idx-1], players[idx]
    
    answer = players
    return answer

solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"])

def solution(players, callings):
    rank_hash = {}  # 1: "mumu", 2:"soe", ...
    name_hash = {}  # "mumu": 1, "soe":2, ...

    for i in range(len(players)):
        rank_hash[i+1] = players[i]
        name_hash[players[i]] = i+1

    for call in callings:
        rank = name_hash[call]
        faster_name = rank_hash[rank-1]

        # rank change
        name_hash[call], name_hash[faster_name] = rank-1, rank
        rank_hash[rank-1], rank_hash[rank]  = call, faster_name

    return list(rank_hash.values())