def choose_agent(user_query):

    query = user_query.lower()

    if any(word in query for word in ["study plan", "schedule", "exam", "timetable"]):
        return "Study Planner"

    elif any(word in query for word in ["notes", "note"]):
        return "Notes Generator"

    elif any(word in query for word in ["quiz", "mcq", "questions"]):
        return "Quiz Generator"

    elif any(word in query for word in ["code", "python", "java", "c program", "debug"]):
        return "Coding Assistant"

    elif any(word in query for word in ["ppt", "presentation", "powerpoint"]):
        return "PPT Generator"

    elif any(word in query for word in ["pdf", "summary", "summarize", "document"]):
        return "PDF Assistant"

    else:
        return "Chat Assistant"