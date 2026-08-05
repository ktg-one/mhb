# Scaffold Industry Fit & Figma Customization Strategy (scaff01–03)

## Objective

Determine optimal industry verticals for ktg-scaff01, scaff02, and scaff03 based on their architectural DNA, content slot structure, and interaction patterns. Assess whether Figma components can be used to rebrand each scaffold as a custom site. Deliver actionable recommendations for both decisions.

## Implementation Plan

- [ ] 1. **Classify each scaffold's architectural identity and content slot structure.** Scaff01 (Next 13, App Router, SCSS Modules, GSAP + Locomotive Scroll + Framer Motion) is a single-page portfolio with linear scroll: Preloader → Landing (infinite marquee text) → Description → Projects (hover-reveal modal images) → SlidingImages → Contact. Content is already seeded with "AI Architect & Founder" text and project entries for Good AI, Kismet, LEGIO, KTG Hub. Scaff02 (Next 10, Pages Router, styled-components, Framer Motion, Canvas API) is a creative studio template: Banner (video + canvas erase-to-reveal + "YOUR SOUND" headline) → Content → FeaturedProject → About (services accordion: "Affordable Audio" Perth studio) → Contact → Footer. Has custom cursor, dark/light theme, `React.memo` discipline throughout. Scaff03 (Next 15, Turbopack, React Three Fiber + drei + Three.js, GSAP, Tailwind 4, TypeScript) is a 3D product showcase: full-viewport WebGL scene with three shirt models (GLB files), texture/material swapping, scroll-driven 3D animations, product routes at `/shirts/[slug]`. Package.json literally says "awwwards-adidas."

- [ ] 2. **Map scaff01 to industry verticals based on content slots.** The hero (background image + marquee text + role descriptor), description (word-animated mission statement), projects (4-card list with hover preview), sliding gallery, and contact CTA form a classic portfolio/personal brand funnel. Best-fit verticals: solo AI practitioner or consultant (current skin), freelance creative director, independent developer, photographer, architect. Secondary fits requiring minimal structural change: small design studio (sub-5 people), boutique consultancy, indie game studio, artist portfolio. The structure assumes an individual whose work IS the product and whose conversion goal is direct contact.

- [ ] 3. **Map scaff02 to industry verticals based on content slots.** The video banner with canvas erase interaction, storytelling content block, single featured project spotlight, services accordion, and contact section form a service-business funnel. Best-fit verticals: audio/music studio (current "Affordable Audio" skin), video production house, branding or creative agency, digital agency, architecture or interior design firm. Secondary fits: law firm or financial boutique (the ethos section + categorized services + contact maps well), wellness studio with session-type services, event production company. The services accordion is the structural differentiator — it assumes defined, categorized offerings. The canvas erase + video banner + custom cursor create a tactile/experiential feel that sells creative credibility.

- [ ] 4. **Map scaff03 to industry verticals based on content slots.** The full-viewport 3D scene with product models, material/texture swapping on interaction, and route-based product pages form a premium product showcase funnel. Best-fit verticals: sportswear (current Adidas skin), sneaker brand, watch brand, headphones or premium audio hardware, luxury accessories, automotive accessories, furniture. This scaffold is structurally locked to physical products that can be 3D-modeled — the entire page IS the WebGL scene. It cannot be repurposed for service businesses, SaaS, content sites, or portfolios without gutting the core value proposition (the 3D interaction).

- [ ] 5. **Assess Figma component extraction viability for scaff01.** SCSS Modules mean styles are already component-scoped with clean file boundaries. Extractable Figma components: RoundedButton (text + border-radius + Magnetic hover, found at `src/common/RoundedButton/index.jsx`), ProjectCard (title + index + hover-reveal image modal, found at `src/components/Projects/components/project/index.jsx`), Description block (auto-layout text with word-reveal reference), Contact CTA section, Header/Nav with Curve overlay (open/closed variants), SlidingImages horizontal gallery frame. Style token extraction path: copy SCSS variables directly to Figma variables — 1:1 mapping, trivial. Animation (GSAP timelines, Locomotive Scroll, Framer Motion variants) is code-only and cannot transfer from Figma, but keyframe states can be designed as Figma variants for developer handoff. Verdict: HIGH Figma viability, easiest of the three.

