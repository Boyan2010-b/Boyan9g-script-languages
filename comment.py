def process_comment(comment):
    words = comment.split()
    if len(words) <= 8:

        if words: 
            words[0] = words[0].capitalize()
        formatted_comment = " ".join(words)
        print(f"Yes. Formatted comment: {formatted_comment}")
    else:
        print("No.Тhe comment exceeds 8 words")

user_comment = input("Int comment: ")
process_comment(user_comment)

