; Auto-generated. Do not edit!


(cl:in-package game_control-srv)


;//! \htmlinclude GetUserScore-request.msg.html

(cl:defclass <GetUserScore-request> (roslisp-msg-protocol:ros-message)
  ((user_name
    :reader user_name
    :initarg :user_name
    :type cl:string
    :initform ""))
)

(cl:defclass GetUserScore-request (<GetUserScore-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GetUserScore-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GetUserScore-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name game_control-srv:<GetUserScore-request> is deprecated: use game_control-srv:GetUserScore-request instead.")))

(cl:ensure-generic-function 'user_name-val :lambda-list '(m))
(cl:defmethod user_name-val ((m <GetUserScore-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader game_control-srv:user_name-val is deprecated.  Use game_control-srv:user_name instead.")
  (user_name m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GetUserScore-request>) ostream)
  "Serializes a message object of type '<GetUserScore-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'user_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'user_name))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GetUserScore-request>) istream)
  "Deserializes a message object of type '<GetUserScore-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'user_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'user_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GetUserScore-request>)))
  "Returns string type for a service object of type '<GetUserScore-request>"
  "game_control/GetUserScoreRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GetUserScore-request)))
  "Returns string type for a service object of type 'GetUserScore-request"
  "game_control/GetUserScoreRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GetUserScore-request>)))
  "Returns md5sum for a message object of type '<GetUserScore-request>"
  "6dbf2818ed2a67e5ff5a9a7493308436")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GetUserScore-request)))
  "Returns md5sum for a message object of type 'GetUserScore-request"
  "6dbf2818ed2a67e5ff5a9a7493308436")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GetUserScore-request>)))
  "Returns full string definition for message of type '<GetUserScore-request>"
  (cl:format cl:nil "string user_name~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GetUserScore-request)))
  "Returns full string definition for message of type 'GetUserScore-request"
  (cl:format cl:nil "string user_name~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GetUserScore-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'user_name))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GetUserScore-request>))
  "Converts a ROS message object to a list"
  (cl:list 'GetUserScore-request
    (cl:cons ':user_name (user_name msg))
))
;//! \htmlinclude GetUserScore-response.msg.html

(cl:defclass <GetUserScore-response> (roslisp-msg-protocol:ros-message)
  ((score
    :reader score
    :initarg :score
    :type cl:integer
    :initform 0))
)

(cl:defclass GetUserScore-response (<GetUserScore-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GetUserScore-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GetUserScore-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name game_control-srv:<GetUserScore-response> is deprecated: use game_control-srv:GetUserScore-response instead.")))

(cl:ensure-generic-function 'score-val :lambda-list '(m))
(cl:defmethod score-val ((m <GetUserScore-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader game_control-srv:score-val is deprecated.  Use game_control-srv:score instead.")
  (score m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GetUserScore-response>) ostream)
  "Serializes a message object of type '<GetUserScore-response>"
  (cl:let* ((signed (cl:slot-value msg 'score)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GetUserScore-response>) istream)
  "Deserializes a message object of type '<GetUserScore-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'score) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GetUserScore-response>)))
  "Returns string type for a service object of type '<GetUserScore-response>"
  "game_control/GetUserScoreResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GetUserScore-response)))
  "Returns string type for a service object of type 'GetUserScore-response"
  "game_control/GetUserScoreResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GetUserScore-response>)))
  "Returns md5sum for a message object of type '<GetUserScore-response>"
  "6dbf2818ed2a67e5ff5a9a7493308436")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GetUserScore-response)))
  "Returns md5sum for a message object of type 'GetUserScore-response"
  "6dbf2818ed2a67e5ff5a9a7493308436")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GetUserScore-response>)))
  "Returns full string definition for message of type '<GetUserScore-response>"
  (cl:format cl:nil "int64 score~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GetUserScore-response)))
  "Returns full string definition for message of type 'GetUserScore-response"
  (cl:format cl:nil "int64 score~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GetUserScore-response>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GetUserScore-response>))
  "Converts a ROS message object to a list"
  (cl:list 'GetUserScore-response
    (cl:cons ':score (score msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'GetUserScore)))
  'GetUserScore-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'GetUserScore)))
  'GetUserScore-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GetUserScore)))
  "Returns string type for a service object of type '<GetUserScore>"
  "game_control/GetUserScore")