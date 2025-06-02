from typing import override

from archinstall.default_profiles.profile import GreeterType, ProfileType
from archinstall.default_profiles.xorg import XorgProfile


class PlasmaProfile(XorgProfile):
	def __init__(self) -> None:
		super().__init__('Wayfire Custom', ProfileType.DesktopEnv)

	@property
	@override
	def packages(self) -> list[str]:
		return [
			'wayfire-git',
			'kitty',
			'kate',
			'dolphin',
			'ark',
			'wofi',
			'waybar',
			'mako',
			'python-pywal16',
			'xdg-desktop-portal-wlr',
			'xdg-desktop-portal-gtk',
			'grim',
			'slurp',
			'qt5-wayland',
			'qt6-wayland',
			'polkit',
			'polkit-kde-agent',
			'yay',
			'fish',
			'waypaper',
			'swww',
			'mpvpaper',

		]
		#hopefully custom repos work lmao

	@property
	@override
	def default_greeter_type(self) -> GreeterType:
		return GreeterType.Sddm
