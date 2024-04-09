# Dada una ruta remota de recurso samba debe separar el nombre del equipo (IP) y la ruta.

def samba_split(smb_path):
    cadena_limpia = smb_path[2:]
    index_slash = cadena_limpia.find("/")
    return (f"{cadena_limpia[0:index_slash]}\n{cadena_limpia[index_slash:]}")
    
print(samba_split("//1.1.1.1/aprende/python")) ## "1.1.1.1" "/aprende/python"
print(samba_split('//samba-server/psf/guido'))
print(samba_split('//8.6.4.2/data/work/upload/'))