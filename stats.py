def chr_count(text):
    text = text.lower()
    count = {}
    
    for chr in text:
        if chr in count:
            count[chr] += 1
        else:
            count[chr] = 1
    return count


def short(items):
    return items[1]

