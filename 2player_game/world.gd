extends Spatial
onready var camera1 = $player/Spatial/SpringArm/Camera
onready var camera2 = $player2/Spatial/SpringArm/Camera

func _ready():
	pass
	
func _input(event):
	if Input.is_action_pressed("control"):
		var stemp_state = $player2.active
		$player2.active = $player.active
		$player.active = stemp_state
		if Input.is_action_pressed("control"):
			if camera1.is_current():
				camera1.clear_current(true)
			elif camera2.is_current():
				camera2.clear_current(true)
