import fs from 'fs';

async function run() {
  const res = await fetch('http://router.project-osrm.org/route/v1/foot/72.9985,19.0735;72.9982,19.0690;72.9972,19.0645?overview=full&geometries=geojson');
  const data = await res.json();
  const coords = data.routes[0].geometry.coordinates; // [lng, lat]
  
  // convert to [lat, lng]
  const latlngs = coords.map(c => [c[1], c[0]]);
  
  // Let's filter to roughly 15-20 points for smoothness
  const step = Math.max(1, Math.floor(latlngs.length / 15));
  let simplified = latlngs.filter((_, i) => i % step === 0);
  
  // ensure the last few points are explicitly added to define stationHaltSegment
  const finalPoints = latlngs.slice(-4); 
  
  // merge and deduplicate
  const finalSet = [...simplified];
  for (const fp of finalPoints) {
    if (!finalSet.find(p => p[0] === fp[0] && p[1] === fp[1])) {
      finalSet.push(fp);
    }
  }
  
  console.log("Full Custom Route:");
  console.log(JSON.stringify(finalSet));
  
  console.log("\nStation Halt Segment (last 4 points):");
  console.log(JSON.stringify(finalPoints));
}
run();
