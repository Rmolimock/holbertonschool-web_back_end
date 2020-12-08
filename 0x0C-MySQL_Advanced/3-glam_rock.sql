-- glam rock

SELECT band_name, COALESCE(split, 2020) FROM metal_bands
WHERE style like '%Glam rock%' ORDER BY lifespan DESC;
