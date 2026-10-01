# WALKSAFE — Design System & Functional Specification

> Identity: Pedestrian-first clean-air navigation engine.
> Design Language: Chalo transit clarity + onscreentimer.com utilitarianism. Zero AI slop, no glow effects, 100% sunlight legibility.

---

## 1. Visual Token Architecture

### Colors (Chalo Transit Palette)
- **Top Brand Bar:** `#059669` (Emerald-600)
- **Base Background:** `#F8FAFC` (Slate-50)
- **Card Surfaces:** `#FFFFFF` (Pure White) with 1px border `border-slate-200`
- **Primary Text:** `#0F172A` (Slate-900 — Maximum contrast)
- **Secondary / Muted Text:** `#64748B` (Slate-500)
- **Clean Route Accent:** `#059669` (Emerald-600) | Light Accent: `#ECFDF5` (Emerald-50)
- **Hazard Alerts:**
  - Active Dust: `#D97706` (Amber-600)
  - Toxic Odor: `#0D9488` (Teal-600)
  - Open Smoke / Burning: `#EA580C` (Orange-600)
  - Transit Idling Halt: `#DC2626` (Red-600)

---

## 2. Page Hierarchy & Dedicated Routes

```text
/ (Home) ─── Splash Loader ──> Clean Hero (Plan Route | Pin Route | Demo)
 │
 ├── /plan           <-- Dedicated "From / To" route entry page
 ├── /pin            <-- Ultra-smooth, zero-lag point-to-point pin drop canvas
 ├── /demo-select    <-- Selection hub for hypothetical nodes (Alpha, Beta, Charlie, Delta)
 ├── /demo           <-- The showcase map (Collapsible Route HUD + 2-Tap Hazard Dropdown)
 │
 └── Settings Pages
      ├── /profile       <-- Commuter identity & walking pace (localStorage)
      ├── /priority      <-- Hazard priority intensity sliders (1 to 4)
      └── /daily-routes  <-- 1-tap bookmarked commutes/plan
```
Build Mission 1 for Walksafe at `src/pages/index.astro`.

Aesthetic Directives:
- Clean, transit-utility aesthetic inspired by Chalo (bg-emerald-600 top brand bar, crisp white cards, slate-900 text, 1px slate-200 borders).
- Fast, static, zero AI slop, no glow effects or heavy blur.

1. Splash Preloader:
   - Centered overlay div with a circular Walksafe icon and bold text: "WalkSafe — Pedestrian Clean-Air Engine".
   - Automatically fades out via a CSS transition (opacity 0, pointer-events-none) after 600ms on client load.

2. Global Header Bar:
   - Wrapped in solid emerald bar (`bg-emerald-600` text-white px-6 py-3.5 flex items-center justify-between shadow-sm).
   - Left: Profile icon link to `/profile` + Brand title "Walksafe" with a subtle pill badge that says simply "Mumbai" (`bg-emerald-700/60 text-emerald-100 text-xs px-2.5 py-0.5 rounded-full font-medium ml-2`).
   - Right: Clean links row:
     - "Demo" (link to `/demo-select`, styled as a crisp white pill button `bg-white text-emerald-800 font-bold px-3 py-1 rounded-xl text-sm shadow-sm hover:bg-emerald-50 transition`).
     - Hamburger icon link to `/menu` (or dropdown trigger to settings pages).

3. Main Hero Stage (Desktop 3-column layout, mobile stacked):
   - Top quote pill banner: "Google Maps shows the shortest road. Walksafe shows the cleanest sidewalk." (Centered, max-w-lg mx-auto mb-6 text-xs font-semibold text-slate-500 bg-white border border-slate-200 py-1.5 px-4 rounded-full text-center).
   - Left Card: Clean card with a cute flat vector illustration placeholder (e.g. people commuting on foot) and text "Exposure-Aware Walking".
   - Center Action Hub:
     - Card container: max-w-md w-full bg-white rounded-3xl border border-slate-200 shadow-md p-6 flex flex-col gap-4 text-center.
     - Title: "Start Your Clean Walk" with subtitle "Avoid unsuppressed dust, stagnant exhaust, and open odor."
     - Action Buttons:
       1. Primary Action: Full-width button "Plan Clean Walk (From - To)" linking to `/plan` (`bg-emerald-600 hover:bg-emerald-700 text-white font-bold py-3.5 px-6 rounded-2xl shadow-sm transition`).
       2. Secondary Row: Two equal buttons:
          - "📍 Pin on Map" linking to `/pin` (`bg-slate-100 hover:bg-slate-200 text-slate-800 font-semibold py-3 px-4 rounded-2xl border border-slate-200 text-sm transition`).
          - "⚡ Showcase Demo" linking to `/demo-select` (`bg-emerald-50 hover:bg-emerald-100 text-emerald-700 font-semibold py-3 px-4 rounded-2xl border border-emerald-200 text-sm transition`).
   - Right Card: Clean card with a flat vector illustration placeholder (e.g. tree canopies & clean city breezes) and text "Hyperlocal Microclimate".

4. Footer:
   - Sits at page bottom: border-t border-slate-200 bg-white py-5 px-6 text-center text-xs text-slate-500 flex flex-col md:flex-row justify-between items-center gap-2 max-w-6xl mx-auto.
   - Text: "Walksafe — Pedestrian-First Air Quality Exposure Engine for InnovateX 2026."
   - Links: "Methodology", "Theme 2: Urban AQI", "GitHub".

Create placeholder pages for `/plan.astro`, `/pin.astro`, `/demo-select.astro`, `/menu.astro`, and `/profile.astro` with simple back buttons so no links produce a 404 error.