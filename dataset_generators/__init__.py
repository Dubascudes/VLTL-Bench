import random


def parse_object_names(filename):
    """
    Reads a file of object names and returns a dict mapping canonical names to lists of synonyms.
    Expected file format: 'canonical: alt1, alt2, ...'
    """
    object_dict = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or ':' not in line:
                continue
            canonical, alts_str = line.split(':', 1)
            canonical = canonical.strip()
            alt_list = [alt.strip() for alt in alts_str.split(',') if alt.strip()]
            object_dict[canonical] = alt_list
    return object_dict


def build_actions_dict(is_stl=False):
    """
    Returns a dictionary mapping canonical actions to lists of action synonyms.
    """
    actions = {
        # ── warehouse verbs ───────────────────────────────────────────────
        "search":       ["locate", "find", "look for", "search for"],
        "pickup":       ["pick up", "grab", "retrieve", "collect"],
        "deliver":      ["deliver", "drop off", "hand over", "transport"],
        "idle":         ["idle", "wait", "remain still", "stand by"],

        # ── search_and_rescue verbs ───────────────────────────────────────
        "go_home":      ["return to base", "go home", "return home", "go back to base"],
        "communicate":  ["talk to", "communicate with", "establish communication with"],
        "deliver_aid":  ["give aid to", "deliver aid to", "provide assistance to"],
        "record":       ["record", "begin recording", "take a video of"],
        "photo":         ["photograph", "take a picture of", "take a photo of"],
        "avoid":        ["avoid", "stay away from", "do not go near"],

        # ── traffic_light verbs ───────────────────────────────────────────
        "get_help":     ["call for help", "request assistance", "get help"],
        "change":       ["change", "switch", "set", "update"],
        "record":       ["record", "begin recording", "take a video of"],
        "photo":         ["photograph", "take a picture of", "take a photo of"]
    }

    return actions

__all__ = ['parse_object_names', 'build_actions_dict'] 