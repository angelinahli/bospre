# INTERVAL SCHEDULING

def interval_schedule(events):
    sorted_events = sorted(events, key=lambda e: e["et"])
    event_order = [sorted_events[0]]
    for event in sorted_events[1:]:
        if event["st"] >= event_order[-1]["et"]:
            event_order.append(event)
    return event_order

if __name__ == "__main__":
    events = [
        {"st": 1.5, "et": 4},
        {"st": 3, "et": 3.5},
        {"st": 8, "et": 9},
        {"st": 4, "et": 8},
        {"st": 5, "et": 7}
    ]
    print(interval_schedule(events))