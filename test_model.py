import json

with open("metrics.json") as f:
    metrics = json.load(f)

rmse = metrics["rmse"]
r2 = metrics["r2"]

# Điều kiện test
assert rmse < 1.0, "RMSE too high"
assert r2 > 0.7, "R2 too low"

print("Model test passed")