import matplotlib.pyplot as plt
import numpy as np

def main():
  x = np.linspace(0, 10 * np.pi, 200)
  y1 = np.sin(x)
  y2 = np.cos(x)
  y3 = np.arctan2(y1, y2)

  fig, (ax) = plt.subplots()
  ax.plot(x, y1)
  ax.plot(x, y2)
  ax.plot(x, y3)
  plt.show()



if __name__ == '__main__':
  main()
