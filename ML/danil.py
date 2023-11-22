import pymorphy2

def to_plural(word):
    parse_results = pymorphy2.MorphAnalyzer().parse(word)
    if not parse_results:
        return word

    m = parse_results[0]
    if m.tag.POS == "NOUN":
        return m.inflect({'plur'}).word
    else:
        return word
