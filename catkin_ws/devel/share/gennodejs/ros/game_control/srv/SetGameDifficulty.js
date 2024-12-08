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

class SetGameDifficultyRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.difficulty = null;
    }
    else {
      if (initObj.hasOwnProperty('difficulty')) {
        this.difficulty = initObj.difficulty
      }
      else {
        this.difficulty = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SetGameDifficultyRequest
    // Serialize message field [difficulty]
    bufferOffset = _serializer.string(obj.difficulty, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SetGameDifficultyRequest
    let len;
    let data = new SetGameDifficultyRequest(null);
    // Deserialize message field [difficulty]
    data.difficulty = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.difficulty);
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'game_control/SetGameDifficultyRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '46679fd82859481ca1fcc690066de35b';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string difficulty
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SetGameDifficultyRequest(null);
    if (msg.difficulty !== undefined) {
      resolved.difficulty = msg.difficulty;
    }
    else {
      resolved.difficulty = ''
    }

    return resolved;
    }
};

class SetGameDifficultyResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.success = null;
    }
    else {
      if (initObj.hasOwnProperty('success')) {
        this.success = initObj.success
      }
      else {
        this.success = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SetGameDifficultyResponse
    // Serialize message field [success]
    bufferOffset = _serializer.bool(obj.success, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SetGameDifficultyResponse
    let len;
    let data = new SetGameDifficultyResponse(null);
    // Deserialize message field [success]
    data.success = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'game_control/SetGameDifficultyResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '358e233cde0c8a8bcfea4ce193f8fc15';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool success
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SetGameDifficultyResponse(null);
    if (msg.success !== undefined) {
      resolved.success = msg.success;
    }
    else {
      resolved.success = false
    }

    return resolved;
    }
};

module.exports = {
  Request: SetGameDifficultyRequest,
  Response: SetGameDifficultyResponse,
  md5sum() { return '790cc17e982cca965724bd72418a57ae'; },
  datatype() { return 'game_control/SetGameDifficulty'; }
};
