import subprocess

def generate_email(name, company):
    prompt = f"""Generate a professional cold email body for job applications with NO introduction, explanation, or commentary. I need ONLY the email content from greeting to signature.

Use these exact details:
- Name: Vihaan Phal
- Education: Computer Science degree from Arizona State University (3.86 GPA)
- Skills: ReactJS, Node.js, Python, C#, Swift, AWS, AI, full-stack development, distributed systems

The email should:
- Be addressed to {name} at {company}
- Emphasize my problem-solving mindset
- Include a clear call-to-action
- Be concise (max 250 words)

Provide ONLY the email body text, starting with 'Dear {name},' and ending with my signature.
    """
    
    try:
        result = subprocess.run(
            ["ollama", "run", "llama2:13b", prompt],
            capture_output=True,
            text=True,
            timeout=30  
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"Error generating email: {e}")
        return "Error generating email."
