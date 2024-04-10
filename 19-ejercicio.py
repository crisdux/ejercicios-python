# Dada una cadena de texto que represente una carita emoji se pide que se devuelva el emoji en cuestión.

def facemoji(emoji_text):
    emoji_text = emoji_text.lower()
    dict_emoji = {"happy": "😀", "sad": "😔", "angry":"😡", "pensive": "🤔", "surprised": "😮"}
    
    return dict_emoji[emoji_text]
    
print(facemoji("happy"))
print(facemoji("SAD"))
print(facemoji("Angry"))
print(facemoji("peNsive"))
print(facemoji("surpriseD"))