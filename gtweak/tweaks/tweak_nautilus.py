# This file is part of gnome-tweak-tool.
#
# Copyright (c) 2011 John Stowers
#
# gnome-tweak-tool is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# gnome-tweak-tool is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with gnome-tweak-tool.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk

import gtweak
from gtweak.utils import AutostartManager
from gtweak.tweakmodel import TweakGroup
from gtweak.widgets import GSettingsSwitchTweak

class DesktopIconTweak(GSettingsSwitchTweak):
    def __init__(self, **options):
        GSettingsSwitchTweak.__init__(self,
            "org.gnome.desktop.background",
            "show-desktop-icons",
            **options)

        #when the user enables nautilus to draw the desktop icons, set nautilus
        #to autostart
        self.nautilus = AutostartManager("nautilus.desktop",
                            autostart_desktop_filename="nautilus-autostart.desktop",
                            exec_cmd="nautilus -n")
        self.settings.connect('changed::'+self.key_name, self._on_setting_changed)

    def _on_setting_changed(self, setting, key):
        self.nautilus.update_start_at_login(
                self.settings.get_boolean(key))

TWEAK_GROUPS = (
        TweakGroup(
            "File Manager",
            DesktopIconTweak()),
)
