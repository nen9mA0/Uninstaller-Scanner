import win32api
import win32con
import os
import re

product_id_ptn = re.compile(r"\{(?P<code>[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12})\}")
product_hkey = win32con.HKEY_LOCAL_MACHINE
product_subkey = r"SOFTWARE\Classes\Installer\Products"

hkey_name_lst = [
    win32con.HKEY_CURRENT_USER,
    win32con.HKEY_LOCAL_MACHINE
]

hkey_type_lst = [
    "HKEY_CURRENT_USER",
    "HKEY_LOCAL_MACHINE"
]

subkey_name_lst = [ r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall",
                r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"]

key_dict = {}

def PrintInfo(display_name, hkey_name, reg_path):
    try:
        key = win32api.RegOpenKey(hkey_name, reg_path, 0, win32con.KEY_READ)
    except:
        return -1
    hkey_type = hkey_type_lst[hkey_name_lst.index(hkey_name)]
    print("=== %s ===" %display_name)
    print("%s\\%s" %(hkey_type, reg_path))
    subkey_len, value_len, modify_time = win32api.RegQueryInfoKey(key)
    for n in range(value_len):
        keyname_tmp = win32api.RegEnumValue(key, n)
        print("\t%s: %s" %(keyname_tmp[0], keyname_tmp[1]))
        a = 0
    win32api.RegCloseKey(key)
    return 0


def Query():
    while True:
        a = input("> ")
        if a == "q":
            break
        try:
            regex = re.compile(a)
        except Exception as e:
            print(e)
            continue

        for new_key in key_dict:
            display_name, mytype = new_key
            p = regex.search(display_name)
            if p:
                hkey_name, reg_path = key_dict[new_key]
                if PrintInfo(display_name, hkey_name, reg_path) != -1:
                    reg_name = os.path.basename(reg_path)
                    q = product_id_ptn.match(reg_name)
                    if q:
                        code = q.group("code")
                        # cvt to product code
                        code_lst = code.split("-")
                        code_str = "".join( [i[::-1] for i in code_lst[:3]] )
                        tmp_str = "".join(code_lst[3:]).replace("-", "")
                        code_str += "".join( [ "%c%c" %(tmp_str[i+1], tmp_str[i]) for i in range(0, len(tmp_str), 2)] )

                        # case insensity in registry
                        # try_subpath = [code_str.upper(), code_str.lower()]
                        reg_path = os.path.join(product_subkey, code_str)
                        try:
                            key = win32api.RegOpenKey(product_hkey, reg_path, 0, win32con.KEY_READ)
                        except:
                            continue
                        print("= Product = : %s\\%s" %(hkey_type_lst[1], reg_path))
                        win32api.RegCloseKey(key)
                    print("\n")



if __name__ == "__main__":
    for hkey_name in hkey_name_lst:
        for subkey_name in subkey_name_lst:
            try:
                key = win32api.RegOpenKey(hkey_name, subkey_name, 0, win32con.KEY_READ)
            except:
                continue
            subkey_len, value_len, modify_time = win32api.RegQueryInfoKey(key)
            for n in range(subkey_len):
                keyname_tmp = win32api.RegEnumKey(key, n)
                new_reg_path = os.path.join(subkey_name, keyname_tmp)
                tmp_key = win32api.RegOpenKey(hkey_name, new_reg_path, 0, win32con.KEY_READ)
                try:
                    display_name = win32api.RegQueryValueEx(tmp_key, "DisplayName")
                    key_dict[display_name] = (hkey_name, new_reg_path)
                except:
                    pass
                win32api.RegCloseKey(tmp_key)

            win32api.RegCloseKey(key)

    Query()