from typing import override

from archinstall.default_profiles.profile import GreeterType, ProfileType
from archinstall.default_profiles.xorg import XorgProfile


class PlasmaProfile(XorgProfile):
	def __init__(self) -> None:
		super().__init__('KDE Plasma Custom', ProfileType.DesktopEnv)

	@property
	@override
	def packages(self) -> list[str]:
		return [
			'plasma-meta',
			'kitty',
			'kate',
			'dolphin',
			'ark',
			'plasma-workspace',
			'kde-material-you-colors',
			'klassy',
			'python-pywal16',
			'fish',
			'yay',

		]
		#hopefully custom repos work lmao

	@property
	@override
	def default_greeter_type(self) -> GreeterType:
		return GreeterType.Sddm
