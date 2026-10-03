const https = require('https');

https.get('https://overpass-api.de/api/interpreter?data=[out:json];way(around:500,19.0690,72.9980)["name"~"Swami Pranavanandji"];out geom;', (res) => {
  let data = '';
  res.on('data', (chunk) => data += chunk);
  res.on('end', () => {
    try {
      const parsed = JSON.parse(data);
      console.log(JSON.stringify(parsed.elements, null, 2));
    } catch(e) { console.error(e); }
  });
});
