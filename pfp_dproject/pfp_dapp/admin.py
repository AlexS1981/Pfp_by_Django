

# Register your models here.
from django.contrib import admin
from django.utils.html import format_html

from pfp_dapp.models import CityAddress, DepartamentAddress, Emergency


@admin.register(CityAddress)
class CityAdressAdmin(admin.ModelAdmin):
    list_display = ("ca_address",
                    "ca_house_number",
                    "ca_stores",
                    "ca_show_coordinates"
                    )

    def ca_show_coordinates(self, obj):
        res = "{},\n{}".format(obj.ca_latitude, obj.ca_longitude)
        return res

    ca_show_coordinates.short_description = "Координати"

    def ca_show_map(self, obj):
        box = [float(obj.ca_longitude) - 0.0716067,
               float(obj.ca_latitude) - 0.0232758,
               float(obj.ca_longitude) + 0.0717306,
               float(obj.ca_latitude) + 0.023788
               ]
        return format_html('<br /> \
            <iframe style="border: 2px solid CadetBlue; \
            " src="https://www.openstreetmap.org/export/embed.html?bbox={}%2C{}%2C{}%2C{}&amp; \
            layer=transportmap&amp;marker={}%2C{}" \
            width="400px" height="300px" frameborder="0" marginwidth="0" marginheight="0" \
            scrolling="no"></iframe> \
            <br />',
                box[0], box[1], box[2], box[3],
                obj.ca_latitude, obj.ca_longitude
                           )

    ca_show_map.short_description = "Мапа"

    readonly_fields = ['ca_show_map']
    fields = ("ca_address",
              "ca_house_number",
              "ca_stores",
              'ca_show_map'
              )


@admin.register(DepartamentAddress)
class DepartamentAdressAdmin(admin.ModelAdmin):
    list_display = ("dep_address",
                    "dep_house_number",
                    "dep_show_coordinates",
                    "dep_rapid",
                    "dep_big_tank",
                    "dep_small_ladder",
                    "dep_big_ladder",
                    "dep_chemical")

    def dep_show_coordinates(self, obj):
        res = "{},\n{}".format(obj.dep_latitude, obj.dep_longitude)
        return res

    dep_show_coordinates.short_description = "Координати"

    def dep_show_map(self, obj):
        box = [float(obj.dep_longitude) - 0.0716067,
               float(obj.dep_latitude) - 0.0232758,
               float(obj.dep_longitude) + 0.0717306,
               float(obj.dep_latitude) + 0.023788
               ]
        return format_html('<br /> \
            <iframe style="border: 2px solid CadetBlue; \
            " src="https://www.openstreetmap.org/export/embed.html?bbox={}%2C{}%2C{}%2C{}&amp; \
            layer=transportmap&amp;marker={}%2C{}" \
            width="400px" height="300px" frameborder="0" marginwidth="0" marginheight="0" \
            scrolling="no"></iframe> \
            <br />',
                box[0], box[1], box[2], box[3],
                obj.dep_latitude, obj.dep_longitude
                           )

    dep_show_map.short_description = "Мапа"

    readonly_fields = ['dep_show_map']
    fields = ("dep_address",
              "dep_house_number",
              "dep_rapid",
              "dep_big_tank",
              "dep_small_ladder",
              "dep_big_ladder",
              "dep_chemical",
              "dep_show_map")


@admin.register(Emergency)
class EmergencyAdmin(admin.ModelAdmin):
    list_display = ("em_address",
                    "em_house_number",
                    "em_stores",
                    "em_type",
                    "em_date_created",
                    "em_time_created",
                    "em_show_coordinates",
                    "em_dep_resources",
                    "em_list_resources",
                    "em_activated")

    def em_show_coordinates(self, obj):
        res = "{},\n{}".format(obj.em_latitude, obj.em_longitude)
        return res

    em_show_coordinates.short_description = "Координати"

    def em_show_map(self, obj):
        box = [float(obj.em_longitude) - 0.0716067,
               float(obj.em_latitude) - 0.0232758,
               float(obj.em_longitude) + 0.0717306,
               float(obj.em_latitude) + 0.023788
               ]
        return format_html('<br /> \
                <iframe style="border: 2px solid CadetBlue; \
                " src="https://www.openstreetmap.org/export/embed.html?bbox={}%2C{}%2C{}%2C{}&amp; \
                layer=transportmap&amp;marker={}%2C{}" \
                width="400px" height="300px" frameborder="0" marginwidth="0" marginheight="0" \
                scrolling="no"></iframe> \
                <br />',
                           box[0], box[1], box[2], box[3],
                           obj.em_latitude, obj.em_longitude
                           )

    em_show_map.short_description = "Мапа"

    readonly_fields = ["em_address",
                       "em_house_number",
                       "em_stores",
                       "em_type",
                       "em_date_created",
                       "em_time_created",
                       "em_dep_resources",
                       "em_list_resources",
                       "em_show_map"
                       ]
    fields = ("em_address",
              "em_house_number",
              "em_type",
              "em_date_created",
              "em_time_created",
              "em_dep_resources",
              "em_list_resources",
              "em_activated",
              "em_show_map")


