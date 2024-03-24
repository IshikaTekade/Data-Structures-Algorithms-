def function(S,T):
    if len(S)!=len(T):
        return 0
    
    s_to_t={}
    t_to_s={}

    for s,t in zip(S,T):
        if s in s_to_t and s_to_t[s]!=t:
            return 0
        if t in t_to_s and t_to_s[t]!=s:
            return 0
        s_to_t[s]=T
        t_to_s[t]=S
    return 1
S="ACAB"
T="XCVY"
print(function(S,T))
