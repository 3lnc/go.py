from math import hypot

class Vector2d(object):
	def __init__(self, x, y):
		self._x = x
		self._y = y

	def __repr__(self):
		return "Vector2d({}, {})".format(self._x, self._y)

	def __add__(self, other):
		if not isinstance(other, Vector2d):
			return NotImplemented
		return Vector2d(self._x + other._x, self._y + other._y)

	def __eq__(self, other):
		if not isinstance(other, Vector2d):
			return NotImplemented
		return self._x == other._x and self._y == other._y

	def __neg__(self):
		return Vector2d(-self._x, -self._y)

	def __mul__(self, other):
		if not isinstance(other, (int, float)):
			return NotImplemented
		return Vector2d(self._x * other, self._y * other)

	def __rmul__(self, other):
		return self * other

	def __abs__(self):
		return hypot(self._x, self._y)

	@property
	def x(self):
	    return self._x
	
	@property
	def y(self):
	    return self._y
