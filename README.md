# WalkSafe Mumbai 🚶‍♂️💨
**InnovateX Civic Tech Challenge**

WalkSafe is a hyperlocal pedestrian exposure modeling and clean-path routing web application designed for Mumbai. Unlike traditional mapping services that optimize strictly for vehicular speed and distance, WalkSafe prioritizes **pedestrian lung health** by dynamically routing users around localized microclimate hazards such as dust, heavy vehicle engine halts, and open sewage corridors.

---

## 🌟 Key Features

* **Active Exposure Engine**: Dynamically calculates and penalizes micro-segments of a walk based on real-time pedestrian environmental data.
* **Route Trade-Off Analysis**: Instantly compares standard direct arterial paths against optimized "WalkSafe Clean Paths," displaying exposure reduction percentages (e.g., `-42% Dust Exposure`).
* **Precise Hazard Taxonomy**: Categorizes urban obstacles into four distinct microclimate penalties:
  * 🟡 **Dust**: Unpaved shoulders and active construction zones.
  * 🟢 **Bad Odor**: Open storm drains and sewage corridors.
  * 🔴 **Engine Halt**: Heavy bus/auto congestion and traffic signal idling zones (e.g., Vashi Station & Bus Depot corridors).
  * 🟠 **Stagnant Smog**: High-corridor idling pockets.
* **Interactive Map UI**: Features custom-styled Leaflet map overlays with frosted-glass tooltips, glowing status indicators, and hardcoded Light Mode stability.

---

## 🛠️ Tech Stack

* **Framework**: [Astro.js](https://astro.build/) (Static Site Generation with dynamic client-side interactivity)
* **Styling**: [Tailwind CSS](https://tailwindcss.com/)
* **Mapping**: Leaflet.js & OpenStreetMap tiles
* **Deployment**: Cloudflare Pages / Static Hosting

---

## 🚀 Getting Started Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/innovatex-walksafe.git](https://github.com/your-username/innovatex-walksafe.git)
   cd innovatex-walksafe
