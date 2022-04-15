class Vector(tuple):
  def __sub__(self, other):
    return tuple(u - up for (u, up) in zip(self, other))

  def __add__(self, other):
    return tuple(u + up for (u, up) in zip(self, other))


class Matrix(tuple):
    """A simple matrix class based on tuples"""

    def apply(self, vec: Vector):
      return Vector(sum(l * v for l, v in zip(row, vec)) for row in self)

    def multiply(self, mat):
      return Matrix(zip(*tuple(self.apply(column) for column in zip(*mat))))

    def __mul__(self, other):
      if isinstance(other, int):
        return Matrix(
          tuple(element * other for element in row)
          for row in self
        )
      if isinstance(other, Vector):
        return self.apply(other)
      elif isinstance(other, Matrix):
        return self.multiply(other)
      else:
        raise NotImplementedError(f"Cannot multiply object of type {type(self)} with object of type {type(other)}")

    def __pow__(self, exponent: int):
      if not isinstance(exponent, int) or exponent < 0 or exponent > 99:
        raise ValueError("exponent must be an integer in range [0, 100[")
      if exponent == 0:
        return Matrix(((1, 0, 0), (0, 1, 0), (0, 0, 1)))

      m = Matrix(self)
      for k in range(exponent - 1):
          m = m * self
      return m


Tx = Matrix(
  (
    ( 1,  0,  0 ),
    ( 0,  0,  1 ),
    ( 0, -1,  0 )
  )
)


Ty = Matrix(
  (
    ( 0,  0, -1 ),
    ( 0,  1,  0 ),
    ( 1,  0,  0 )
  )
)


Tz = Matrix(
  (
    ( 0,  1,  0 ),
    (-1,  0,  0 ),
    ( 0,  0,  1 ),
  )
)

all_cubic_group_transformations = set()

for k in {0, 1, 2, 3}:
  for l in {0, 1, 2, 3}:
    for m in {0, 1, 2, 3}:
      all_cubic_group_transformations.add((Tx ** k) * (Ty ** l) * (Tz ** m))
print(all_cubic_group_transformations)
assert len(all_cubic_group_transformations) == 24