- [ ] 6. **Assess Figma component extraction viability for scaff02.** styled-components couple layout and style in JS files rather than CSS. Extractable components: AppBar (menu states, found at `components/AppBar/AppBar.jsx`), Services Accordion (expand/collapse variants per item, found at `components/Home/About/About.jsx`), Featured Project Card (video thumbnail + info overlay + arrow), Icon set (Arrow, Facebook, Instagram, Logo, Vimeo in `components/Icons/`), SocialMedia bar, Contact section. Cannot extract: Canvas Eraser banner (pure JS canvas interaction, no Figma equivalent — Figma gets the "revealed" state only), StickyCursor (code behavior, skip), theme system (tokens live in JS at `styles/colors.js` and `styles/themes/`, require manual reading and mapping to Figma variables rather than direct CSS extraction). Verdict: MODERATE Figma viability. Components are extractable but the token system requires reverse-engineering from JS rather than lifting from a stylesheet.

- [ ] 7. **Assess Figma component extraction viability for scaff03.** The entire page surface is a Three.js WebGL scene. The only 2D components are: Header (logo SVG mask + MusicStreamLine toggle, found at `components/Header.tsx`) and Footer. All product showcase interaction (model loading via `useGLTF`, material system in `lib/material.ts`, texture system in `lib/textures.ts`, camera rig in `components/Rig.tsx`) is code-only with no 2D equivalent. Color tokens exist in `lib/colors.ts` (three shirt color themes) and are trivially extractable but only affect the 3D scene lighting/wall colors. To use Figma for this scaffold, you would screenshot key render states of the 3D scene and use those as static reference frames — but there are no meaningful 2D components to build a Figma library from. Verdict: NEAR-ZERO Figma viability for the core experience. Header/Footer chrome only.

- [ ] 8. **Produce a prioritized Figma workflow recommendation across all three scaffolds.** Start with scaff01 — build a Figma component library from its SCSS-scoped components (buttons, cards, nav, sections) and extract design tokens directly from SCSS variables. Add scaff02's accordion and featured project patterns as extensions to that library. Manually map scaff02's styled-component theme values (`styles/colors.js`: white #fff, black #000, accent) into the same Figma variable set to create one unified token system across both scaffold families. Ignore scaff03 for Figma entirely — its value is the 3D pipeline, not 2D design system components.

## Verification Criteria

- Each scaffold mapped to at least 3 primary industry verticals with rationale tied to specific content slots and interaction patterns
- Figma viability assessed per-scaffold with specific component names, file paths, and extraction difficulty ratings
- Style token extraction path documented for each scaffold's CSS architecture (SCSS vs styled-components vs Tailwind)
- Clear boundary drawn between what Figma CAN extract (2D components, layout, tokens) and what it CANNOT (GSAP animations, Canvas interactions, Three.js scenes)
- Unified Figma workflow recommendation that prioritizes scaffolds by extraction ROI

## Potential Risks and Mitigations

1. **Scaff02 is pinned to Next 10 / React 17 — ancient dependency chain**
   Mitigation: If scaff02 is selected for production use, budget a migration to App Router + React 18+ before any customization work. Every dependency update will fight the current version pins. Figma extraction can proceed independently since it targets component structure, not runtime.

2. **Scaff03 3D models are Adidas-specific — cannot be reused**
   Mitigation: Replacement requires actual 3D assets in GLB/GLTF format from Blender, Spline, or similar tooling. The React Three Fiber pipeline (model loading, material system, camera rig) is reusable; only the model files and texture maps need replacement. Budget 3D asset creation as a separate workstream from site customization.

3. **Scaff01 content is already seeded with personal brand data**
   Mitigation: The customization path is straightforward — replace text strings in component JSX and swap images in `/public/images/`. But the project data structure in `Projects/index.jsx` (title, src, color array) is hardcoded, not CMS-driven. For multi-client use, consider extracting project data to a JSON file or headless CMS before cloning the scaffold.

4. **No shared component language across scaffolds**
   Mitigation: Do not attempt a unified component library across all three. Each scaffold is its own design system (SCSS modules vs styled-components vs Tailwind + R3F). Build per-scaffold Figma libraries and share only design tokens (colors, typography, spacing) across them via Figma variables.

## Alternative Approaches

1. **Focus on scaff01 only as the Figma-first scaffold:** Lowest effort, highest extraction ROI. Build the complete Figma library from scaff01, use it as the reusable template for portfolio/consultancy sites. Treat scaff02 and scaff03 as code-only templates that get customized directly in code without Figma intermediation.

2. **Migrate scaff02 to Tailwind before Figma extraction:** Eliminates the styled-components token reverse-engineering problem. A Tailwind migration would align scaff02's style system with scaff03's, creating a shared token extraction path for both. Higher upfront cost but produces a more maintainable codebase and cleaner Figma pipeline.

3. **Use scaff04 (already in the repo) instead of scaff02 for the "platform/community" vertical:** Scaff04 already has shadcn/ui + Radix + Tailwind + TypeScript — the most Figma-compatible stack in the entire repo. If the goal is maximum Figma integration, scaff04 should be the second scaffold in the pipeline after scaff01, not scaff02.
