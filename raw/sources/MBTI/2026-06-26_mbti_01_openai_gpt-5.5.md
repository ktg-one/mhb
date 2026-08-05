MODEL: openai/gpt-5.5 | TASK: 01.txt | SURFACE: api | DATE: 2026-06-26 | MODE: mbti-blind | ASSESSOR: ktg.one
BLIND: yes - fresh stateless instance, sees ONLY this task. SCORING: external, NOT self.

### TASK PROMPT
Build me a landing page.

### MODEL RESPONSE
Sure — here’s a clean, modern landing page you can use as a starting point. It’s a single-file HTML page with responsive styling included.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Launch Your Product Faster</title>
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: Inter, Arial, sans-serif;
      color: #111827;
      background: #ffffff;
      line-height: 1.6;
    }

    a {
      text-decoration: none;
      color: inherit;
    }

    .container {
      width: min(1120px, 92%);
      margin: 0 auto;
    }

    header {
      padding: 24px 0;
      border-bottom: 1px solid #e5e7eb;
      background: #ffffff;
    }

    .nav {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .logo {
      font-size: 1.4rem;
      font-weight: 800;
      color: #2563eb;
    }

    .nav-links {
      display: flex;
      gap: 28px;
      align-items: center;
      font-size: 0.95rem;
      color: #374151;
    }

    .nav-links a:hover {
      color: #2563eb;
    }

    .btn {
      display: inline-block;
      padding: 12px 20px;
      border-radius: 10px;
      font-weight: 700;
      transition: 0.2s ease;
    }

    .btn-primary {
      background: #2563eb;
      color: #ffffff;
    }

    .btn-primary:hover {
      background: #1d4ed8;
      transform: translateY(-1px);
    }

    .btn-secondary {
      background: #eff6ff;
      color: #2563eb;
    }

    .hero {
      padding: 96px 0;
      background:
        radial-gradient(circle at top right, #dbeafe 0, transparent 35%),
        linear-gradient(180deg, #ffffff 0%, #f9fafb 100%);
    }

    .hero-grid {
      display: grid;
      grid-template-columns: 1.1fr 0.9fr;
      gap: 56px;
      align-items: center;
    }

    .badge {
      display: inline-block;
      margin-bottom: 18px;
      padding: 6px 12px;
      border-radius: 999px;
      background: #dbeafe;
      color: #1d4ed8;
      font-weight: 700;
      font-size: 0.85rem;
    }

    h1 {
      font-size: clamp(2.5rem, 6vw, 4.8rem);
      line-height: 1.05;
      letter-spacing: -0.05em;
      margin-bottom: 24px;
    }

    .hero p {
      font-size: 1.15rem;
      color: #4b5563;
      max-width: 620px;
      margin-bottom: 32px;
    }

    .hero-actions {
      display: flex;
      gap: 16px;
      flex-wrap: wrap;
      align-items: center;
    }

    .hero-card {
      background: #ffffff;
      border: 1px solid #e5e7eb;
      border-radius: 24px;
      padding: 28px;
      box-shadow: 0 24px 60px rgba(15, 23, 42, 0.12);
    }

    .dashboard {
      border-radius: 18px;
      background: #111827;
      color: white;
      padding: 22px;
    }

    .dashboard-top {
      display: flex;
      gap: 8px;
      margin-bottom: 24px;
    }

    .dot {
      width: 10
