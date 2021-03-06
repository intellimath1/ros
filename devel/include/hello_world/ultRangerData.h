// Generated by gencpp from file hello_world/ultRangerData.msg
// DO NOT EDIT!


#ifndef HELLO_WORLD_MESSAGE_ULTRANGERDATA_H
#define HELLO_WORLD_MESSAGE_ULTRANGERDATA_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace hello_world
{
template <class ContainerAllocator>
struct ultRangerData_
{
  typedef ultRangerData_<ContainerAllocator> Type;

  ultRangerData_()
    : distance(0.0)
    , ECHO(0)
    , TRIG(0)  {
    }
  ultRangerData_(const ContainerAllocator& _alloc)
    : distance(0.0)
    , ECHO(0)
    , TRIG(0)  {
  (void)_alloc;
    }



   typedef double _distance_type;
  _distance_type distance;

   typedef int64_t _ECHO_type;
  _ECHO_type ECHO;

   typedef int64_t _TRIG_type;
  _TRIG_type TRIG;





  typedef boost::shared_ptr< ::hello_world::ultRangerData_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::hello_world::ultRangerData_<ContainerAllocator> const> ConstPtr;

}; // struct ultRangerData_

typedef ::hello_world::ultRangerData_<std::allocator<void> > ultRangerData;

typedef boost::shared_ptr< ::hello_world::ultRangerData > ultRangerDataPtr;
typedef boost::shared_ptr< ::hello_world::ultRangerData const> ultRangerDataConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::hello_world::ultRangerData_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::hello_world::ultRangerData_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::hello_world::ultRangerData_<ContainerAllocator1> & lhs, const ::hello_world::ultRangerData_<ContainerAllocator2> & rhs)
{
  return lhs.distance == rhs.distance &&
    lhs.ECHO == rhs.ECHO &&
    lhs.TRIG == rhs.TRIG;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::hello_world::ultRangerData_<ContainerAllocator1> & lhs, const ::hello_world::ultRangerData_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace hello_world

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::hello_world::ultRangerData_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::hello_world::ultRangerData_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::hello_world::ultRangerData_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::hello_world::ultRangerData_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::hello_world::ultRangerData_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::hello_world::ultRangerData_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::hello_world::ultRangerData_<ContainerAllocator> >
{
  static const char* value()
  {
    return "977bed47f562a4bff3f01c6a45d8dc10";
  }

  static const char* value(const ::hello_world::ultRangerData_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x977bed47f562a4bfULL;
  static const uint64_t static_value2 = 0xf3f01c6a45d8dc10ULL;
};

template<class ContainerAllocator>
struct DataType< ::hello_world::ultRangerData_<ContainerAllocator> >
{
  static const char* value()
  {
    return "hello_world/ultRangerData";
  }

  static const char* value(const ::hello_world::ultRangerData_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::hello_world::ultRangerData_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 distance\n"
"int64 ECHO\n"
"int64 TRIG\n"
;
  }

  static const char* value(const ::hello_world::ultRangerData_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::hello_world::ultRangerData_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.distance);
      stream.next(m.ECHO);
      stream.next(m.TRIG);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ultRangerData_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::hello_world::ultRangerData_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::hello_world::ultRangerData_<ContainerAllocator>& v)
  {
    s << indent << "distance: ";
    Printer<double>::stream(s, indent + "  ", v.distance);
    s << indent << "ECHO: ";
    Printer<int64_t>::stream(s, indent + "  ", v.ECHO);
    s << indent << "TRIG: ";
    Printer<int64_t>::stream(s, indent + "  ", v.TRIG);
  }
};

} // namespace message_operations
} // namespace ros

#endif // HELLO_WORLD_MESSAGE_ULTRANGERDATA_H
