def get_next_free_man(m_free):
    # try to find a free man; else None
    for k in m_free:
        if m_free[k]:
            return k

def gale_shapley(m, w, m_prefs, w_prefs):
    w_engage = {x: None for x in w}
    m_free = {x: True for x in m}

    next_m = m[0]
    while next_m:
        next_w = m_prefs[next_m].pop(0)

        if w_engage[next_w] == None:
            w_engage[next_w] = next_m  # they become engaged
            m_free[next_m] = False     # m no longer free
        
        else:
            curr_m = w_engage[next_w]
            curr_rank = w_prefs[next_w].index(curr_m)
            next_rank = w_prefs[next_w].index(next_m)
            
            if next_rank > curr_rank:
                w_engage[next_w] = next_m
                m_free[next_m] = False
                m_free[curr_m] = True

        next_m = get_next_free_man(m_free)
    return list(w_engage.items())     # [(w, m), (w1, m1)]