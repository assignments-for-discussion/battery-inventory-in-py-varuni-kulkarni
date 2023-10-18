
def count_batteries_by_health(present_capacities):
  counts = {
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }

  for present_capacity in present_capacities:
    SoH = 100 * present_capacity/120
  #classification of the ranges
    if SoH <= 100 and SoH > 80:
      counts["healthy"] += 1
    elif 63 <= SoH <= 80:
      counts["exchange"] += 1
    else:
      counts["failed"] += 1
    
  return counts

def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
