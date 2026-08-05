MODEL: qwen/qwen3.7-max | TASK: 01.txt | SURFACE: api | DATE: 2026-06-26 | MODE: mbti-blind | ASSESSOR: ktg.one
BLIND: yes - fresh stateless instance, sees ONLY this task. SCORING: external, NOT self.

### TASK PROMPT
Build me a landing page.

### MODEL RESPONSE
Since you didn't specify a framework (like React or WordPress), I have built a **complete, modern, responsive landing page using HTML, CSS, and a tiny bit of JavaScript.**

This is a "Single File" solution. You can copy the code below, save it as `index.html`, and open it in your browser immediately.

### The Design Features:
*   **Modern Aesthetic:** Clean typography and a gradient hero section.
*   **Responsive:** Looks good on mobile and desktop.
*   **Sections Included:** Navigation, Hero (Call to Action), Features, Testimonials, and Footer.
*   **No Dependencies:** Uses standard Google Fonts and FontAwesome (via CDN) for icons.

### Copy and Paste this code:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modern Landing Page</title>
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <!-- Font Awesome for Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    
    <style>
        /* --- CSS VARIABLES & RESET --- */
        :root {
            --primary: #4F46E5; /* Indigo */
            --primary-dark: #4338ca;
            --secondary: #10B981; /* Emerald */
            --dark: #1F2937;
            --light: #F9FAFB;
            --gray: #6B7280;
            --white: #ffffff;
            --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', sans-serif;
            color: var(--dark);
            line-height: 1.6;
            background-color: var(--white);
        }

        a { text-decoration: none; color: inherit; transition: 0.3s; }
        ul { list-style: none; }

        /* --- UTILITIES --- */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        .btn {
            display: inline-block;
            padding: 12px 32px;
            border-radius: 8px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .btn-primary {
            background-color: var(--primary);
            color: var(--white);
        }

        .btn-primary:hover {
            background-color: var(--primary-dark);
            transform: translateY(-2px);
        }

        .btn-outline {
            border: 2px solid var(--primary);
            color: var(--primary);
            margin-left: 10px;
        }

        .btn-outline:hover {
            background-color: var(--primary);
            color: var(--white);
        }

        /* --- NAVIGATION --- */
        nav {
            padding: 20px 0;
            position: fixed;
            width: 100%;
            top: 0;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            z-index: 
