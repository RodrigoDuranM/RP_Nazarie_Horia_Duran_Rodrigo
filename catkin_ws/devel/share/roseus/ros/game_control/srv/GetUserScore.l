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
  :slots (_score ))

(defmethod game_control::GetUserScoreResponse
  (:init
   (&key
    ((:score __score) 0)
    )
   (send-super :init)
   (setq _score (round __score))
   self)
  (:score
   (&optional __score)
   (if __score (setq _score __score)) _score)
  (:serialization-length
   ()
   (+
    ;; int64 _score
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _score
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _score (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _score) (= (length (_score . bv)) 2)) ;; bignum
              (write-long (ash (elt (_score . bv) 0) 0) s)
              (write-long (ash (elt (_score . bv) 1) -1) s))
             ((and (class _score) (= (length (_score . bv)) 1)) ;; big1
              (write-long (elt (_score . bv) 0) s)
              (write-long (if (>= _score 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _score s)(write-long (if (>= _score 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _score
#+(or :alpha :irix6 :x86_64)
      (setf _score (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _score (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(defclass game_control::GetUserScore
  :super ros::object
  :slots ())

(setf (get game_control::GetUserScore :md5sum-) "6dbf2818ed2a67e5ff5a9a7493308436")
(setf (get game_control::GetUserScore :datatype-) "game_control/GetUserScore")
(setf (get game_control::GetUserScore :request) game_control::GetUserScoreRequest)
(setf (get game_control::GetUserScore :response) game_control::GetUserScoreResponse)

(defmethod game_control::GetUserScoreRequest
  (:response () (instance game_control::GetUserScoreResponse :init)))

(setf (get game_control::GetUserScoreRequest :md5sum-) "6dbf2818ed2a67e5ff5a9a7493308436")
(setf (get game_control::GetUserScoreRequest :datatype-) "game_control/GetUserScoreRequest")
(setf (get game_control::GetUserScoreRequest :definition-)
      "string user_name
---
int64 score

")

(setf (get game_control::GetUserScoreResponse :md5sum-) "6dbf2818ed2a67e5ff5a9a7493308436")
(setf (get game_control::GetUserScoreResponse :datatype-) "game_control/GetUserScoreResponse")
(setf (get game_control::GetUserScoreResponse :definition-)
      "string user_name
---
int64 score

")



(provide :game_control/GetUserScore "6dbf2818ed2a67e5ff5a9a7493308436")


