import math

class Vector:
    """A two-dimensional vector with Cartesian coordinates."""

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        """Human-readable string representation of the vector."""
        return '{:g}x + {:g}y'.format(self.x, self.y)

    def __repr__(self):
        """Unambiguous string representation of the vector."""
        return '{:g}x + {:g}y'.format(self.x, self.y)

    def dot(self, other):
        """The scalar (dot) product of self and other. Both must be vectors."""

        if not isinstance(other, Vector):
            raise TypeError('Can only take dot product of two Vector objects')
        return self.x * other.x + self.y * other.y
    # Alias the __matmul__ method to dot so we can use a @ b as well as a.dot(b).
    __matmul__ = dot

    def __sub__(self, other):
        """Vector subtraction."""
        return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        """Vector equality"""
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        """Vector greater than"""
        return self.x > other.x or self.y > other.y

    def __lt__(self, other):
        """Vector less than"""
        return self.x < other.x and self.y < other.y


    def __add__(self, other):
        """Vector addition."""
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        """Multiplication of a vector by a scalar."""

        if isinstance(scalar, int) or isinstance(scalar, float):
            return Vector(self.x*scalar, self.y*scalar)
        raise NotImplementedError('Can only multiply Vector by a scalar')

    def __rmul__(self, scalar):
        """Reflected multiplication so vector * scalar also works."""
        return self.__mul__(scalar)

    def __neg__(self):
        """Negation of the vector (invert through origin.)"""
        return Vector(-self.x, -self.y)

    def __truediv__(self, scalar):
        """True division of the vector by a scalar."""
        return Vector(self.x / scalar, self.y / scalar)

    def __mod__(self, scalar):
        """One way to implement modulus operation: for each component."""
        return Vector(self.x % scalar, self.y % scalar)

    def __abs__(self):
        """Absolute value (magnitude) of the vector."""
        return math.sqrt(self.x**2 + self.y**2)

    def distance_to(self, other):
        """The distance between vectors self and other."""
        return abs(self - other)

    def to_polar(self):
        """Return the vector's components in polar coordinates."""
        return self.__abs__(), math.atan2(self.y, self.x)

    def __hash__(self):
        """Return the vector's hash value."""
        return hash((self.y, self.x))
