extends RigidBody2D
#func _process(delta):
	#on_WallDetector_body_entered()
func _on_WallDetector_body_entered(b):
	b.Break()
func _ready():
	contact_monitor = true

