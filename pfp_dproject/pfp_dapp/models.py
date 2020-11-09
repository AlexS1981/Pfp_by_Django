import os
import datetime
import json
import re
import math
from django.db import models

# Create your models here.

os.chdir(os.getcwd())


class Pfp(models.Model):

    list_week = ["Понеділок", "Вівторок", "Середа", "Четвер", \
                 "Пʼятниця", "Субота", "Неділя"]
    list_year = ["Січня", "Лютого", "Березня", "Квітня", "Травня", "Червня", \
                 "Липня", "Серпня", "Вересня", "Жовтня", "Листопада", "Грудня"]
    pfp_id = models.AutoField(primary_key=True)
    dt = models.CharField(int(datetime.datetime.strftime(datetime.datetime.now(), '%d')), \
    list_year[int(datetime.datetime.strftime(datetime.datetime.now(), '%m'))-1], \
    datetime.datetime.strftime(datetime.datetime.now(), '%Y року.'), \
    list_week[datetime.datetime.now().weekday()], \
    datetime.datetime.strftime(datetime.datetime.now(), 'Час: %H:%M:%S'))
    dialog_data = dict()
    address_data = dict()
    departament_data = dict()

    def write_data(self, dict_to_write):
        fr = open("pfp_data.json", 'r')
        str_data = str()
        str_end = str()
        for line in fr:
            str_data += line[0: len(line) - 1]
            str_end = line[len(line) - 1:]
        str_data += str_end
        dict_data = json.loads(str_data)
        list_data = ["dialog_data", "address_data", "departament_data"]
        self.dialog_data = dict_data.get(list_data[0])
        self.address_data = dict_data.get(list_data[1])
        self.departament_data = dict_data.get(list_data[2])
        fr.close()
        if dict_to_write.get(list_data[0]) != None:
            self.dialog_data.update(dict_to_write.get(list_data[0]))
        elif dict_to_write.get(list_data[1]) != None:
            self.address_data.update(dict_to_write.get(list_data[1]))
        elif dict_to_write.get(list_data[2]) != None:
            self.departament_data.update(dict_to_write.get(list_data[2]))
        str_new = '{\n\t"' + str(list_data[0]) + '": {\n'
        for key in self.dialog_data:
            if str(self.dialog_data.get(key))[0] == "[":
                str_new += '\t\t"' + key + '": ' + str(self.dialog_data.get(key)).replace("'",'"') + ',\n'
            else:
                str_new += '\t\t"' + key + '": ' + '"' + str(self.dialog_data.get(key)).replace("'",'"') + '",\n'
        str_new_end = str_new[0:len(str_new) - 2]
        str_new = str_new_end + "\n\t},\n"
        str_new += '\t"' + str(list_data[1]) + '": {\n'
        for key in self.address_data:
            str_new += '\t\t"' + key + '": ' + str(self.address_data.get(key)).replace("'", '"') + ',\n'
        str_new_end = str_new[0:len(str_new) - 2]
        str_new = str_new_end + "\n\t},\n"
        str_new += '\t"' + str(list_data[2]) + '": {\n'
        for key in self.departament_data:
            if str(self.departament_data.get(key))[0] == "[":
                str_new += '\t\t"' + key + '": ' + str(self.departament_data.get(key)).replace("'", '"') + ',\n'
            else:
                str_new += '\t\t"' + key + '": ' + '"' + str(self.departament_data.get(key)).replace("'", '"') + '",\n'
        str_new_end = str_new[0:len(str_new) - 2]
        str_new = str_new_end + "\n\t}\n}\n"

        fw = open("pfp_data.json", 'w')
        fw.write(str_new)
        fw.close()

    def load_data(self):
        f = open("pfp_data.json", 'r')
        str_data = str()
        str_end = str()
        for line in f:
            str_data += line[0: len(line) - 1]
            str_end = line[len(line) - 1:]
        str_data += str_end
        f.close()
        dict_data = json.loads(str_data)
        self.dialog_data = dict_data.get("dialog_data")
        self.address_data = dict_data.get("address_data")
        self.departament_data = dict_data.get("departament_data")

    def get_call_data(self):
        print("{} {} {} {}. {}\n" \
              .format(self.dt[0], self.dt[1], self.dt[2], self.dt[3], self.dt[4]))
        print(self.dialog_data.get("001"))
        e_type_res = self.list_dialog(self.dialog_data.get("002"), 0)
        if e_type_res == 0:
            return print(self.dialog_data.get("000"))
        print(self.dialog_data.get("003"))
        e_nature_res = self.list_dialog(self.dialog_data.get("004"), 0)
        if e_nature_res == 0:
            return print(self.dialog_data.get("000"))
        print(self.dialog_data.get("005"))
        e_level_res = self.list_dialog(self.dialog_data.get("006"), 0)
        if e_level_res == 0:
            return print(self.dialog_data.get("000"))

        list_em = [e_type_res, e_nature_res, e_level_res]
        return list_em

    @staticmethod
    def list_dialog(description, param):
        inp = str()
        while inp != 0:
            for i in range(len(description) - 1):
                print("{}. {};".format(i + 1, description[i]))
            print("{}. {}".format(len(description), description[len(description) - 1]))
            err = 'Не вірна цифра! Або введіть цифру повторно, або "0" для завершення програми.'
            try:
                inp = int(input("Введіть цифру: "))
                if inp == 0:
                    return 0
                elif param == 0:
                    return description[inp - 1]
                elif param == 1:
                    s = len(description[inp - 1]) - 6
                    s_1 = len(description[inp - 1]) - 1
                    return description[inp - 1][s: s_1]
            except IndexError:
                print(err)
            except ValueError:
                print(err)


