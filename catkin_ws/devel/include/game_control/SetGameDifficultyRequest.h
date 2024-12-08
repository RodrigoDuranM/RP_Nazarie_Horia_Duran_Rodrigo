// Generated by gencpp from file game_control/SetGameDifficultyRequest.msg
// DO NOT EDIT!


#ifndef GAME_CONTROL_MESSAGE_SETGAMEDIFFICULTYREQUEST_H
#define GAME_CONTROL_MESSAGE_SETGAMEDIFFICULTYREQUEST_H


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
struct SetGameDifficultyRequest_
{
  typedef SetGameDifficultyRequest_<ContainerAllocator> Type;

  SetGameDifficultyRequest_()
    : difficulty()  {
    }
  SetGameDifficultyRequest_(const ContainerAllocator& _alloc)
    : difficulty(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _difficulty_type;
  _difficulty_type difficulty;





  typedef boost::shared_ptr< ::game_control::SetGameDifficultyRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::game_control::SetGameDifficultyRequest_<ContainerAllocator> const> ConstPtr;

}; // struct SetGameDifficultyRequest_

typedef ::game_control::SetGameDifficultyRequest_<std::allocator<void> > SetGameDifficultyRequest;

typedef boost::shared_ptr< ::game_control::SetGameDifficultyRequest > SetGameDifficultyRequestPtr;
typedef boost::shared_ptr< ::game_control::SetGameDifficultyRequest const> SetGameDifficultyRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::game_control::SetGameDifficultyRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::game_control::SetGameDifficultyRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::game_control::SetGameDifficultyRequest_<ContainerAllocator1> & lhs, const ::game_control::SetGameDifficultyRequest_<ContainerAllocator2> & rhs)
{
  return lhs.difficulty == rhs.difficulty;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::game_control::SetGameDifficultyRequest_<ContainerAllocator1> & lhs, const ::game_control::SetGameDifficultyRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace game_control

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::game_control::SetGameDifficultyRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::game_control::SetGameDifficultyRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::game_control::SetGameDifficultyRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::game_control::SetGameDifficultyRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::game_control::SetGameDifficultyRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::game_control::SetGameDifficultyRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::game_control::SetGameDifficultyRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "46679fd82859481ca1fcc690066de35b";
  }

  static const char* value(const ::game_control::SetGameDifficultyRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x46679fd82859481cULL;
  static const uint64_t static_value2 = 0xa1fcc690066de35bULL;
};

template<class ContainerAllocator>
struct DataType< ::game_control::SetGameDifficultyRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "game_control/SetGameDifficultyRequest";
  }

  static const char* value(const ::game_control::SetGameDifficultyRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::game_control::SetGameDifficultyRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string difficulty\n"
;
  }

  static const char* value(const ::game_control::SetGameDifficultyRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::game_control::SetGameDifficultyRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.difficulty);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SetGameDifficultyRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::game_control::SetGameDifficultyRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::game_control::SetGameDifficultyRequest_<ContainerAllocator>& v)
  {
    s << indent << "difficulty: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.difficulty);
  }
};

} // namespace message_operations
} // namespace ros

#endif // GAME_CONTROL_MESSAGE_SETGAMEDIFFICULTYREQUEST_H
