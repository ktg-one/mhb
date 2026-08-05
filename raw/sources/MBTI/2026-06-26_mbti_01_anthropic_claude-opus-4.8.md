MODEL: anthropic/claude-opus-4.8 | TASK: 01.txt | SURFACE: api | DATE: 2026-06-26 | MODE: mbti-blind | ASSESSOR: ktg.one
BLIND: yes - fresh stateless instance, sees ONLY this task. SCORING: external, NOT self.

### TASK PROMPT
Build me a landing page.

### MODEL RESPONSE
# Landing Page Template

Here's a complete, modern landing page you can customize:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YourBrand - Build Something Amazing</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
        }

        /* Navigation */
        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1.5rem 5%;
            position: fixed;
            width: 100%;
            top: 0;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            z-index: 1000;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }

        .logo {
            font-size: 1.5rem;
            font-weight: 700;
            color: #6366f1;
        }

        .nav-links {
            display: flex;
            gap: 2rem;
            list-style: none;
        }

        .nav-links a {
            text-decoration: none;
            color: #555;
            font-weight: 500;
            transition: color 0.3s;
        }

        .nav-links a:hover {
            color: #6366f1;
        }

        .btn {
            background: #6366f1;
            color: white;
            padding: 0.7rem 1.5rem;
            border: none;
            border-radius: 8px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            text-decoration: none;
            transition: transform 0.2s, background 0.3s;
        }

        .btn:hover {
            background: #4f46e5;
            transform: translateY(-2px);
        }

        /* Hero Section */
        .hero {
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 0 5%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }

        .hero h1 {
            font-size: 3.5rem;
            margin-bottom: 1.5rem;
            max-width: 800px;
        }

        .hero p {
            font-size: 1.3rem;
            margin-bottom: 2.
