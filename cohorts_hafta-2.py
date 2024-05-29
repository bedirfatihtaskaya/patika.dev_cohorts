def euclidean_distance(point1, point2):
  """
  Bu fonksiyon iki nokta arasındaki Öklid mesafesini hesaplar.

  Args:
    point1: (x1, y1) şeklinde bir demet olan ilk nokta.
    point2: (x2, y2) şeklinde bir demet olan ikinci nokta.

  Returns:
    İki nokta arasındaki Öklid mesafesi.
  """
  x1, y1 = point1
  x2, y2 = point2
  return 0.5**((x2 - x1) ** 2 + (y2 - y1) ** 2)

def main():
  # Noktaları tanımlayın
  points = [(1, 1), (4, 5)]

  # Mesafeleri hesaplayın
  distances = []
  for i in range(len(points)):
    for j in range(i + 1, len(points)):
      distance = euclidean_distance(points[i], points[j])
      distances.append(distance)

  # Minimum mesafeyi bulun
  minimum_distance = min(distances)

  # Sonucu yazdırın
  print("Minimum mesafe:", minimum_distance)

main()