class Emergency(models.Model):
    """
    Содержит: тип ЧС (пожар, наводнение...),
    характер (природный или техногенный),
    уровень (международный, государственный,
    региональный, местный, объектовый)
    """
    def __init__(self, e_em, e_code = 0):
        self.e_type = e_em[0]
        self.e_nature = e_em[1]
        self.e_level = e_em[2]
        self.em_address = str()
        self.e_code = e_code
        self.dep_data = list()


    def emergency_info(self, em_address):
        self.em_address = em_address
        print("\n{}, {} характеру, {} рівня" \
              .format(self.e_type, str.lower(self.e_nature), str.lower(self.e_level)))
        print("\nЧС трапилось за адресою: {}".format(self.em_address))

    def emergency_navigate(self, cl_name):
        d = EmergencyNavigation(self.em_address, \
                                            cl_name.address_data.get(self.em_address)[0], \
                                            cl_name.address_data.get(self.em_address)[1], \
                                            cl_name.address_data.get(self.em_address)[2], \
                                            cl_name)
        self.dep_data = d.minimal_distance()
        print()
        print("Відстань до найближчої частини: ", self.dep_data[0], \
              "км.\nАдреса частини:", self.dep_data[1])

    def get_emergency_code(self):
        """
        По данным пользователя устанавливается характер и уровень,
        и формируется код ЧС.
        """
        dict_group = dict()
        dict_subclass = dict()
        dict_class = dict()
        dict_em = dict()
        list_subclass = list()
        list_class = list()
        list_em = list()
        print("\nФормуємо код ЧС:")

        for key in self.dict_emergency:
            if int(key) % 10000 == 0:
                dict_group.update({key: self.dict_emergency.get(key)})
        list_group = [(self.dict_emergency.pop(key) + " (код: " + key + ")") for key in dict_group]
        str_code_inp = Pfp.list_dialog(list_group, 1)

        for key in self.dict_emergency:
            if int(key) % 100 == 0:
                dict_subclass.update({key: self.dict_emergency.get(key)})
        for key in dict_subclass:
            if (int(key) >= int(str_code_inp)) and (int(key) < int(str_code_inp) + 10000):
                list_subclass.append(self.dict_emergency.pop(key) + " (код: " + key + ")")
        str_code_inp = Pfp.list_dialog(list_subclass, 1)

        for key in self.dict_emergency:
            if int(key) % 10 == 0:
                dict_class.update({key: self.dict_emergency.get(key)})
        for key in dict_class:
            if (int(key) >= int(str_code_inp)) and (int(key) < int(str_code_inp) + 100):
                list_class.append(self.dict_emergency.pop(key) + " (код: " + key + ")")
        str_code_inp = Pfp.list_dialog(list_class, 1)

        for key in self.dict_emergency:
            dict_em.update({key: self.dict_emergency.get(key)})
        for key in dict_em:
            if (int(key) >= int(str_code_inp)) and (int(key) < int(str_code_inp) + 10):
                list_em.append(self.dict_emergency.pop(key) + " (код: " + key + ")")
        if len(list_em) > 0:
            str_code_inp = Pfp.list_dialog(list_em, 1)

        self.e_code = int(str_code_inp)
        return int(self.e_code)

    def read_emergency_classifier(self):
        """
        Читает из файла форматированный текст классификатора ЧС.
        Возвращает словарь
        """
        f = open("Emergency_classifier.txt", 'r')
        str_end = str()
        list_data = list()
        dict_data = dict()
        for line in f:
            list_data.append(line[0: len(line) - 1])
            str_end = line[len(line) - 1:]
        end = list_data[len(list_data) - 1]
        list_data[len(list_data) - 1] = end + str_end
        f.close()
        count = 0
        iter_data = iter(list_data)
        for i in iter_data:
            if i[0:7] == '-------':
                count += 1
            if len(i) > 0\
                    and i[0] == '|'\
                    and str.isdigit(i[1:6])\
                    and count < 2:
                last_key = i[1:6]
                last_val = re.sub(" +", " ", i[7:65])
                if last_val[len(last_val) - 1] == " ":
                    val_1 = last_val[0:len(last_val) - 1]
                    last_val = val_1
                dict_data.update({last_key:last_val})
                i = next(iter_data)
                try:
                    while i[6] != '+':
                        new_val = "\n" + re.sub(" +", " ", i[7:65])
                        if new_val[len(new_val) - 1] == " ":
                            val_2 = new_val[0:len(new_val) - 1]
                            new_val = val_2
                        if new_val[1:3] != '--':
                            dict_data.update({last_key: last_val + new_val})
                            last_val = last_val + new_val
                        i = next(iter_data)
                except IndexError:
                    continue
        self.dict_emergency = dict_data