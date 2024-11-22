// Generated by gencpp from file game_control/user_msg.msg
// DO NOT EDIT!


#ifndef GAME_CONTROL_MESSAGE_USER_MSG_H
#define GAME_CONTROL_MESSAGE_USER_MSG_H


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
struct user_msg_
{
  typedef user_msg_<ContainerAllocator> Type;

  user_msg_()
    : name()
    , username()
    , age(0)  {
    }
  user_msg_(const ContainerAllocator& _alloc)
    : name(_alloc)
    , username(_alloc)
    , age(0)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _name_type;
  _name_type name;

   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _username_type;
  _username_type username;

   typedef int64_t _age_type;
  _age_type age;





  typedef boost::shared_ptr< ::game_control::user_msg_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::game_control::user_msg_<ContainerAllocator> const> ConstPtr;

}; // struct user_msg_

typedef ::game_control::user_msg_<std::allocator<void> > user_msg;

typedef boost::shared_ptr< ::game_control::user_msg > user_msgPtr;
typedef boost::shared_ptr< ::game_control::user_msg const> user_msgConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::game_control::user_msg_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::game_control::user_msg_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::game_control::user_msg_<ContainerAllocator1> & lhs, const ::game_control::user_msg_<ContainerAllocator2> & rhs)
{
  return lhs.name == rhs.name &&
    lhs.username == rhs.username &&
    lhs.age == rhs.age;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::game_control::user_msg_<ContainerAllocator1> & lhs, const ::game_control::user_msg_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace game_control

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::game_control::user_msg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::game_control::user_msg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::game_control::user_msg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::game_control::user_msg_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::game_control::user_msg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::game_control::user_msg_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::game_control::user_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "76ad7cc8793d3811f3fd0e458252b5c3";
  }

  static const char* value(const ::game_control::user_msg_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x76ad7cc8793d3811ULL;
  static const uint64_t static_value2 = 0xf3fd0e458252b5c3ULL;
};

template<class ContainerAllocator>
struct DataType< ::game_control::user_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "game_control/user_msg";
  }

  static const char* value(const ::game_control::user_msg_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::game_control::user_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string name\n"
"string username\n"
"int64 age\n"
;
  }

  static const char* value(const ::game_control::user_msg_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::game_control::user_msg_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.name);
      stream.next(m.username);
      stream.next(m.age);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct user_msg_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::game_control::user_msg_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::game_control::user_msg_<ContainerAllocator>& v)
  {
    s << indent << "name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.name);
    s << indent << "username: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.username);
    s << indent << "age: ";
    Printer<int64_t>::stream(s, indent + "  ", v.age);
  }
};

} // namespace message_operations
} // namespace ros

#endif // GAME_CONTROL_MESSAGE_USER_MSG_H
