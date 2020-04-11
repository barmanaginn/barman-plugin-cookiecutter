# {{cookiecutter.repo_name}} - plugin for barman
# Copyright © {{cookiecutter.year}} {{cookiecutter.author}} <{{cookiecutter.email}}>
#
# {{cookiecutter.repo_name}} is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# {{cookiecutter.repo_name}} is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with {{cookiecutter.repo_name}}.  If not, see <https://www.gnu.org/licenses/>.

from django.utils.translation import ugettext_lazy as _

from barman.plugin import BarmanPlugin


class PluginApp(BarmanPlugin):
    name = "{{cookiecutter.module_name}}"

    class BarmanPluginMeta:
        name = "{{cookiecutter.name}}"
        author = "{{cookiecutter.author}}"
        description = _("{{cookiecutter.description}}")
        version = {{cookiecutter.version}}
        url = "{{cookiecutter.repo_url}}"
        email = "{{cookiecutter.email}}"

        # Define here urls for navbar. See documentation for more details.
        nav_urls = ()

        # Define here settings specific to this plugin. See documentation for more details.
        settings = ()

        # Define here additionnal info for user profile. See documentation for more details.
        user_profile = ()

    def ready(self):
        from . import signals
        return super().ready()

default_app_config = "{{cookiecutter.module_name}}.PluginApp"
