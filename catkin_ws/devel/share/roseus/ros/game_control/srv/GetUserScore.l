;; Auto-generated. Do not edit!


(when (boundp 'game_control::GetUserScore)
  (if (not (find-package "GAME_CONTROL"))
    (make-package "GAME_CONTROL"))
  (shadow 'GetUserScore (find-package "GAME_CONTROL")))
(unless (find-package "GAME_CONTROL::GETUSERSCORE")
  (make-package "GAME_CONTROL::GETUSERSCORE"))
(unless (find-package "GAME_CONTROL::GETUSERSCOREREQUEST")
  (make-package "GAME_CONTROL::GETUSERSCOREREQUEST"))
(unless (find-package "GAME_CONTROL::GETUSERSCORERESPONSE")
  (make-package "GAME_CONTROL::GETUSERSCORERESPONSE"))

(in-package "ROS")





(defclass game_control::GetUserScoreRequest
  :super ros::object
  :slots (_user_name ))

(defmethod game_control::GetUserScoreRequest
  (:init
   (&key
    ((:user_name __user_name) "")
    )
   (send-super :init)
   (setq _user_name (string __user_name))
   self)
  (:user_name
   (&optional __user_name)
   (if __user_name (setq _user_name __user_name)) _user_name)
  (:serialization-length
   ()
   (+
    ;; string _user_name
    4 (length _user_name)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _user_name
       (write-long (length _user_name) s) (princ _user_name s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _user_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _user_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass game_control::GetUserScoreResponse
  :super ros::object
  :slots (_score_percentage ))

(defmethod game_control::GetUserScoreResponse
  (:init
   (&key
    ((:score_percentage __score_percentage) 0.0)
    )
   (send-super :init)
   (setq _score_percentage (float __score_percentage))
   self)
  (:score_percentage
   (&optional __score_percentage)
   (if __score_percentage (setq _score_percentage __score_percentage)) _score_percentage)
  (:serialization-length
   ()
   (+
    ;; float64 _score_percentage
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _score_percentage
       (sys::poke _score_percentage (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _score_percentage
     (setq _score_percentage (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass game_control::GetUserScore
  :super ros::object
  :slots ())

(setf (get game_control::GetUserScore :md5sum-) "e10e2705e269839872c95ff0a89588d4")
(setf (get game_control::GetUserScore :datatype-) "game_control/GetUserScore")
(setf (get game_control::GetUserScore :request) game_control::GetUserScoreRequest)
(setf (get game_control::GetUserScore :response) game_control::GetUserScoreResponse)

(defmethod game_control::GetUserScoreRequest
  (:response () (instance game_control::GetUserScoreResponse :init)))

(setf (get game_control::GetUserScoreRequest :md5sum-) "e10e2705e269839872c95ff0a89588d4")
(setf (get game_control::GetUserScoreRequest :datatype-) "game_control/GetUserScoreRequest")
(setf (get game_control::GetUserScoreRequest :definition-)
      "string user_name
---
float64 score_percentage

")

(setf (get game_control::GetUserScoreResponse :md5sum-) "e10e2705e269839872c95ff0a89588d4")
(setf (get game_control::GetUserScoreResponse :datatype-) "game_control/GetUserScoreResponse")
(setf (get game_control::GetUserScoreResponse :definition-)
      "string user_name
---
float64 score_percentage

")



(provide :game_control/GetUserScore "e10e2705e269839872c95ff0a89588d4")


