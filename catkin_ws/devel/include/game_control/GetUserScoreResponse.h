// Generated by gencpp from file game_control/GetUserScoreResponse.msg
// DO NOT EDIT!


#ifndef GAME_CONTROL_MESSAGE_GETUSERSCORERESPONSE_H
#define GAME_CONTROL_MESSAGE_GETUSERSCORERESPONSE_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace game_control
{
template <class ContainerAllocator>
struct GetUserScoreResponse_
{
  typedef GetUserScoreResponse_<ContainerAllocator> Type;

  GetUserScoreResponse_()
    : score_percentage(0.0)  {
    }
  GetUserScoreResponse_(const ContainerAllocator& _alloc)
    : score_percentage(0.0)  {
  (void)_alloc;
    }



   typedef double _score_percentage_type;
  _score_percentage_type score_percentage;





  typedef boost::shared_ptr< ::game_control::GetUserScoreResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::game_control::GetUserScoreResponse_<ContainerAllocator> const> ConstPtr;

}; // struct GetUserScoreResponse_

typedef ::game_control::GetUserScoreResponse_<std::allocator<void> > GetUserScoreResponse;

typedef boost::shared_ptr< ::game_control::GetUserScoreResponse > GetUserScoreResponsePtr;
typedef boost::shared_ptr< ::game_control::GetUserScoreResponse const> GetUserScoreResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::game_control::GetUserScoreResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::game_control::GetUserScoreResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::game_control::GetUserScoreResponse_<ContainerAllocator1> & lhs, const ::game_control::GetUserScoreResponse_<ContainerAllocator2> & rhs)
{
  return lhs.score_percentage == rhs.score_percentage;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::game_control::GetUserScoreResponse_<ContainerAllocator1> & lhs, const ::game_control::GetUserScoreResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace game_control

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::game_control::GetUserScoreResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::game_control::GetUserScoreResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::game_control::GetUserScoreResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::game_control::GetUserScoreResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::game_control::GetUserScoreResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::game_control::GetUserScoreResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::game_control::GetUserScoreResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "c1a32e2a12011e18190e52b4e74c1757";
  }

  static const char* value(const ::game_control::GetUserScoreResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xc1a32e2a12011e18ULL;
  static const uint64_t static_value2 = 0x190e52b4e74c1757ULL;
};

template<class ContainerAllocator>
struct DataType< ::game_control::GetUserScoreResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "game_control/GetUserScoreResponse";
  }

  static const char* value(const ::game_control::GetUserScoreResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::game_control::GetUserScoreResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 score_percentage\n"
"\n"
;
  }

  static const char* value(const ::game_control::GetUserScoreResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::game_control::GetUserScoreResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.score_percentage);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct GetUserScoreResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::game_control::GetUserScoreResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::game_control::GetUserScoreResponse_<ContainerAllocator>& v)
  {
    s << indent << "score_percentage: ";
    Printer<double>::stream(s, indent + "  ", v.score_percentage);
  }
};

} // namespace message_operations
} // namespace ros

#endif // GAME_CONTROL_MESSAGE_GETUSERSCORERESPONSE_H
