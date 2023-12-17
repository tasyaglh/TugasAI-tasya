sasuke_do_example = 'Halo.. Nama saya sasuke, saya berusia 17 tahun!'
print(sasuke_do_example)

sasuke_do_example = sasuke_do_example.split(" ")
print(sasuke_do_example)
print(f"index-6: {sasuke_do_example[6]}")
print(f"type index-6: {type(sasuke_do_example[6])}")

sasuke_do_example[6] = int(sasuke_do_example[6])
print(sasuke_do_example)
print(f"index-6: {sasuke_do_example[6]}")
print(f"type index-6: {type(sasuke_do_example[6])}")