// Auto-generated. Do not edit!

// (in-package game_control.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class GetUserScoreRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.user_name = null;
    }
    else {
      if (initObj.hasOwnProperty('user_name')) {
        this.user_name = initObj.user_name
      }
      else {
        this.user_name = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type GetUserScoreRequest
    // Serialize message field [user_name]
    bufferOffset = _serializer.string(obj.user_name, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type GetUserScoreRequest
    let len;
    let data = new GetUserScoreRequest(null);
    // Deserialize message field [user_name]
    data.user_name = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.user_name);
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'game_control/GetUserScoreRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '159b36609af19853383ab1313ed185b0';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string user_name
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new GetUserScoreRequest(null);
    if (msg.user_name !== undefined) {
      resolved.user_name = msg.user_name;
    }
    else {
      resolved.user_name = ''
    }

    return resolved;
    }
};

class GetUserScoreResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.score_percentage = null;
    }
    else {
      if (initObj.hasOwnProperty('score_percentage')) {
        this.score_percentage = initObj.score_percentage
      }
      else {
        this.score_percentage = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type GetUserScoreResponse
    // Serialize message field [score_percentage]
    bufferOffset = _serializer.float64(obj.score_percentage, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type GetUserScoreResponse
    let len;
    let data = new GetUserScoreResponse(null);
    // Deserialize message field [score_percentage]
    data.score_percentage = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'game_control/GetUserScoreResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c1a32e2a12011e18190e52b4e74c1757';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 score_percentage
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new GetUserScoreResponse(null);
    if (msg.score_percentage !== undefined) {
      resolved.score_percentage = msg.score_percentage;
    }
    else {
      resolved.score_percentage = 0.0
    }

    return resolved;
    }
};

module.exports = {
  Request: GetUserScoreRequest,
  Response: GetUserScoreResponse,
  md5sum() { return 'e10e2705e269839872c95ff0a89588d4'; },
  datatype() { return 'game_control/GetUserScore'; }
};
