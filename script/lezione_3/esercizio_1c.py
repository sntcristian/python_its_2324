def count_words(lyrics):
    list_of_words = lyrics.split(" ")
    dict_of_words = dict()
    words_to_remove = ['a', 'i', 'am', 'to', ';;', 'the', 'you', 'don’t', 'and', 'that', 'i’m', 'it’s']
    for word in list_of_words:
        if word not in words_to_remove:
            if word not in dict_of_words:
                dict_of_words[word]=1
            dict_of_words[word]+=1
    return dict_of_words

lyrics = "well i’m so above you ;; and it’s plain to see ;; but i came to love you anyway ;; so you pulled my heart out ;; and i don’t mind bleeding ;; any old time you keep me waiting ;; waiting, waiting ;; oh, oh-oh i got a love that keeps me waiting ;; oh, oh-oh i got a love that keeps me waiting ;; i’m a lonely boy ;; i’m a lonely boy ;; oh, oh-oh i got a love that keeps me waiting ;; well your mama kept you but your daddy left you ;; and i should’ve done you just the same ;; but i came to love you ;; am i born to bleed? ;; any old time you keep me waiting ;; waiting, waiting ;; oh, oh-oh i got a love that keeps me waiting ;; oh, oh-oh i got a love that keeps me waiting ;; i’m a lonely boy ;; i’m a lonely boy ;; oh, oh-oh i got a love that keeps me waiting ;; hey! ;; oh, oh-oh i got a love that keeps me waiting ;; oh, oh-oh i got a love that keeps me waiting ;; i’m a lonely boy ;; i’m a lonely boy ;; oh, oh-oh i got a love that keeps me waiting"

dict_of_words = count_words(lyrics)
print(dict_of_words)