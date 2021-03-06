# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from hello_world/SensorData.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class SensorData(genpy.Message):
  _md5sum = "4a1990867dc4d7d4a1a2518817eae425"
  _type = "hello_world/SensorData"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """string manufacturer_name
int64 distance
string sensor_type
int64 max_range
int64 min_range"""
  __slots__ = ['manufacturer_name','distance','sensor_type','max_range','min_range']
  _slot_types = ['string','int64','string','int64','int64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       manufacturer_name,distance,sensor_type,max_range,min_range

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SensorData, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.manufacturer_name is None:
        self.manufacturer_name = ''
      if self.distance is None:
        self.distance = 0
      if self.sensor_type is None:
        self.sensor_type = ''
      if self.max_range is None:
        self.max_range = 0
      if self.min_range is None:
        self.min_range = 0
    else:
      self.manufacturer_name = ''
      self.distance = 0
      self.sensor_type = ''
      self.max_range = 0
      self.min_range = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.manufacturer_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.distance
      buff.write(_get_struct_q().pack(_x))
      _x = self.sensor_type
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2q().pack(_x.max_range, _x.min_range))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.manufacturer_name = str[start:end].decode('utf-8')
      else:
        self.manufacturer_name = str[start:end]
      start = end
      end += 8
      (self.distance,) = _get_struct_q().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.sensor_type = str[start:end].decode('utf-8')
      else:
        self.sensor_type = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.max_range, _x.min_range,) = _get_struct_2q().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.manufacturer_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.distance
      buff.write(_get_struct_q().pack(_x))
      _x = self.sensor_type
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2q().pack(_x.max_range, _x.min_range))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.manufacturer_name = str[start:end].decode('utf-8')
      else:
        self.manufacturer_name = str[start:end]
      start = end
      end += 8
      (self.distance,) = _get_struct_q().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.sensor_type = str[start:end].decode('utf-8')
      else:
        self.sensor_type = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.max_range, _x.min_range,) = _get_struct_2q().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2q = None
def _get_struct_2q():
    global _struct_2q
    if _struct_2q is None:
        _struct_2q = struct.Struct("<2q")
    return _struct_2q
_struct_q = None
def _get_struct_q():
    global _struct_q
    if _struct_q is None:
        _struct_q = struct.Struct("<q")
    return _struct_q
