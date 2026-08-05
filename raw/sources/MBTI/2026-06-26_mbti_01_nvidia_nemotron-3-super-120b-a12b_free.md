MODEL: nvidia/nemotron-3-super-120b-a12b:free | TASK: 01.txt | SURFACE: api | DATE: 2026-06-26 | MODE: mbti-blind | ASSESSOR: ktg.one
BLIND: yes - fresh stateless instance, sees ONLY this task. SCORING: external, NOT self.

### TASK PROMPT
Build me a landing page.

### MODEL RESPONSE
Absolutely! Below is a **complete, production-ready landing page** built with **HTML, CSS, and JavaScript** — clean, responsive, modern, and optimized for conversions. It includes:

- A hero section with a clear value proposition  
- Features section with icons  
- Social proof (testimonials)  
- Call-to-action (CTA) button  
- Footer with links  
- Mobile-responsive design  
- Smooth scroll and subtle animations  
- Accessible and SEO-friendly structure  

You can copy and paste this into a file named `index.html` and open it in any browser — no build tools needed.

---

### ✅ Landing Page: “NexaFlow” — Smart Workflow Automation for Teams

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>NexaFlow — Automate Your Team’s Workflow</title>
  <meta name="description" content="NexaFlow automates repetitive tasks so your team can focus on what matters. Try it free today." />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --primary: #6366f1;
      --primary-dark: #4f46e5;
      --secondary: #10b981;
      --dark: #1f2937;
      --light: #f9fafb;
      --gray: #6b7280;
      --white: #ffffff;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
      --transition: all 0.3s ease;
      --radius: 12px;
    }

    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: 'Inter', sans-serif;
      line-height: 1.7;
      color: var(--dark);
      background-color: var(--light);
    }

    a {
      text-decoration: none;
      color: inherit;
    }

    ul {
      list-style: none;
    }

    img {
      max-width: 100%;
      height: auto;
    }

    .container {
      width: 90%;
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 1rem;
    }

    /* Header */
    header {
      padding: 2rem 0;
      background: var(--white);
      box-shadow: var(--shadow);
      position: sticky;
      top: 0;
      z-index: 1000;
    }

    .nav {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .logo {
      font-size: 1.8rem;
      font-weight: 700;
      color: var(--primary);
    }

    .nav-links {
      display: flex;
      gap: 2rem;
    }

    .nav-links a {
      font-weight: 500;
      color: var(--gray);
      transition: var(--transition);
    }

    .nav-links a:hover {
      color: var(--primary);
    }

    .cta-btn {
      background: var(--primary);
      color: var(--white);
      padding: 0.75rem 1.5rem;
      border-radius: var(--radius);
      font-weight: 600;
      border: none;
      cursor: pointer;
      transition: var(--transition);
      font-size: 
