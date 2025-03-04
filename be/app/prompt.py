def template_from_message(msg: str) :
    messages = []
    with open("context.txt", "r") as f:
        context = f.read()
    messages.append({
        "role": "system",
        "message": f"""Kamu adalah penjawab pertanyaan handal\n
        Kamu menjawab pertanyaan dengan seefisien mungkin\n
        Jawab pertanyaan hanya berdasarkan konteks berikut\n
        {context}
        """
    })
    
    messages.append({
        "role": "user",
        "message": msg
    })
    
    return messages
    