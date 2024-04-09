# Implemente un "clon" de Akinator que permita adivinar el personaje de Marvel en base a las tres preguntas siguientes:             │
# │                                                                                                                                   │
# │  1 ¿Puede volar? → Se representa por la variable de entrada: can_fly                                                              │
# │  2 ¿Es humano? → Se representa por la variable de entrada: is_human                                                               │
# │  3 ¿Tiene máscara? → Se representa por la variable de entrada: has_mask

#                                 ✔                                                                                │
# │                                              ┌──────► Ironman                                                                     │
# │                                ✔             │                                                                                    │
# │                              ┌───► Has mask? │                                                                                    │
# │                              │               │                                                                                    │
# │                              │               └──────► Captain Marvel                                                              │
# │                              │                   ˟                                                                                │
# │               ✔              │                                                                                                    │
# │           ┌──────► Is human? │                                                                                                    │
# │           │                  │                   ✔                                                                                │
# │           │                  │               ┌──────► Ronan Accuser                                                               │
# │           │                  │               │                                                                                    │
# │           │                  └───► Has mask? │                                                                                    │
# │           │                    ˟             │                                                                                    │
# │           │                                  └──────► Vision                                                                      │
# │           │                                      ˟                                                                                │
# │           │                                                                                                                       │
# │  Can fly? │                                                                                                                       │
# │           │                                      ✔                                                                                │
# │           │                                  ┌──────► Spiderman                                                                   │
# │           │                    ✔             │                                                                                    │
# │           │                  ┌───► Has mask? │                                                                                    │
# │           │                  │               │                                                                                    │
# │           │                  │               └──────► Hulk                                                                        │
# │           │                  │                   ˟                                                                                │
# │           │                  │                                                                                                    │
# │           └──────► Is human? │                                                                                                    │
# │               ˟              │                   ✔                                                                                │
# │                              │               ┌──────► Black Bolt                                                                  │
# │                              │               │                                                                                    │
# │                              └───► Has mask? │                                                                                    │
# │                                ˟             │                                                                                    │
# │                                              └──────► Thanos                                                                      │
# │                                                  ˟

def marvel_akinator_2(can_fly, is_human, has_mask):
    if can_fly and is_human and has_mask:
        return "Iroman"
    if can_fly and is_human and not has_mask:
        return "Capitan Marvel"
    if can_fly and not is_human and has_mask:
        return "Ronan Accuser"
    if can_fly and not is_human and not has_mask:
        return "Vision"
    if not can_fly and is_human and has_mask:
        return "Spiderman"
    if not can_fly and is_human and not has_mask:
        return "Hulk"
    if not can_fly and not is_human and has_mask:
        return "Black Bold"
    if not can_fly and not is_human and not has_mask:
        return "Thonos"
                
print(marvel_akinator_2(False, True, True))
print(marvel_akinator_2(True, False, True))
print(marvel_akinator_2(False, False, True))
print (marvel_akinator_2(True, True, False))
        