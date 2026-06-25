def story_prompt_template(prompt: str, tone: str = "mysterious", length: str = "medium", setting: str = "shrine") -> str:
    return f"Write an evocative story set in a {setting} with a {tone} tone and {length} length. Prompt: {prompt}"
