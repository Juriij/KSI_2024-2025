class ColorMixer():
    def __init__(self, n):
        pass

    def get(self, i):
        pass

    def set(self, i, color):
        pass

    # both i and j are inclusive
    def mix(self, i, j):
        pass



color_mixer = ColorMixer(9)
print(color_mixer.get(0)) # '000000'
print(color_mixer.mix(0, 8)) # '000000'
color_mixer.set(3, '0000ff')
color_mixer.set(4, 'cccccc')
print(color_mixer.mix(3, 4)) # 'ccccff'
color_mixer.set(3, 'dd00af')
print(color_mixer.mix(3, 4)) # 'ddcccc'
color_mixer.set(8, '12ee42')
print(color_mixer.mix(4, 8)) # 'cceecc'
print(color_mixer.get(0)) # '000000'
print(color_mixer.get(4)) # 'cccccc'
print(color_mixer.get(3)) # 'dd00af'
