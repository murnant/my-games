extends Spatial
var BULLET = []
var timer = 0
var bullet_pick = 0
func _ready():
	BULLET.append(preload('bullet.tscn'))
	BULLET.append(preload('flare.tscn'))
	BULLET.append(preload('cluster.tscn'))
func _process(delta):
	timer -= 1
	if Input.is_action_pressed("space") and timer <= 0:
		var bullet = BULLET[bullet_pick].instance()
		bullet.global_transform = $Position3D.global_transform
		get_node("/root").add_child(bullet)
		timer = 50
	if Input.is_action_pressed("switch_up"):
		if bullet_pick < len(BULLET) -1:
			bullet_pick += 1
		else:
			bullet_pick = 0
