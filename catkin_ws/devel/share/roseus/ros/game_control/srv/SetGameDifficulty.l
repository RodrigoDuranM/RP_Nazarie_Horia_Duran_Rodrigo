;; Auto-generated. Do not edit!


(when (boundp 'game_control::SetGameDifficulty)
  (if (not (find-package "GAME_CONTROL"))
    (make-package "GAME_CONTROL"))
  (shadow 'SetGameDifficulty (find-package "GAME_CONTROL")))
(unless (find-package "GAME_CONTROL::SETGAMEDIFFICULTY")
  (make-package "GAME_CONTROL::SETGAMEDIFFICULTY"))
(unless (find-package "GAME_CONTROL::SETGAMEDIFFICULTYREQUEST")
  (make-package "GAME_CONTROL::SETGAMEDIFFICULTYREQUEST"))
(unless (find-package "GAME_CONTROL::SETGAMEDIFFICULTYRESPONSE")
  (make-package "GAME_CONTROL::SETGAMEDIFFICULTYRESPONSE"))

(in-package "ROS")





(defclass game_control::SetGameDifficultyRequest
  :super ros::object
  :slots (_difficulty ))

(defmethod game_control::SetGameDifficultyRequest
  (:init
   (&key
    ((:difficulty __difficulty) "")
    )
   (send-super :init)
   (setq _difficulty (string __difficulty))
   self)
  (:difficulty
   (&optional __difficulty)
   (if __difficulty (setq _difficulty __difficulty)) _difficulty)
  (:serialization-length
   ()
   (+
    ;; string _difficulty
    4 (length _difficulty)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _difficulty
       (write-long (length _difficulty) s) (princ _difficulty s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _difficulty
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _difficulty (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass game_control::SetGameDifficultyResponse
  :super ros::object
  :slots (_success ))

(defmethod game_control::SetGameDifficultyResponse
  (:init
   (&key
    ((:success __success) nil)
    )
   (send-super :init)
   (setq _success __success)
   self)
  (:success
   (&optional (__success :null))
   (if (not (eq __success :null)) (setq _success __success)) _success)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass game_control::SetGameDifficulty
  :super ros::object
  :slots ())

(setf (get game_control::SetGameDifficulty :md5sum-) "790cc17e982cca965724bd72418a57ae")
(setf (get game_control::SetGameDifficulty :datatype-) "game_control/SetGameDifficulty")
(setf (get game_control::SetGameDifficulty :request) game_control::SetGameDifficultyRequest)
(setf (get game_control::SetGameDifficulty :response) game_control::SetGameDifficultyResponse)

(defmethod game_control::SetGameDifficultyRequest
  (:response () (instance game_control::SetGameDifficultyResponse :init)))

(setf (get game_control::SetGameDifficultyRequest :md5sum-) "790cc17e982cca965724bd72418a57ae")
(setf (get game_control::SetGameDifficultyRequest :datatype-) "game_control/SetGameDifficultyRequest")
(setf (get game_control::SetGameDifficultyRequest :definition-)
      "string difficulty
---
bool success

")

(setf (get game_control::SetGameDifficultyResponse :md5sum-) "790cc17e982cca965724bd72418a57ae")
(setf (get game_control::SetGameDifficultyResponse :datatype-) "game_control/SetGameDifficultyResponse")
(setf (get game_control::SetGameDifficultyResponse :definition-)
      "string difficulty
---
bool success

")



(provide :game_control/SetGameDifficulty "790cc17e982cca965724bd72418a57ae")


