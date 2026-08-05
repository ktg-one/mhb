MODEL: deepseek/deepseek-v4-pro | TASK: 01.txt | SURFACE: api | DATE: 2026-06-26 | MODE: mbti-blind | ASSESSOR: ktg.one
BLIND: yes - fresh stateless instance, sees ONLY this task. SCORING: external, NOT self.

### TASK PROMPT
Build me a landing page.

### MODEL RESPONSE
This is a complete HTML landing page for a fictional SaaS product called "FlowSpark." You can run it directly in your browser.
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>FlowSpark | Automate your workflow</title>
  <!-- Font Awesome 6 (free CDN) -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
      background: linear-gradient(145deg, #f9fafc 0%, #ffffff 100%);
      color: #1a1e2b;
      line-height: 1.5;
      scroll-behavior: smooth;
    }

    .container {
      max-width: 1300px;
      margin: 0 auto;
      padding: 0 2rem;
    }

    /* Header & Navigation */
    header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 1.5rem 0;
      flex-wrap: wrap;
      gap: 1.5rem;
    }

    .logo {
      font-size: 1.8rem;
      font-weight: 700;
      letter-spacing: -0.5px;
      background: linear-gradient(135deg, #2563eb, #7c3aed);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .logo i {
      background: none;
      -webkit-text-fill-color: #2563eb;
      font-size: 2rem;
    }

    .nav-links {
      display: flex;
      gap: 2.5rem;
      align-items: center;
      flex-wrap: wrap;
    }

    .nav-links a {
      text-decoration: none;
      color: #334155;
      font-weight: 500;
      transition: color 0.2s ease;
      font-size: 1rem;
    }

    .nav-links a:hover {
      color: #2563eb;
    }

    .btn {
      padding: 0.7rem 1.8rem;
      border-radius: 40px;
      font-weight: 600;
      font-size: 0.95rem;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      transition: all 0.25s ease;
      border: none;
      cursor: pointer;
      background: white;
      color: #1e293b;
      box-shadow: 0 4px 12px rgba(0,0,0,0.04);
      border: 1px solid #e2e8f0;
    }

    .btn-primary {
      background: #2563eb;
      color: white;
      border: 1px solid #2563eb;
      box-shadow: 0 8px 20px rgba(37,99,235,0.25);
    }

    .btn-primary:hover {
      background: #1d4ed8;
      transform: translateY(-2px);
      box-shadow: 0 12px 24px rgba(37,99,235,0.3);
    }

    .btn-outline:hover {
      background: #f1f5f9;
      border-color: #cbd5e1;
      transform: translateY(-1px);
    }

    /* Hero Section */
    .hero {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 3rem;
     
